# Password-Policy-Audit
Here is a comprehensive, professional `README.md` file designed specifically for your **Password Policy Audit & Kali Linux Implementation** project repository on GitHub. You can copy and paste this directly into your repository's `README.md` file.

```markdown
# Password Policy Audit & Enterprise Implementation Plan

## 📌 Project Overview
Traditional enterprise password rules—such as 8-character minimums, mandatory complex symbols, forced 30-day rotations, and blocking paste functionality—often backfire. They lead to predictable user patterns (e.g., `Spring2026!`), password reuse across critical systems, and sticky-note storage.

This project, completed as part of the **InternCircle Cybersecurity Internship (Project 02)**[cite: 1], audits a legacy enterprise password policy against modern **NIST SP 800-63B** digital identity guidelines[cite: 1, 2]. It delivers a restructured, human-centric policy, a one-page employee reference guide, and hands-on technical verification executed in a **Kali Linux** environment[cite: 1, 2].

## 📂 Repository Directory Structure
```text
password-policy-audit-project/
├── README.md                            # Main project overview and documentation
├── docs/
│   ├── password_policy_audit_report.pdf # Complete printable PDF report (Audit + Kali Steps + Staff Guide)
│   ├── rewritten_policy.md              # Plain-language enterprise password policy text
│   └── staff_one_page_guide.md          # One-page quick reference guide for employees
└── scripts/
    └── hibp_audit.py                    # Python k-Anonymity breach verification script

```

## 🚀 Key Deliverables & Features

1. **Legacy Audit Matrix:** Evaluated old rules against NIST SP 800-63B standards, detailing security risks and justifications for keeping, changing, or removing each rule.


2. **Rewritten Enterprise Policy:** Implemented a practical, 6-rule policy enforcing 12+ character passphrases, mandatory password managers (Bitwarden), Multi-Factor Authentication (MFA/2FA), and eliminating arbitrary periodic expirations.


3. **Kali Linux Technical Lab:**
* Configured PAM security hardening (`/etc/security/pwquality.conf`).

* Demonstrated weak hash cracking vulnerabilities using `John the Ripper`.

* Built an automated Python script leveraging the **Have I Been Pwned (HIBP) k-Anonymity API** to check credential exposure without transmitting plaintext passwords or full hashes.

4. **Staff Quick-Reference Guide:** Created a concise, 3-step guide designed to make secure behavior the easiest path for non-technical employees.

## 🛠️ Tools & Technologies Used

* **Operating System:** Kali Linux

* **Standards & Frameworks:** NIST SP 800-63B (Digital Identity Guidelines)

* **Security Tools:** `John the Ripper`, PAM (`pam_pwquality`), `chage`

* **Languages & Libraries:** Python 3 (`hashlib`, `requests`, `sys`)

* **Password Management:** Bitwarden

## ⚙️ Quick Start: Running the HIBP Breach Audit Script

To run the automated breach verification script safely in your Kali Linux terminal:

1. **Clone the repository:**
```bash
git clone [https://github.com/YOUR_USERNAME/password-policy-audit-project.git](https://github.com/YOUR_USERNAME/password-policy-audit-project.git)
cd password-policy-audit-project

2. **Install required dependencies:**
```bash
pip3 install requests --break-system-packages

3. **Execute the Python script:**
```bash
python3 scripts/hibp_audit.py

## 📄 Documentation Access

The full formal report, including detailed tables, Kali Linux commands, and staff guides, is compiled in **`docs/password_policy_audit_report.pdf`**. Individual markdown texts are also available in the `docs/` folder for review.

## 🙏 Acknowledgments

Thanks to **InternCircle** for providing practical cybersecurity tasks and guidance.
