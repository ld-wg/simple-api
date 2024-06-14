from app.state import accounts


def reset_server():
    accounts.clear()
    return "OK", 200
