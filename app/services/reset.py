from app.state import accounts

def reset_server():
    accounts.clear()
    return '', 200
