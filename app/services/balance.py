from flask import jsonify, request
from app.state import accounts


def get_balance():
    account_id = request.args.get("account_id")
    if account_id is None:
        return jsonify({"error": "Account ID is required"}), 400

    balance = accounts.get(account_id)

    if balance is None:
        return jsonify(0), 404

    return jsonify(balance), 200
