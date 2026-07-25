# Mini Project 1: Understanding Phishing Emails & Social Engineering

## 📌 Overview
This project builds awareness of how **phishing emails** are structured and
the social engineering techniques attackers use to trick recipients into
clicking malicious links, downloading attachments, or handing over
credentials. The focus is entirely defensive: recognizing red flags in
real-world-style phishing attempts so they can be spotted and reported.

> ⚠️ **Disclaimer:** This project is for educational awareness only. All
> sample emails in `samples/` are fictional, generic mock-ups — they do not
> impersonate any real company, brand, or individual, and contain no
> functional links or attachments. This project does not create or send
> phishing emails to anyone.

## 🎯 Objectives
- Understand the anatomy of a phishing email
- Learn common social engineering techniques (urgency, authority,
  fear, curiosity, reward)
- Identify technical red flags (spoofed sender domains, mismatched
  links, suspicious attachments)
- Practice analyzing email headers for signs of spoofing
- Learn what to do when a phishing email is received

## 🧠 Anatomy of a Phishing Email

| Element | What Attackers Do | Red Flag to Look For |
|---------|--------------------|------------------------|
| **Sender address** | Spoof or use a lookalike domain (e.g., `support@paypa1.com`) | Domain doesn't match the real company; extra characters, typos |
| **Subject line** | Create urgency ("Account Suspended", "Action Required") | Excessive urgency, ALL CAPS, threats |
| **Greeting** | Generic ("Dear Customer") instead of your actual name | Legit companies usually personalize |
| **Body** | Impersonate a trusted brand, request "verification" | Requests for passwords, OTPs, payment details |
| **Links** | Display text shows a real URL, but the actual `href` points elsewhere | Hover over the link — check the real destination before clicking |
| **Attachments** | Disguised as invoices, resumes, "important documents" | Unexpected attachments, especially `.exe`, `.zip`, macro-enabled `.docm` |
| **Tone** | Authority + urgency + consequence ("your account will be closed in 24 hours") | Pressure to act immediately without verification |

## 🔍 Social Engineering Techniques Covered
1. **Urgency/Scarcity** — "Your account will be locked in 24 hours"
2. **Authority** — Impersonating IT department, bank, or a CEO ("CEO fraud")
3. **Fear** — "Suspicious activity detected on your account"
4. **Curiosity/Reward** — "You've won a prize, claim it now"
5. **Trust exploitation** — Spoofing a colleague or known vendor

## 📁 Sample Analysis
See `samples/` for annotated example phishing emails (fictional, generic)
showing each of the above patterns with red flags called out.

## 🔬 Header Analysis
Real phishing detection often involves inspecting **email headers**
(`Return-Path`, `Received`, `SPF`, `DKIM`, `DMARC` results) to check whether
the sending server was actually authorized to send on behalf of the claimed
domain. See `scripts/analyze_headers.py` for a simple header-analysis helper.

## ✅ What To Do If You Receive a Phishing Email
1. **Don't click** any links or open attachments.
2. **Verify independently** — contact the organization via their official
   website/phone number, not the info in the email.
3. **Report it** — most email clients have a "Report Phishing" button;
   forward to your organization's security team if applicable.
4. **Delete** after reporting.
5. If you already clicked a link or entered credentials, **change your
   password immediately** and enable MFA.

## 📁 Repository Structure
```
mini-project-1-phishing/
├── README.md
├── samples/
│   ├── example-1-urgency.md
│   ├── example-2-authority.md
│   └── example-3-reward.md
├── scripts/
│   └── analyze_headers.py
└── screenshots/
    └── (annotated screenshots, if any)
```

## 📚 References
- [OWASP Phishing Overview](https://owasp.org/www-community/attacks/Phishing)
- [Anti-Phishing Working Group (APWG)](https://apwg.org/)
- [CISA — Avoiding Social Engineering and Phishing Attacks](https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks)

---
*Submitted as part of Mini Project 1 — CipherSchools Cybersecurity Track*
