from flask import Flask, jsonify, request
app = Flask(__name__)

# In-memory order storage
orders = []

@app.route('/', methods=['GET'])
def index():
    return "Welcome to the Order Service!"

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/orders', methods=['POST'])
def create_order():
    new_order = request.get_json()  # Expecting JSON data in request body
    orders.append(new_order)  # Add the new order to the list
    return jsonify(new_order), 201  # Return created order with a 201 status

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
