# Setup Instructions

## 1. No special installation needed
`scripts/analyze_headers.py` only uses Python's standard library — no
external packages required.

## 2. Try the analyzer on the included sample
```bash
cd scripts
python3 analyze_headers.py ../samples/test-suspicious-email.eml
```

## 3. Analyze a real suspicious email (optional, your own inbox only)
Most email clients let you export/download a message as a `.eml` file:
- **Gmail:** Open the email → three-dot menu → "Download message"
- **Outlook:** Open the email → File → Save As → choose `.eml`

Then run:
```bash
python3 analyze_headers.py path/to/downloaded-email.eml
```

> Only analyze emails sent to you personally. Do not forward or share other
> people's email content without permission.

## 4. Read the sample write-ups
See `samples/example-1-urgency.md`, `example-2-authority.md`, and
`example-3-reward.md` for annotated breakdowns of common phishing patterns,
which you can use as a template to analyze your own real-world example.
