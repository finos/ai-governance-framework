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
}


def check(report):
    totals = report["totals"]
    if report["suite"] != "vectors-receipt-signature" or report["rail"] != "external":
        return "wrong suite or rail"
    if (totals["vectors"] != 13 or totals["conform"] != 13
            or totals["fail"] or totals["suiteRefusals"]
            or report["verifier"]["vectorsExecuted"] != 13):
        return "external verifier did not pass all 13 vectors"

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
        error = check(json.load(source))
    if error:
        print(error, file=sys.stderr)
        sys.exit(1)
    print("MI-21: external verifier passed 13 vectors, including the three pinned cases")
