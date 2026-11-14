import hashlib
import requests
import sys

def check_pwned_password(password: str) -> int:
    """
    Checks if a password appears in known public data breaches using the
    Have I Been Pwned k-Anonymity API without transmitting the plaintext
    password or full hash over the network.
    """
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    response = requests.get(url, timeout=10)
    if response.status_code != 200:
        raise RuntimeError(f"Error fetching data from HIBP API: HTTP {response.status_code}")

    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return int(count)
    return 0

if __name__ == "__main__":
    # Sample test credential (never enter real production passwords)
    sample_password = sys.argv[1] if len(sys.argv) > 1 else "Winter2026!Secure#"
    print("[*] Auditing sample credential against Have I Been Pwned (k-Anonymity API)...")
    try:
        breach_count = check_pwned_password(sample_password)
        if breach_count > 0:
            print(f"[!] VULNERABLE: Credential appeared {breach_count:,} times in known data breaches.")
        else:
            print("[+] SAFE: Credential not found in any known public data breaches.")
    except Exception as exc:
        print(f"[!] Audit failed: {exc}")
