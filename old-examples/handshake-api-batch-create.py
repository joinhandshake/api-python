import csv
import requests
import json

headers = {'Authorization': 'Token token="35ead9076bdb1cef11a5ddef669d7f3b', 'content-type': 'application/json'}
url = "http://localhost:3000/api/v1/batch"

with open('handshake-users.csv', 'rb') as csvfile:
    data = csv.reader(csvfile, delimiter=',', quotechar="\"")
    ops = []
    for row in data:
        user = { 'email_address': row[0], 'username' : row[1], 
                'first_name' : row[2], 'last_name': row[3] }
        # ops.append({'method': 'delete', 'url': '/api/v1/users/destroy.json', 'params': {'user': user}})
        ops.append({'method': 'post', 'url': '/api/v1/users', 'params': {'user': user}})
    params = json.dumps({'ops': ops, 'sequential': True})
    r = requests.post(url, data=params, headers=headers)
    print r.text
