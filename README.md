# CITS5505-project
Yi Zhou &amp; Zekun Shi's web project
## Getting Started

Activate the python virtual environment:
`$source venv/Scripts/activate`

To run the app:
`$python manager.py runserver`

To stop the app:
`$^C`

To exit the environment:
`$deactivate`

### Prerequisites

Requires python3, flask, venv, and sqlite

```
Give examples
```

### Installing

Install python3, sqlite3

1. Set up a virtual environment:
 - use pip or another package manager to install virtualenv package `pip install virtualenv`
 - start the provided virtual environment
   `source virtual-environment/bin/activate`
	`pip install -r requirements.txt`
 - This should include flask and all the required packages
2. Install sqlite
 - [Windows instructions](http://www.sqlitetutorial.net/download-install-sqlite/)
 - In \*nix, `sudo apt-get install sqlite`
3. one test db is already in the project folder

This should start the app running on localhost at port 5000, i.e. [http://localhost:5000](http://localhost:5000)


## User api 

an api for user managerment
/user/<string:username>
get:get userinformation
post:sign in user
delete:delete user
put:update user information

## Running the unit tests for user-api

python -m unittest discover

### tests

test_login
	pass this test if status_code is 200 and get right access token

test_login_failed
	pass this test if status_code is 401 and get the right warning message 

test_user_create
	pass this test if status_code is 200 and check the user is existed 

test_user_get
	pass if get the right user information

test_user_get_not_exist
	pass if status_code is 404 and return right error message

test_user_delete
	pass if the status_code is 200, and return right message

test_user_delete_not_exist
	pass if deleted user not exist
	


## Built With

jetbrain pycharm and git

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning
version 0.1
version 0.2
version 0.3
version 0.4
version 0.5
version 0.6
version 0.7
version 0.8
version Api-test (for api test only)
## Authors

* **Yi Zhou** - *Initial work* - [drtnf](https://github.com/gityizhou)
* **Zekun Shi** - *Initial work* - [drtnf](https://github.com/akamic)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Built following the [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) by **Miguel Grinberg**.
