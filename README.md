# CITS5505-project
Yi Zhou &amp; Zekun Shi's web project

## Introduction

This Web application is designed for voting best anime that are listed by authors. We use first past the post voting as the social choice mechanism. Users can register an account and then participate in voting. Also users can view results of voting in results page. If user is just a visitor, he/she can also view results but cannot take part in voting activity.
Our web mainly includes 6 pages. You can access Home page, vote page, result page and login page via nevigation bar on the top of the website. (Attention: you cannot access vote page if you have not signed in.)  
Home page shows the introduction of our website. You can enter login or vote page by clicking pics or corresponding words in Home page. Login page is used for signing in and if you are new to this website. You can sign up through clicking "new user" in login page. Once signing in, you can view vote page and choose the best anime you like listed in the page. You can also see the introduction of the anime on Wiki via clicking the pics. Once you finish voting, the web will jump thankyou page automatically and you can click view result button to view the vote results there. (you can also view the page through nevigation bar).

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

## Architecture
manager.py: runserver

models.py: all the db models in it

unit_test:

 test_login.py: unittest for userlogin api

 test_user.py: unittest for user api

forms.py: the form model of our application

route.py: basic model of our application(login, logout, register etc.)

user_api.py: user api model

config.py: config document

__init__.py: basic app route , module import etc.

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

## Reference

En.wikipedia.org. (2019). One Piece. [online] Available at: https://en.wikipedia.org/wiki/One_Piece [Accessed 20 May 2019].

En.wikipedia.org. (2019). Naruto. [online] Available at: https://en.wikipedia.org/wiki/Naruto [Accessed 20 May 2019].

En.wikipedia.org. (2019). Bleach. [online] Available at: https://en.wikipedia.org/wiki/Bleach [Accessed 20 May 2019].

En.wikipedia.org. (2019). Fairytail. [online] Available at: https://en.wikipedia.org/wiki/Fairytail [Accessed 20 May 2019].

En.wikipedia.org. (2019). Fullmetal. [online] Available at: https://en.wikipedia.org/wiki/Fullmetal [Accessed 20 May 2019].

Download Awesome collection of handpicked wallpapers and images. (2019). one piece 1080p windows 1440x900. [online] Available at: https://www.tokkoro.com/1507503-one-piece.html [Accessed 20 May 2019].
