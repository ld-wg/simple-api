from flask import jsonify
from app.state import accounts

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
    return jsonify({"origin": {"id":origin, "balance": accounts[origin]}}), 201

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
