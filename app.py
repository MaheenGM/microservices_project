from flask import Flask, jsonify, request
app = Flask(__name__)

# In-memory user storage (this can be a database in a real application)
users = []

@app.route('/', methods=['GET'])
def index():
    return "Welcome to the User Service!"

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.get_json()  # Expecting JSON data in request body
    users.append(new_user)  # Add the new user to the list
    return jsonify(new_user), 201  # Return created user with a 201 status

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
