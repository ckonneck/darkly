import sys
import requests
 
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
 
# step 2 - upload file
# only pass the bare filename, no path - slashes cause 500
filepath = "../sw.js"
filename = filepath.split("/")[-1]  # strips any path, just keeps filename
 
with open(filepath, "rb") as f:
    response = requests.post(
        "http://localhost:4942/upload/avatar",
        files={"file": (filename, f, "text/javascript")},
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
print("Body:", response.text[:500])
 