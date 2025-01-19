
from flask import Flask, jsonify, request
import requests
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Online Bookstore</h1>
    <ul>
        <li><a href="/users">View Users</a></li>
        <li><a href="/books">View Books</a></li>
        <li><a href="/orders">View Orders</a></li>
    </ul>
    <h3>Add a New User:</h3>
    <form action="/add_user" method="post">
        Name: <input type="text" name="name"><br>
        <input type="submit" value="Add User">
    </form>
    <h3>Add a New Book:</h3>
    <form action="/add_book" method="post">
        Title: <input type="text" name="title"><br>
        Author: <input type="text" name="author"><br>
        <input type="submit" value="Add Book">
    </form>
    <h3>Add a New Order:</h3>
    <form action="/add_order" method="post">
        User ID: <input type="number" name="user_id"><br>
        Book ID: <input type="number" name="book_id"><br>
        Quantity: <input type="number" name="quantity"><br>
        <input type="submit" value="Add Order">
    </form>
    '''

@app.route('/users')
def users():
    users = requests.get('http://user-service:5003/users').json()
    return jsonify(users)

@app.route('/books')
def books():
    books = requests.get('http://book-service:5001/books').json()
    return jsonify(books)

@app.route('/orders')
def orders():
    orders = requests.get('http://order-service:5002/orders').json()
    return jsonify(orders)

@app.route('/add_user', methods=['POST'])
def add_user():
    user_name = request.form['name']
    new_user = {"id": len(requests.get('http://user-service:5003/users').json()) + 1, "name": user_name}
    requests.post('http://user-service:5003/users', json=new_user)
    return jsonify(new_user)

@app.route('/add_book', methods=['POST'])
def add_book():
    book_title = request.form['title']
    book_author = request.form['author']
    new_book = {"id": len(requests.get('http://book-service:5001/books').json()) + 1, "title": book_title, "author": book_author}
    requests.post('http://book-service:5001/books', json=new_book)
    return jsonify(new_book)

@app.route('/add_order', methods=['POST'])
def add_order():
    user_id = request.form['user_id']
    book_id = request.form['book_id']
    quantity = request.form['quantity']
    new_order = {"id": len(requests.get('http://order-service:5002/orders').json()) + 1, "user_id": user_id, "book_id": book_id, "quantity": quantity}
    
    # Add order to order service
    response = requests.post('http://order-service:5002/orders', json=new_order)
    
    if response.status_code == 201:
        order_details = response.json()
        return f"""
        <h2>Your order has been placed. Thanks for shopping!</h2>
        <h3>Order Details:</h3>
        <p>Order ID: {order_details['id']}</p>
        <p>User ID: {order_details['user_id']}</p>
        <p>Book ID: {order_details['book_id']}</p>
        <p>Quantity: {order_details['quantity']}</p>
        """
    else:
        return "<h2>There was an issue placing your order. Please try again.</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
