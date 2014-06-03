import csv
import requests
import json

headers = {'Authorization': 'Token token="35ead9076bdb1cef11a5ddef669d7f3b', 'content-type': 'application/json'}
batch_url = "http://localhost:3000/api/v1/batch"
start_sync_url = "http://localhost:3000/api/v1/users/start_sync"
create_or_update_url = "http://localhost:3000/api/v1/users/create_or_update"
sync_details_url = "http://localhost:3000/api/v1/users/sync_details"
abort_sync_url = "http://localhost:3000/api/v1/users/abort_sync"
end_sync_url = "http://localhost:3000/api/v1/users/end_sync"

with open('handshake-users.csv', 'rb') as csvfile:
    data = csv.reader(csvfile, delimiter=',', quotechar="\"")

    # abort a sync if it already is started
    r = requests.post(abort_sync_url, data="{}", headers=headers)

    # start the sync
    r = requests.post(start_sync_url, data="{}", headers=headers)
    print "Start sync:"
    print r.text

    # print the initial details
    r = requests.post(sync_details_url, data="{}", headers=headers)
    print "Pre sync:"
    print r.text

    # Create or update users
    ops = []
    for row in data:
        user = { 'email_address': row[0], 'username' : row[1], 
                'first_name' : row[2], 'last_name': row[3] }
        ops.append({'method': 'post', 'url': create_or_update_url, 'params': {'user': user}})
    params = json.dumps({'ops': ops, 'sequential': True})

    # for some reason this returns with not found for the batch requests.
    # not sure why this is
    r = requests.post(batch_url, data=params, headers=headers)
    
    # Create or update all users results
    print r.text

    # print the initial details
    r = requests.post(sync_details_url, data="{}", headers=headers)
    print "Post sync:"
    print r.text
