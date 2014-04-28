#!/usr/bin/env python
# Filename: stryder_users.py
import requests
import json

#Global Variables
#Potentially api token here

class Handshake(object):
	#Variables
	base_url = "https://handshake-staging.herokuapp.com/api/v1/"

	def __communicate(self, url, data, action):
		'''
		Takes the ending of the url and the data to be passed to the server
		Appends the function url to the base API url
		'''
		access_url = self.base_url + url
		headers = {'Authorization': 'Token token="fb0255bd9c1640914181e2a1aff1d42e"', 'content-type': 'application/json'}

		if(action == "create"):
			r = requests.post(access_url, data=data, headers=headers)
		elif(action == "delete"):
			r = requests.delete(access_url, data=data, headers=headers)
		elif(action == "update"):
			r = requests.put(access_url, data=data, headers=headers)
		return r


	def data(self, email_address, username, first_name, last_name):
		'''
		Takes in the paramters that get passed to User classes
		'''
		return json.dumps({
			'user': {
				'email_address': email_address, 
				'username': username, 
				'first_name': first_name, 
				'last_name': last_name,
				}
			})


	def create_user(self, email, username, first_name, last_name):
		'''
		Creates a user
		URL: users
		'''
		url = "users"
		action = "create"
		data = self.data(email, username, first_name, last_name)
		results = self.__communicate(url, data, action)

		return results


	def delete_user(self):
		'''
		Deletes a specified user
		URL: users/delete
		'''
		url = "users/delete"
		action = "delete"
		data = self.data(email, username, first_name, last_name)
		results = self.__communicate(url, {}, action)
		return results


	def update_user(self):
		'''
		Updates a Specified user
		URL: users/update
		'''
		url = "users/update"
		action = "update"
		data = self.data(email, username, first_name, last_name)
		results = self.__communicate(url, {}, action)
		return results

