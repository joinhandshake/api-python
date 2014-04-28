#!/usr/bin/env python
# Filename: stryder_users.py
import requests
import json

#Global Variables
#api_access_key = "Token token=\"fb0255bd9c1640914181e2a1aff1d42e"

class Handshake(object):
	#Variables
	base_url = "https://handshake-staging.herokuapp.com/api/v1/"

	def __communicate(self, url, data, action):
		'''
		Takes the ending of the url and the data to be passed to the server
		Appends the function url to the base API url
		'''
		access_url = self.base_url + url
		data = self.__data()
		headers = {'Authorization': 'Token token="fb0255bd9c1640914181e2a1aff1d42e"', 'content-type': 'application/json'}

		if(action == "create"):
			r = requests.post(access_url, data=data, headers=headers)
		elif(action == "delete"):
			r = requests.delete(access_url, data=data, headers=headers)
		return r

	def __data(self):
		'''
		Stuff
		'''
		return json.dumps({
			'user': {
				'email_address':'amsilski@mtu.edu', 
				'username':'amsilski', 
				'first_name':'Ann', 
				'last_name':'Silski',
				}
			})


	def create(self):
		'''
		Creates a user
		URL: users
		'''
		url = "users"
		action = "create"
		results = self.__communicate(url, {}, action)

		return results

	def delete(self):
		'''
		Deletes a specified user
		URL: users/delete
		'''
		url = "users/delete"
		action = "delete"
		results = self.__communicate(url, {}, action)
		return results


