from flask import Flask, jsonify, request
from app.services.event import handle_deposit, handle_withdraw, handle_transfer
from app.services.balance import get_balance
from app.services.reset import reset_server

def set_routes(app: Flask):
    @app.route('/')
    def home():
        return 'root'

    @app.route("/reset", methods=["POST"])
    def reset_state():
        return reset_server()
    
    @app.route('/balance', methods=['GET'])
    def balance():
        return get_balance()
    
    @app.route('/event', methods=['POST'])
    def handle_event():
        data = request.get_json()
        event_type = data.get('type')
        
        if event_type == 'deposit':
            return handle_deposit(data)
        if event_type == 'withdraw':
            return handle_withdraw(data)
        if event_type == 'transfer':
            return handle_transfer(data)
        else:
            return jsonify({'error': 'Invalid event type'}), 400
