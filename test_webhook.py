import requests


user_message = "who are you ?"

request_message = {"message": user_message}

# url = "http://localhost:5678/webhook-test/9c64073a-6fba-45d8-9443-399ba9b980d1" # for testing
url = "http://localhost:5678/webhook/9c64073a-6fba-45d8-9443-399ba9b980d1" # for production

response = requests.post(url, json=request_message)

print(response.status_code)

print("----------------------------------------------------------------")

print(response.json()[0].get("output"))