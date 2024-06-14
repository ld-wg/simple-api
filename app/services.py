from flask import request, jsonify

users = {}

accounts = {
    '1001': 500,
    '1002': 1500
}

def fetch_user_data(user_id):
    user_data = users.get(user_id, {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    })
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    return jsonify(user_data), 200

def create_user_data():
    data = request.get_json()
    users[data.get("user_id")] = data
    return jsonify(data), 201

def reset_user_data():
    global users
    users = {}
    return '', 200

def get_balance():
    account_id = request.args.get('account_id')
    if account_id is None:
        return jsonify({'error': 'Account ID is required'}), 400

    balance = get_account_balance(account_id)
    if balance is None:
        return jsonify(0), 404
    return jsonify(balance), 200

def get_account_balance(account_id):
    return accounts.get(account_id)