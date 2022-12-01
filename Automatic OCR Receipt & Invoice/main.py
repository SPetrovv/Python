import requests
import pickle
import json

# url = "https://ocr.asprise.com/api/v1/receipt"
# image = "receipt2.png"
#
# res = requests.post(url,
#                     data={
#                         'api_key': "TEST",
#                         'recognizer': 'auto',
#                         'ref_no': 'oct_python_123'
#                     },
#                     files={
#                         'file': open(image, 'rb')
#                     })
#
#
# with open("response2.json", "w") as f:
#     json.dump(json.loads(res.text), f)

with open("response1.json", "r") as f:
    data = json.load(f)


# print(data['receipts'][0].keys())

items = data['receipts'][0]['items']


print(F"Your purchase at {data['receipts'][0]['merchant_name']}")

for item in items:
    print(F"{item['description']} - ${item['amount']}")


print('*' * 30)
print(F"Subtotal: {data['receipts'][0]['subtotal']}")
print(F"Tax: {data['receipts'][0]['tax']}")
print('*' * 30)
print(F"Total: {data['receipts'][0]['total']}")
