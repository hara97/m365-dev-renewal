import requests

token = "<PASTE_YOUR_BEARER_TOKEN_HERE>"

resp = requests.get(
    "https://graph.microsoft.com/v1.0/users",
    headers={"Authorization": f"Bearer {token}"}
)

print("Status:", resp.status_code)
for user in resp.json().get("value", [])[:3]:
    print(user["displayName"], "-", user["mail"])
