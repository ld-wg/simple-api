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

    balance = accounts.get(account_id)

    if balance is None:
        return jsonify(0), 404
    
    return jsonify(balance), 200

def handle_deposit(data):
    destination = data.get('destination')
    amount = data.get('amount')
    
    if destination not in accounts:
        accounts[destination] = 0  # Create a new account if it doesn't exist
    
    accounts[destination] += amount  # Deposit the amount
    return jsonify({'destination': {'id': destination, 'balance': accounts[destination]}}), 201

def handle_withdraw(data):
    origin = data.get('origin')
    amount = data.get('amount')

    if origin not in accounts:
        return jsonify(0), 404
    
    accounts[origin] -= amount  # Withdraw the amount
    return jsonify({"origin": {"id":origin, "balance": accounts[origin]}})

def handle_transfer(data):
    origin = data.get('origin')
    if origin is None:
        return jsonify({'error': 'Origin account id is required'}), 400
    
    destination = data.get('destination')
    if destination is None:
        return jsonify({'error': 'Destination account id is required'}), 400
    
    amount = data.get('amount')
    if amount is None:
        return jsonify({'error': 'Amount is required'}), 400
    
    if accounts.get(origin) is None:
        return jsonify(0), 404
    
    if accounts.get(destination) is None:
        accounts[destination] = 0  # Create a new account if it doesn't exist
    
    accounts[destination] += amount
    accounts[origin] -= amount

    return jsonify({"origin": {"id":origin, "balance":accounts[origin]}, "destination": {"id":destination, "balance":accounts[destination]}}), 201


