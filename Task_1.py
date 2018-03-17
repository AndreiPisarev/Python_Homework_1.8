import requests

response = requests.get('https://netology.ru')
print(response.content)
