from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
import requests
import base64
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"


input(f"{GREEN}Stumbling through the forums you come across a post by Wil - a server admin: ")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print(f"CONTINUING.")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print(f"___________________________________________________________________________________________{RESET}")

targeturl = "http://localhost:4942/forum/bbeo32ucx0a65b8"

response = requests.get(
        targeturl,
        allow_redirects=False
    )

soup = BeautifulSoup(response.text, "html.parser")

cell = soup.find("div", class_="post-content")

if cell:
    card = cell.parent
    print(card.get_text(separator="\n", strip=True))
else:
    print("ohno")

input(f"{GREEN}Decoding the 'Networks ops ref for the team' via md5: ")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print(f"CONTINUING.")
print("___________________________________________________________________________________________")
print("___________________________________________________________________________________________")
print(f"___________________________________________________________________________________________{RESET}")


encoded_data = "dmFsaWRhdGlvbl9rZXk9NDJuZXR3b3Jr"

# Decode to bytes
decoded_bytes = base64.b64decode(encoded_data)

# Convert bytes to string
decoded_string = decoded_bytes.decode('utf-8')

print(decoded_string)