#!/usr/bin/env python3

import getpass
import sys
import requests

BASE_URL = "http://localhost:8090"

EMAIL = "admin@42network.local"
PASSWORD = "Darkly42Admin!"

auth = requests.post(
    f"{BASE_URL}/api/admins/auth-with-password",
    json={
        "identity": EMAIL,
        "password": PASSWORD
    },
)

print("Auth status:", auth.status_code)

if not auth.ok:
    print(auth.text)
    sys.exit(1)

token = auth.json()["token"]

if len(sys.argv) < 3:
    print(f"Usage: {sys.argv[0]} GET|POST|PATCH /api/...")
    sys.exit(1)

method = sys.argv[1].upper()
endpoint = sys.argv[2]

response = requests.request(
    method,
    BASE_URL + endpoint,
    headers={
        "Authorization": token,
        "Accept": "application/json",
        "Content-Type": "application/json",
    },
)

print("Status:", response.status_code)
print(response.text)