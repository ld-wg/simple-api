from flask import Flask
from .services import fetch_user_data, create_user_data, get_balance, reset_user_data

def set_routes(app: Flask):
    @app.route('/')
    def home():
        return 'Home'

    @app.route("/get-user/<user_id>")
    def get_user(user_id):
        return fetch_user_data(user_id)

    @app.route("/create-user", methods=["POST"])
    def create_user():
        return create_user_data()

    @app.route("/reset", methods=["POST"])
    def reset_state():
        return reset_user_data()
    
    @app.route('/balance', methods=['GET'])
    def balance():
        return get_balance()
