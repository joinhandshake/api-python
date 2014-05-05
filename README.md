Handshake Python Wrapper
=======================

This python wrapper can be used to easily make calls to the Handshake api and perform the following Tasks:
	
	Users
		Get Users
		Create Users
		Delete Users
		Update Users
	
	Reports
		Add Content
		Add Content
		Add Content
		Add Content

Installation
============
To install the handshake python package please perform the following tasks:

Download the handshake zip or clone this repo from GitHub

You can then continue to running the *setup.py* file

	$ cd ~/path_to_download/handshake
	$ python setup.py install

Usage
=====

Using this wrapper is very simplistic and requires only a few lines of code

	from handshake import Handshake

After importing the wrapper you need to initialize the Handshake class with your API key.

	hs = Handshake("insert_api_key_here")

Performing tasks after this point is as easy knowing what function to call.

*Get Users:*

	hs.get_users()

*Creating Users:*

	hs.create_user("user_email", "user_account_name", "First_Name", "Last_Name")

*Deleting Users:*
	
	hs.delete_user("user_email", "user_account_name")

*Updating Users:*

	hs.update_user("user_email", "user_account_name", "First_Name", "Last_Name")

Each of these functions return json data.

		
