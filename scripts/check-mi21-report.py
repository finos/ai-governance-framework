#!/usr/bin/env python3
"""Check that the MI-21 run exercised an external verifier on the pinned cases."""

import json
import sys


CASES = {
    "v4f9fe96e52a39bfb": ("valid", "valid"),
    "ve116653dd041dda0": ("invalid signature_invalid", "invalid signature_invalid"),
    "v5397adb77c3e6754": (
        "invalid signature_in_signing_input", "invalid signature_in_signing_input"
    ),
    "vb27b15aa51e9da9b": ("invalid malformed_chain_link", "invalid malformed_chain_link"),
    "v967bcffede491026": ("invalid chain_link_mismatch", "invalid chain_link_mismatch"),
    "v429ea40212de7b5d": ("undecidable window_not_applicable", "valid"),
}


def check(report):
    totals = report["totals"]
    if report["suite"] != "vectors-receipt-signature" or report["rail"] != "external":
        return "wrong suite or rail"
    if (totals["vectors"] < 29 or totals["conform"] != totals["vectors"]
            or totals["fail"] or totals["suiteRefusals"]
            or report["verifier"]["vectorsExecuted"] != totals["vectors"]):
        return "external verifier did not pass every vector of a corpus of at least 29"

    rows = {row["id"]: row for row in report["vectors"]}
    for case, (windows, no_windows) in CASES.items():
        row = rows.get(case)
        if (not row or not row["verifierRan"] or row["status"] != "PASS"
                or row["withWindows"] != windows
                or row["withoutWindows"] != no_windows):
            return f"wrong result for {case}"
    return None


if __name__ == "__main__":
    with open(sys.argv[1], encoding="utf-8") as source:
        report = json.load(source)
    error = check(report)
    if error:
        print(error, file=sys.stderr)
        sys.exit(1)
    print(f"MI-21: external verifier passed {report['totals']['vectors']} vectors, "
          "including the pinned cases")
