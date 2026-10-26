#!/usr/bin/env python3
"""Run the Veritas Acta receipt verifier through the MI-21 vector contract."""

import json
import os
import subprocess
import sys
import tempfile


def run(*args):
    return subprocess.run(["verify", *args], capture_output=True, text=True, timeout=60)


def main():
    if len(sys.argv) != 2 or not os.getenv("AEV_RECEIPT_JWKS"):
        print("receipt path and AEV_RECEIPT_JWKS required", file=sys.stderr)
        return 3

    receipt = sys.argv[1]
    result = run(receipt, "--jwks", os.environ["AEV_RECEIPT_JWKS"],
                 "--mode", "receipt", "--json")
    if result.returncode not in (0, 1, 2):
        print(result.stderr or result.stdout, file=sys.stderr)
        return 3
    try:
        report = json.loads(result.stdout)
    except ValueError:
        print(result.stdout, file=sys.stderr)
        return 3

    code = report.get("error")
    if isinstance(code, dict):
        code = code.get("code")
    if code == "invalid_signature":
        code = "signature_invalid"

    status = result.returncode
    if status == 0 and os.getenv("AEV_RECEIPT_CONTEXT"):
        with open(os.environ["AEV_RECEIPT_CONTEXT"], encoding="utf-8") as source:
            chain = json.load(source)["chain"]
        with tempfile.TemporaryDirectory() as work:
            path = os.path.join(work, "chain.jsonl")
            with open(path, "w", encoding="utf-8") as output:
                for member in [*chain, receipt]:
                    with open(member, encoding="utf-8") as source:
                        output.write(json.dumps(json.load(source)) + "\n")
            replay = run("--replay-chain", path, "--json")
        try:
            breaks = json.loads(replay.stdout)["chainBreaks"]
        except (ValueError, KeyError, TypeError):
            print(replay.stderr or replay.stdout, file=sys.stderr)
            return 3
        if breaks:
            status, code = 1, "chain_link_mismatch"

    verdict = ("valid", "invalid", "undecidable")[status]
    print(json.dumps({"verdict": verdict, "code": None if status == 0 else code}))
    return status


if __name__ == "__main__":
    raise SystemExit(main())
