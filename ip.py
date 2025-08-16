import requests

resp = requests.get("https://api.ipify.org")
print("当前出口 IP:", resp.text)
