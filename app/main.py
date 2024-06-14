from flask import Flask
from .routes import set_routes

app = Flask(__name__)
# Call the set_routes function to set up the endpoints
set_routes(app)

if __name__ == '__main__':
    app.run(debug=True, port=5001)