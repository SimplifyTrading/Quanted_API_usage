import requests


url = "http://api.simplifytrading.ai/predict"
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer <YOUR API KEY>'
}

json = {
    "ModelName": "<AI MODEL NAME>",
    "TradeType": "LONG"
}
response = requests.post(url, json=json, headers=headers)

print(response.json())
