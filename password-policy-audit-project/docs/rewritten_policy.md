# Enterprise Password & Authentication Policy

**Effective Date:** November 2026  
**Standard Alignment:** NIST SP 800-63B (Digital Identity Guidelines)  

## Policy Rules

1. **Use a Passphrase of at Least 12 Characters (15+ Recommended)**  
   Length provides exponentially greater resistance against modern brute-force cracking than arbitrary character complexity. Spaces are permitted and encouraged to create memorable multi-word passphrases.

2. **Never Reuse Passwords Across Accounts**  
   Every work account, email, and third-party service must have a unique password so that a single external data breach cannot compromise company systems.

3. **Store All Credentials in the Approved Password Manager**  
   Employees must use the organization-approved password manager (e.g., Bitwarden) to generate, store, and autofill complex credentials. Copy-and-paste functionality is explicitly permitted across all login forms.

4. **Enable Two-Step Verification (MFA/2FA) Everywhere**  
   Multi-Factor Authentication (authenticator app or hardware security key) is mandatory for email, VPN, cloud infrastructure, banking, and administrative accounts.

5. **No Arbitrary Periodic Password Resets**  
   Passwords do not expire every 30 or 90 days. Forced periodic resets lead to predictable patterns (e.g., `Spring2026!`, `Summer2026!`) and sticky-note storage.

6. **Change Passwords Immediately Upon Suspected Compromise**  
   Passwords must be changed immediately if there is evidence of unauthorized access, phishing exposure, or appearance in a known breach database.

7. **Screen New Passwords Against Compromised Breach Lists**  
   All newly created or updated passwords are automatically checked against known breached credential databases (such as Have I Been Pwned) and dictionary blocklists prior to acceptance.
