#!/usr/bin/env python
# Filename: handshake.py
import requests
import json


class Handshake(object):
	'''
	Initalize the Handshake class with the api key
	hs = Handshake("api_key")
	'''
	#Variables
	__base_url = "https://handshake-staging.herokuapp.com/api/v1/"
	token = None

	def __init__(self, token):
		self.token = token

	
	def __post_function(self, url, data, headers):
		r = requests.post(url, data=data, headers=headers)
		return r


	def __delete_function(self, url, data, headers):
		r = requests.delete(url, data=data, headers=headers)
		return r


	def __update_function(self, url, data, headers):
		r = requests.put(url, data=data, headers=headers)
		return r


	def __get_users_function(self, url, data, headers):
		r = requests.get(url, headers=headers)
		return r


	def __communicate(self, url, data, action):
		'''
		Takes the ending of the url and the data to be passed to the server
		Appends the function url to the base API url
		'''
		base_token = 'Token token=' + '\"' + self.token + '\"'
		access_url = self.__base_url + url
		headers = {'Authorization': base_token, 'content-type': 'application/json'}

		token_dictionary = {
			'create' : self.__post_function,
			'delete' : self.__delete_function,
			'update' : self.__update_function,
			'get_users' : self.__get_users_function,
		}

		function_to_call = token_dictionary[action]
		r = function_to_call(access_url, data, headers)
		return r.text


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


	def get_users(self):
		'''
		Gets a user or multiple users
		URL: users
		Gets multiple users by default
		'''
		url = "users"
		action = "get_users"
		data = None
		results = self.__communicate(url, data, action)
		return results


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


	def delete_user(self, email, username, first_name, last_name):
		'''
		Deletes a specified user
		URL: users/delete
		'''
		url = "users/delete"
		action = "delete"
		data = self.data(email, username, first_name, last_name)
		results = self.__communicate(url, data, action)
		return results


	def update_user(self, email, username, first_name, last_name):
		'''
		Updates a Specified user
		URL: users/update
		'''
		url = "users/update"
		action = "update"
		data = self.data(email, username, first_name, last_name)
		results = self.__communicate(url, data, action)
		return results

