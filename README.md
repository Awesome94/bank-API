## Bank-API

Bank RestFul APIs built with Flask and Python.

-   API public documentation can be found here. https://bit.ly/2CrOv0K
-   Live API can be found here. https://bit.ly/2CC9wpz.
-   Trello Board. https://bit.ly/2MgIKT9

## Overview
This is a simple RestApi for performing basic bank tasks such as:

-   Register and get account number.
-   Deposit and withdraw
-   check account balance     

HTTP |End Point  | Result
--- | --- | ----------
GET | `/v1/register` | Registers a new user and assigns them an account.
POST | `/v1/login` | Logs in registered user and returns a token.
GET | `/v1/users` | Returns all users.
GET | `/v1/users/<user_id>` | Returns a particular user matching the given User ID.
PUT | `/v1/users/<user_id>` | Updates profile for a particular user.
DELETE | `/v1/users/<user_id>` | Deletes profile for a particular user.
GET | `/v1/accounts` | Returns all accounts.
GET | `/v1/accounts/<accounts_id>` | Returns a particular account matching the given User ID.
PUT | `/v1/accounts/deposit/<accounts_id>` | Deposit funds on a particular user.(Admin/Teller)
PUT | `/v1/accounts/withdraw/<accounts_id>` | withdraw funds on a particular user.
PUT | `/v1/accounts/transfer/<accounts_id>` | Transfer funds between accounts.
DELETE | `/v1/accounts/<accounts_id>` | Deletes an account.

## Installation

 ## Requirements:

* Python 3.6
* pip
* virtualenv
* postgresql

## Run application on Local
1. clone repo. `$ git clone https://github.com/Awesome94/bank-API.git`

    `cd bankapp/`

2. Create and activate a virtual environment and install requirements:

    - `$ mkvirtualenv <name_of_your_choice>`

    - `$ pip install -r requirements.txt.`

3. create a local database and run migrations:
    - `$ createdb bankapi`
        - `flask db init`
        - `flask db migrate`
        - `flask db upgrade`


    NB: Make sure you have FLASK_APP set as `app/__init__.py`.


4. Start your application



    $ python run run.py
     * Running on http://127.0.0.1:5000/
     * Restarting with reloader

You can now open the API with Curl from the command line:
or Postman.

    $ using Curl

    $ curl -X GET http://127.0.0.1:5000/v1/
    [{"url": "http://127.0.0.1:5000/v1/", "text": "start banking"}

You can also work on the API directly in your browser, by opening <http://127.0.0.1:5000/>.  You can then navigate between notes, and make `GET`, `PUT`, `POST` and `DELETE` API requests.
