import requests

link = r'https://felipemonsef.pythonanywhere.com/webhook'

json = {
  "event": "message",
  "from": "5511988888888",
  "message": "Teste"
}

response = requests.post(link, json=json)
print(response.status_code)
print(response.text)