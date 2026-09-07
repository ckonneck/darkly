import sys
import requests


GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

#login and get session cookie

identity = "admin@42network.local"
password = "Darkly42Admin!"
auth = requests.post(
    "http://localhost:8090/api/admins/auth-with-password",
    data={"identity": identity, "password": password},
    allow_redirects=False
)
 
try:
    auth_data = auth.json()
    token = auth_data["token"]
except (ValueError, KeyError):
    print(f"{RED}[-] Login response did not contain a token{RESET}")
    print(auth.text[:200])
    sys.exit(1)
 
print(f"{GREEN}Logged in successfully with " + identity + " and " + password )

print(f"{RESET}__________")
print(f"{CYAN}accessing 'internal audit records'{RESET}")
targeturl = "http://localhost:8090/api/collections/internal_audit/records"

response = requests.get(
        targeturl,
        headers={
            "Authorization": f"Bearer {token}",
            "Origin": "http://localhost:8090/api/collections/internal_audit/records",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
        },
        allow_redirects=False
    )
print("__________")
print("response of GET api/collections/internal_audit/records:\n")
print(response.text)
print(response.status_code)
print("__________")


print("___________") 
keyword = "note"
index = response.text.find(keyword)

# Check if found to avoid slicing from -1
if index != -1:
    result = response.text[index:]
    print(f"{GREEN}"+ result)
else:
    print("")