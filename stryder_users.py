!#/usr/bin/env python
# Filename: stryder_users.py
import requests

class User:
	headers = {'Authorization': 'Token token="fb0255bd9c1640914181e2a1aff1d42e"', 'content-type':'application/json'}

	def create(self):
		'''
		Create user  
		'''
		url = "https://handshake-staging.herokuapp.com/api/v1/users"

		user = {'email_address':'pjmiddle@mtu.edu', 'username':'pjmiddle', 'first_name':'Philip', 'last_name':'Middleton'}
		user = json.dumps({'user':user})

		r = requests.post(url, data=user, headers=headers)
		print r.text
		return self

	def delete(self):
		'''
		Delete User
		URL: https://handshake-staging.herokuapp.com/api/vi/users/delete
		'''
		url = "https://handshake-staging.herokuapp.com/api/vi/users/delete"
		user = {'email_address':'pjmiddle@mtu.edu', 'username':'pjmiddle', 'first_name':'Philip', 'last_name':'Middleton'}
		user = json.dumps({'user':user})

		r = requests.post(url, data=user, headers=headers)
		print r.text

		return self