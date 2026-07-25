"""
analyze_headers.py

Educational, defensive script for Mini Project 1 (Phishing Mail awareness).
Parses a raw email (.eml) file's headers and flags common phishing/spoofing
indicators: SPF/DKIM/DMARC failures, mismatched Return-Path vs From, and
suspicious Reply-To differences.

This tool only *reads and reports on* headers of an email you already have
(e.g., a suspicious email you exported as .eml, or one of your own test
emails) — it does not send, forge, or interact with any live mail server.

Usage:
    python3 analyze_headers.py path/to/email.eml
"""

import sys
import email
from email import policy
from email.parser import BytesParser


def get_domain(address: str) -> str:
    if "@" in address:
        return address.split("@")[-1].strip(">").lower()
    return ""


def analyze(msg) -> list[str]:
    findings = []

    from_addr = msg.get("From", "")
    return_path = msg.get("Return-Path", "")
    reply_to = msg.get("Reply-To", "")
    auth_results = msg.get("Authentication-Results", "")
    received_spf = msg.get("Received-SPF", "")

    from_domain = get_domain(from_addr)
    return_path_domain = get_domain(return_path)
    reply_to_domain = get_domain(reply_to)

    print(f"From:            {from_addr}")
    print(f"Return-Path:     {return_path}")
    print(f"Reply-To:        {reply_to}")
    print(f"Authentication-Results: {auth_results or '(not present)'}")
    print(f"Received-SPF:    {received_spf or '(not present)'}")
    print()

    # 1. Return-Path domain mismatch
    if return_path_domain and from_domain and return_path_domain != from_domain:
        findings.append(
            f"Return-Path domain ({return_path_domain}) does not match "
            f"From domain ({from_domain}) — possible spoofing."
        )

    # 2. Reply-To domain mismatch (common in BEC/phishing)
    if reply_to_domain and from_domain and reply_to_domain != from_domain:
        findings.append(
            f"Reply-To domain ({reply_to_domain}) differs from From domain "
            f"({from_domain}) — replies would go somewhere unexpected."
        )

    # 3. SPF / DKIM / DMARC results
    auth_lower = auth_results.lower()
    for mechanism in ("spf", "dkim", "dmarc"):
        if mechanism in auth_lower and f"{mechanism}=fail" in auth_lower:
            findings.append(f"{mechanism.upper()} check FAILED — sender may not be authorized for this domain.")
        elif mechanism not in auth_lower:
            findings.append(f"No {mechanism.upper()} result found in Authentication-Results header.")

    if not findings:
        findings.append("No obvious header-level red flags detected (still review the body/links manually).")

    return findings


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 analyze_headers.py path/to/email.eml")
        sys.exit(1)

    path = sys.argv[1]
    try:
        with open(path, "rb") as f:
            msg = BytesParser(policy=policy.default).parse(f)
    except FileNotFoundError:
        print(f"File not found: {path}")
        sys.exit(1)

    print(f"Analyzing headers of: {path}\n")
    findings = analyze(msg)

    print("Findings:")
    for i, finding in enumerate(findings, 1):
        print(f"  {i}. {finding}")


if __name__ == "__main__":
    main()
