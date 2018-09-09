data = {
    "Bankapl v1": "Welcome to the Bankapl /v1 general api schema",
    "$schema": "http://json-schema.org/draft-04/hyper-schema#",
    "properties": {
        "register": {
            "$ref": "/v1/register/"
        },
        "login": {
            "$ref": "/v1/login"
        },
        "logout": {
            "$ref": "/v1/logout"
        },
        "users": {
            "$ref": "/v1/users/"
        },
        "user": {
            "$ref": "/v1/users/<id>"
        },
        "accounts": {
            "$ref": "/v1/accounts/"
        },
        "account": {
            "$ref": "/v1/accounts/<id>"
        },
        "balance": {
            "$ref": "/v1/account/balance/<id>"
        },
        "deposit": {
            "$ref": "/v1/account/deposit/<id>"
        },
        "withdraw": {
            "$ref": "/v1/account/withdraw"
        },
        "Transfer": {
            "$ref": "/v1/account/transfer/<id>#"
        },
        "events": {
            "$ref": "/v1/events/"
        },
    }
}
