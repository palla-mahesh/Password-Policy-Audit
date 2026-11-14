# Password Policy Audit & Kali Linux Implementation

## Overview
This project audits a legacy enterprise password policy against modern **NIST SP 800-63B** digital identity guidelines and provides a practical, user-friendly policy, a one-page staff reference guide, and hands-on technical verification scripts executed in **Kali Linux**.

## Repository Structure
```text
password-policy-audit-project/
├── README.md                            # Main project overview and documentation
├── docs/
│   ├── password_policy_audit_report.pdf # Complete PDF report (Audit + Kali Steps + Staff Guide)
│   ├── rewritten_policy.md              # Plain-language enterprise password policy text
│   └── staff_one_page_guide.md          # One-page quick reference guide for employees
└── scripts/
    └── hibp_audit.py                    # Python k-Anonymity breach verification script
```

## Key Highlights
- **Legacy Audit:** Identified weaknesses in 8-character limits, mandatory symbol rules, 30-day forced expiration, space restrictions, and paste blocking.
- **Modern Policy:** Enforces 12+ character passphrases, prohibits password reuse, mandates a company password manager (Bitwarden), enforces Multi-Factor Authentication (MFA/2FA), and eliminates arbitrary password expiration.
- **Kali Linux Lab:** Includes PAM (`pam_pwquality`) hardening, `John the Ripper` cracking demonstrations, and automated Have I Been Pwned (HIBP) k-Anonymity API verification.

## Quick Start (Running the HIBP Audit Script)
```bash
pip3 install requests --break-system-packages
python3 scripts/hibp_audit.py
```
