## Bank-API

Bank RestFul APIs built with Flask and Python.

## Overview
This is a simple RestApi for performing basic bank tasks such as:
    - Register and get account number.
    - Deposit and withdraw
    - check account balance     

## Installation

 ## Requirements:

* Python 3.6
* pip
* virtualenv
* postgresql

## Run application on Local
1. $ git clone ``
Install using `pip`:

    cd bankapp

2. Create and activate a virtual environment and install requirements:

    mkvirtualenv <name_of_your_choice>

    pip install -r requirements.txt.

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

You can also work on the API directly in your browser, by opening <http://127.0.0.1:5000/v1/>.  You can then navigate between notes, and make `GET`, `PUT`, `POST` and `DELETE` API requests.
