from enum import Enum, auto
from flask import Flask, jsonify, request
from app.services.event import handle_deposit, handle_withdraw, handle_transfer
from app.services.balance import get_balance
from app.services.reset import reset_server


class EventType(Enum):
    DEPOSIT = auto()
    WITHDRAW = auto()
    TRANSFER = auto()


def set_routes(app: Flask):
    @app.route("/")
    def home():
        return "root"

    @app.route("/reset", methods=["POST"])
    def reset_state():
        return reset_server()

    @app.route("/balance", methods=["GET"])
    def balance():
        return get_balance()

    @app.route("/event", methods=["POST"])
    def handle_event():
        data = request.get_json()
        event_type = data.get("type")

        try:
            event_type_enum = EventType[
                event_type.upper()
            ]  # Convert string to EventType
        except KeyError:
            return jsonify({"error": "Invalid event type"}), 400

        if event_type_enum == EventType.DEPOSIT:
            return handle_deposit(data)
        elif event_type_enum == EventType.WITHDRAW:
            return handle_withdraw(data)
        elif event_type_enum == EventType.TRANSFER:
            return handle_transfer(data)
