import requests

res = requests.get('https://api.github.com/users/estevammr')
data = res.json()
print(data)
