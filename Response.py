import requests
response = requests.get("https://api.github.com/users/TuraevArtyom")
print(response.text)