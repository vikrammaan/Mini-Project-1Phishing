# Sample 2: Authority / "CEO Fraud" (Fictional Example)

> This is a fictional, generic mock-up for educational analysis only. It does
> not impersonate any real company or individual.

## The Email

```
From: J. Carter (CEO) <j.carter.office@corp-exec-mail.com>
To: finance-team@example.com
Subject: Quick task before my flight

Hi,

I'm heading into back-to-back meetings and about to board a flight, so I
can't call right now. I need you to process an urgent wire transfer to a
new vendor before end of day — I'll send the account details in a follow-up.
Please keep this between us for now as it's a confidential acquisition
matter. Let me know once it's done.

Thanks,
J. Carter
```

## Red Flags Identified

| # | Red Flag | Explanation |
|---|----------|-------------|
| 1 | Sender domain `corp-exec-mail.com` | Not the company's real domain — attackers often register lookalike domains |
| 2 | Unavailability excuse ("boarding a flight") | Prevents the target from calling to verify |
| 3 | Urgency ("before end of day") | Pressure to skip normal approval processes |
| 4 | Secrecy request ("keep this between us") | Isolates the target from colleagues who might spot the scam |
| 5 | Unusual request via email | Wire transfers/vendor payments should go through verified, established processes — not ad hoc email requests |
| 6 | Generic first name signature | Real executives at a company typically have a consistent, known email signature/style |

## Social Engineering Technique
**Authority + Urgency + Isolation** — impersonating a senior executive to
pressure a lower-level employee into bypassing normal controls, while asking
for secrecy to prevent verification.

## Correct Response
Never act on financial requests received only by email. Verify via a known,
independent channel (call the executive's known phone number, not one
provided in the email). Report to IT/security — this pattern is commonly
known as **Business Email Compromise (BEC)** or "CEO fraud."
