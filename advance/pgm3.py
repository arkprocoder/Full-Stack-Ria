import requests
api=requests.get("https://api.github.com/users")
print(api)
# print(api.content)
# print(api.headers)
print(api.json())
