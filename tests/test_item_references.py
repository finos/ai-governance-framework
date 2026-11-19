#!/usr/bin/env python3
"""
Test suite for the #426 item-reference checks.

Stdlib + PyYAML only, matching the repo's existing dependencies.
Each case builds a throwaway fixture repo, so nothing depends on the
real catalogue except the integration cases.

Usage:  python3 tests/test_item_references.py [path-to-real-clone]
"""
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

PASSED, FAILED = [], []


# ---------------------------------------------------------------- fixtures

def build_repo(base, standards, items):
    """standards: {name: {'lens':..., 'entries':[keys], 'superseded':{old:new}}}
       items:     {collection: {item_id: {'domain':..., 'refs':{ds:[keys]}, 'raw':str}}}"""
    refdir = os.path.join(base, "docs", "_data", "references")
    os.makedirs(refdir, exist_ok=True)
    for name, spec in standards.items():
        lines = ['title: "T"', 'description: "D"']
        if spec.get("lens") is not None:
            lines.append(f"lens: {spec['lens']}")
        lines.append("entries:")
        for key in spec.get("entries", []):
            lines.append(f"  {key}:")
            lines.append(f'    title: "{key}"')
            lines.append(f'    url: "https://example.org/{key}"')
            if key in spec.get("superseded", {}):
                lines.append(f"    superseded_by: {spec['superseded'][key]}")
        open(os.path.join(refdir, f"{name}.yml"), "w").write("\n".join(lines) + "\n")

    for collection, members in items.items():
        d = os.path.join(base, "docs", collection)
        os.makedirs(d, exist_ok=True)
        for item_id, spec in members.items():
            path = os.path.join(d, f"{item_id}_fixture.md")
            if "raw" in spec:
                open(path, "w").write(spec["raw"])
                continue
            fm = ["---", f"sequence: {item_id.split('-')[1]}", f"title: {item_id}",
                  f"domain: {spec.get('domain', 'components')}"]
            for ds, keys in spec.get("refs", {}).items():
                fm.append(f"{ds}_references:")
                for k in keys:
                    fm.append(f"  - {k}")
            fm += ["---", "", "## Summary", "body"]
            open(path, "w").write("\n".join(fm) + "\n")
    return base


STD = {
    "owasp-llm":  {"lens": "threat",     "entries": [f"llm{i}" for i in range(1, 9)]},
    "owasp-asi":  {"lens": "threat",     "entries": ["asi1", "asi2"]},
    "eu-ai-act":  {"lens": "obligation", "entries": [f"a{i}" for i in range(1, 9)]},
    "iosco-supervisory-toolkit": {"lens": "obligation", "entries": ["t1", "t2"]},
    "iso-42001":  {"lens": "control",    "entries": ["c1", "c2"]},
    "nist-sp-800-53r5": {"lens": "control", "entries": [f"n{i}" for i in range(1, 9)]},
}


def fixture(items, standards=None):
    base = tempfile.mkdtemp(prefix="aigf-test-")
    return build_repo(base, standards or STD, items)


# ---------------------------------------------------------------- harness

def check(test_id, description, actual, expected):
    ok = actual == expected
    (PASSED if ok else FAILED).append(test_id)
    mark = "PASS" if ok else "FAIL"
    print(f"  [{mark}] {test_id}  {description}")
    if not ok:
        print(f"         expected: {expected!r}")
        print(f"         actual:   {actual!r}")


# ------------------------------------------------- implementation under test
# Imported from the script, not reimplemented, so a bug in the script fails here.

import importlib.util  # noqa: E402

SCRIPT = os.environ.get(
    "AIGF_SCRIPT",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "scripts",
                 "validate-item-references.py"),
)


