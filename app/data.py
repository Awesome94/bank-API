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
            "$ref": "/v2/logout"
        },
        "users": {
            "$ref": "/v1/users/"
        },
        "user": {
            "$ref": "/v2/users/<id>"
        },
        "accounts": {
            "$ref": "/v2/accounts/"
        },
        "account": {
            "$ref": "/v2/accounts/<id>"
        },
        "balance": {
            "$ref": "/v2/account/balance/<id>"
        },
        "deposit": {
            "$ref": "/v2/account/deposit/<id>"
        },
        "withdraw": {
            "$ref": "/v2/account/withdraw"
        },
        "Transfer": {
            "$ref": "/v2/account/transfer/<id>#"
        },
        "events": {
            "$ref": "/v1/events/"
        },
    }
}
