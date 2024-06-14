from flask import request, jsonify

users = {}

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
    return jsonify({"message": "State has been reset"}), 200