def load_module_for(root):
    """Import the script with its ROOT pointed at a fixture repo."""
    spec = importlib.util.spec_from_file_location("vir", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.ROOT = root
    module.DOCS_DIR = os.path.join(root, "docs")
    module.REFERENCES_DIR = os.path.join(module.DOCS_DIR, "_data", "references")
    module.PARSE_FAILURES.clear()
    module.MALFORMED_REFERENCES.clear()
    module._ITEM_CACHE.clear()
    return module


def floor_findings(root, strict_iosco=True):
    m = load_module_for(root)
    findings, unknown = m.check_floor(m.load_library(m.REFERENCES_DIR),
                                      strict_iosco=strict_iosco)
    return sorted((item_id, tuple(missing)) for _, item_id, _, missing in findings), sorted(unknown)


def cap_findings(root):
    m = load_module_for(root)
    findings, _duplicates = m.check_cap()
    return sorted((item_id, dataset, count)
                  for _, item_id, _, dataset, count in findings)


def reverse_findings(root):
    m = load_module_for(root)
    usage, dangling, stale, _unknown = m.check_reverse(m.load_library(m.REFERENCES_DIR))
    return (sorted((ds, k) for ds, k, _ in dangling),
            sorted((ds, k, nxt) for ds, k, nxt, _ in stale),
            {ds: row["unused"] for ds, row in usage.items()})


# ---------------------------------------------------------------- the tests

def section_1_floor_risks():
    print("\n1. Floor check — risks")
    cases = [
        ("F-01", "threat + obligation", {"owasp-llm": ["llm1"], "eu-ai-act": ["a1"]}, []),
        ("F-02", "threat only", {"owasp-llm": ["llm1"]}, [("ri-1", ("obligation",))]),
        ("F-03", "obligation only", {"eu-ai-act": ["a1"]}, [("ri-1", ("threat",))]),
        ("F-04", "no references", {}, [("ri-1", ("threat", "obligation"))]),
        ("F-05", "empty reference list", {"owasp-llm": []},
         [("ri-1", ("threat", "obligation"))]),
        ("F-06", "control only", {"iso-42001": ["c1"]},
         [("ri-1", ("threat", "obligation"))]),
        ("F-07", "two standards, same lens", {"owasp-llm": ["llm1"], "owasp-asi": ["asi1"]},
         [("ri-1", ("obligation",))]),
    ]
    for tid, desc, refs, expected in cases:
        root = fixture({"_risks": {"ri-1": {"refs": refs}}})
        try:
            check(tid, desc, floor_findings(root)[0], expected)
        finally:
            shutil.rmtree(root)


def section_2_floor_mitigations_iosco():
    print("\n2. Floor check — mitigations and the IOSCO switch")
    mit = [
        ("F-08", "mitigation cites a control", {"nist-sp-800-53r5": ["n1"]}, []),
        ("F-09", "mitigation cites no control", {"owasp-llm": ["llm1"]},
         [("mi-1", ("control",))]),
        ("F-10", "mitigation needs no threat/obligation", {"iso-42001": ["c1"]}, []),
    ]
    for tid, desc, refs, expected in mit:
        root = fixture({"_mitigations": {"mi-1": {"refs": refs}}})
        try:
            check(tid, desc, floor_findings(root)[0], expected)
        finally:
            shutil.rmtree(root)

    iosco_only = {"owasp-llm": ["llm1"], "iosco-supervisory-toolkit": ["t1"]}
    root = fixture({"_risks": {"ri-1": {"refs": iosco_only}}})
    try:
        check("F-11", "IOSCO-only, --lenient-iosco",
              floor_findings(root, strict_iosco=False)[0], [])
        check("F-12", "IOSCO-only, default mode",
              floor_findings(root)[0], [("ri-1", ("obligation",))])
    finally:
        shutil.rmtree(root)

    both = {"owasp-llm": ["llm1"], "iosco-supervisory-toolkit": ["t1"], "eu-ai-act": ["a1"]}
    root = fixture({"_risks": {"ri-1": {"refs": both}}})
    try:
        check("F-13", "IOSCO + EU AI Act, default mode",
              floor_findings(root)[0], [])
    finally:
        shutil.rmtree(root)


def section_3_cap():
    print("\n3. Cap check")
    cases = [
        ("C-01", "exactly 3 (boundary)", {"eu-ai-act": ["a1", "a2", "a3"]}, []),
        ("C-02", "exactly 4 (boundary)", {"eu-ai-act": ["a1", "a2", "a3", "a4"]},
         [("ri-1", "eu-ai-act", 4)]),
        ("C-03", "zero references", {}, []),
        ("C-04", "two standards over cap",
         {"eu-ai-act": ["a1", "a2", "a3", "a4", "a5"], "owasp-llm": ["llm1", "llm2", "llm3", "llm4"]},
         [("ri-1", "eu-ai-act", 5), ("ri-1", "owasp-llm", 4)]),
        ("C-05", "3 each from four standards",
         {"eu-ai-act": ["a1", "a2", "a3"], "owasp-llm": ["llm1", "llm2", "llm3"],
          "iso-42001": ["c1", "c2"], "owasp-asi": ["asi1", "asi2"]}, []),
    ]
    for tid, desc, refs, expected in cases:
        root = fixture({"_risks": {"ri-1": {"refs": refs}}})
        try:
            check(tid, desc, cap_findings(root), expected)
        finally:
            shutil.rmtree(root)

    std = dict(STD, nolens={"lens": None, "entries": ["x1", "x2", "x3", "x4", "x5"]})
    root = fixture({"_risks": {"ri-1": {"refs": {"nolens": ["x1", "x2", "x3", "x4", "x5"]}}}}, std)
    try:
        check("C-06", "cap ignores lens", cap_findings(root), [("ri-1", "nolens", 5)])
    finally:
        shutil.rmtree(root)


def section_4_reverse():
    print("\n4. Reverse coverage")
    std = {"owasp-llm": {"lens": "threat", "entries": ["llm1", "llm2"]}}
    root = fixture({"_risks": {"ri-1": {"refs": {"owasp-llm": ["llm1"]}}}}, std)
    try:
        dangling, stale, unused = reverse_findings(root)
        check("R-01", "one cited, one not", unused["owasp-llm"], 1)
        check("R-02", "no dangling when keys exist", dangling, [])
    finally:
        shutil.rmtree(root)

    root = fixture({"_risks": {"ri-1": {"refs": {"owasp-llm": ["nope-99"]}}}}, std)
    try:
        check("R-03", "cited key absent from library",
              reverse_findings(root)[0], [("owasp-llm", "nope-99")])
    finally:
        shutil.rmtree(root)

    sup = {"owasp-llm": {"lens": "threat", "entries": ["old1", "new1"],
                         "superseded": {"old1": "new1"}}}
    root = fixture({"_risks": {"ri-1": {"refs": {"owasp-llm": ["old1"]}}}}, sup)
    try:
        check("R-04", "superseded entry cited",
              reverse_findings(root)[1], [("owasp-llm", "old1", "new1")])
    finally:
        shutil.rmtree(root)

    root = fixture({"_risks": {"ri-1": {"refs": {"owasp-llm": ["new1"]}}}}, sup)
    try:
        check("R-05", "superseded entry not cited", reverse_findings(root)[1], [])
    finally:
        shutil.rmtree(root)

    root = fixture({"_usecases": {"uc-1": {"refs": {"owasp-llm": ["llm1"]}}}}, std)
    try:
        check("R-06", "use-case citation counts", reverse_findings(root)[2]["owasp-llm"], 1)
    finally:
        shutil.rmtree(root)


def section_5_robustness():
    print("\n5. Robustness")
    root = fixture({"_risks": {"ri-1": {"raw": "# No front matter\n\ntext\n"}}})
    try:
        check("E-01", "no front matter", floor_findings(root)[0], [])
    finally:
        shutil.rmtree(root)

    root = fixture({"_risks": {"ri-1": {"refs": {"owasp-llm": ["llm1"], "eu-ai-act": ["a1"]}}}})
    open(os.path.join(root, "docs", "_risks", "README.md"), "w").write("# Notes\n")
    try:
        check("E-02", "non-conforming filename", floor_findings(root)[0], [])
    finally:
        shutil.rmtree(root)

    std = dict(STD, owasp_nolens={"lens": None, "entries": ["z1"]})
    root = fixture({"_risks": {"ri-1": {"refs": {"owasp_nolens": ["z1"], "eu-ai-act": ["a1"]}}}}, std)
    try:
        findings, warnings = floor_findings(root)
        check("E-03", "reference file missing lens -> warning", warnings, ["owasp_nolens"])
    finally:
        shutil.rmtree(root)

    root = fixture({"_risks": {"ri-1": {"refs": {"made-up": ["q1"], "eu-ai-act": ["a1"]}}}})
    try:
        findings, warnings = floor_findings(root)
        check("E-04", "dataset with no library file", warnings, ["made-up"])
    finally:
        shutil.rmtree(root)

    root = fixture({"_risks": {}})
    try:
        check("E-05", "empty collection", floor_findings(root)[0], [])
    finally:
        shutil.rmtree(root)

    root = fixture({"_risks": {"ri-1": {"refs": {"owasp-llm": ["llm1"], "eu-ai-act": ["a1"]}}}})
    open(os.path.join(root, "docs", "_risks", "notes.txt"), "w").write("ignore me\n")
    try:
        check("E-06", "non-markdown file ignored", floor_findings(root)[0], [])
    finally:
        shutil.rmtree(root)


def section_6_integration(real):
    print(f"\n6. Integration — real repository at {real}")
    findings, warnings = floor_findings(real, strict_iosco=True)
    lenient, _ = floor_findings(real, strict_iosco=False)
    check("I-01", "floor --lenient-iosco -> only ri-30",
          [i for i, _ in lenient], ["ri-30"])
    strict = findings
    check("I-02", "floor default (strict) -> ri-24..ri-30",
          [i for i, _ in strict],
          ["ri-24", "ri-25", "ri-26", "ri-27", "ri-28", "ri-29", "ri-30"])
    check("I-03", "no mitigation below floor",
          [i for i, _ in findings if i.startswith("mi-")], [])
    dangling, stale, _ = reverse_findings(real)
    check("I-04", "no dangling citations", dangling, [])
    check("I-05", "two superseded cited, both owasp-llm",
          [(ds, k) for ds, k, _ in stale],
          [("owasp-llm", "llm03-2025"), ("owasp-llm", "llm06-2025")])
    over = {i for i, _, _ in cap_findings(real)}
    check("I-06", "items over cap", len(over), 39)
    check("I-07", "no missing-lens warnings", warnings, [])


if __name__ == "__main__":
    section_1_floor_risks()
    section_2_floor_mitigations_iosco()
    section_3_cap()
    section_4_reverse()
    section_5_robustness()
    if len(sys.argv) > 1:
        section_6_integration(sys.argv[1])
    else:
        print("\n6. Integration — skipped (pass a clone path to run)")

    print(f"\n{'=' * 60}")
    print(f"  {len(PASSED)} passed, {len(FAILED)} failed")
    if FAILED:
        print(f"  failed: {', '.join(FAILED)}")
    sys.exit(1 if FAILED else 0)
