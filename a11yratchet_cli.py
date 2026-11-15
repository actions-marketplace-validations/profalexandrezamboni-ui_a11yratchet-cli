#!/usr/bin/env python3
"""Zero-dependency CLI for A11yRatchet WCAG 2.2 AA & EN 301 549 Baseline Ratchet."""
import argparse, json, pathlib, sys, urllib.request

EDGE_URL = "https://specgate.profalexandrezamboni.workers.dev/api/v1/a11yratchet/evaluate"

def main() -> int:
    p = argparse.ArgumentParser(description="A11yRatchet WCAG 2.2 & EN 301 549 CI Gate")
    p.add_argument("--report", required=True, help="Path to axe-core JSON report")
    args, _ = p.parse_known_args()
    payload = {"axe_report": json.loads(pathlib.Path(args.report).read_text(encoding="utf-8"))}
    req = urllib.request.Request(EDGE_URL, data=json.dumps(payload).encode("utf-8"), headers={"Content-Type": "application/json", "User-Agent": "a11yratchet-cli/1.1.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        res = json.loads(resp.read().decode("utf-8"))
    print(json.dumps(res, indent=2))
    if not res.get("gate_passed", res.get("ratchet_gate_passed", res.get("verdict") == "PASS")):
        print(f"\n[A11yRatchet] Net-new WCAG 2.2 / EN 301 549 regression! Export compliance bundles ($19/mo Starter · $39/mo Team): https://specgate.profalexandrezamboni.workers.dev/#pricing", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
