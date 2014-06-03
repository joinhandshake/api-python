import csv
import requests
import json

headers = {'Authorization': 'Token token="35ead9076bdb1cef11a5ddef669d7f3b', 'content-type': 'application/json'}
# url = "http://localhost:3000/api/v1/users/destroy.json"
url = "http://localhost:3000/api/v1/users.json"
#url = "https://app.joinhandshake.com/api/v1/users.json"

with open('handshake-users.csv', 'rb') as csvfile:
    data = csv.reader(csvfile, delimiter=',', quotechar="\"")
    for row in data:
        user = { 'email_address': row[0], 'username' : row[1], 
                'first_name' : row[2], 'last_name': row[3] }
        user = json.dumps({'user': user})
        r = requests.post(url, data=user, headers=headers)
        # r = requests.delete(url, data=user, headers=headers)
        print r.text
