

from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
import requests

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"


input(f"{GREEN}Stumbling through the forums you come across a post by Wil - a server admin, upon inspecting his profile, you are greeted by this note.")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print(f"CONTINUING.")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print(f"___________________________________________________________________________________________{RESET}")

targeturl = "http://localhost:4942/profile/k1asdfeditojrb4"

response = requests.get(
        targeturl,
        allow_redirects=False
    )

soup = BeautifulSoup(response.text, "html.parser")

cell = soup.find("div", class_="card-title", string="🔒 Private note")

if cell:
    card = cell.parent
    print(card.get_text(separator="\n", strip=True))
else:
    print("ohno")
