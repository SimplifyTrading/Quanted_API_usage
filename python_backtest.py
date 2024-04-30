import requests


url = "https://api.simplifytrading.ai/backtest"
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer <YOUR API KEY>'
}

json = {
    "ModelName": "<AI MODEL NAME>",
    "TradeType": "LONG",
    "EntryTime": "07/06/2023 10:00:00 +00:00"
}
response = requests.post(url, json=json, headers=headers)

print(response.json())
