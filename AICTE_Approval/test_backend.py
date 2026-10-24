

import requests

url = "http://127.0.0.1:5002/api/applications"

data = {
    "institution_name": "Demo Engineering College",
    "application_type": "New Institution"
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response:", response.text)
