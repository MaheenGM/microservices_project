from flask import Flask, jsonify, request
app = Flask(__name__)

# In-memory book storage
books = []

@app.route('/', methods=['GET'])
def index():
    return "Welcome to the Book Service!"

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.get_json()  # Expecting JSON data in request body
    books.append(new_book)  # Add the new book to the list
    return jsonify(new_book), 201  # Return created book with a 201 status

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
