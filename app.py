from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest
import jwt
import psycopg2
from pymongo import MongoClient

app = Flask(__name__)

# Define a dictionary to store prices for each product
product_prices = {
    "Crusty Chicken": 5.99,
    "New Yorker": 6.99,
    "Meatfree Cheezy": 7.99
}

# Define a list of items for which the "Buy 1, Get 2" offer should be applied
special_offer_items = {"Crusty Chicken", "New Yorker"}

# PostgreSQL connection
postgres_connection = psycopg2.connect(
    dbname="david",
    user="david",
    password="your_password",
    host="localhost"
)
postgres_cursor = postgres_connection.cursor()

# MongoDB connection
mongo_client = MongoClient("mongodb://localhost:27017")
mongo_db = mongo_client["your_mongodb_database"]
mongo_collection = mongo_db["your_mongodb_collection"]

# Set the secret key for JWT token
app.config['SECRET_KEY'] = 'your_secret_key'


def process_special_offer(order, apply_special_offer=True):
    total_price = 0
    for item, quantity in order.items():
        if apply_special_offer and item in special_offer_items and quantity >= 2:
            quantity -= quantity // 2  # apply "2 for 1" offer
        total_price += product_prices.get(item, 0) * quantity
    return total_price


def verify_token(token):
    try:
        payload = jwt.decode(
            token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        raise BadRequest(description="Token expired, please log in again")
    except jwt.InvalidTokenError:
        raise BadRequest(description="Invalid token, please log in again")


@app.route('/checkout', methods=['POST'])
def checkout():
    # check if token is provided in the header
    token = request.headers.get('Authorization')
    if not token or not token.startswith('Bearer '):
        raise BadRequest(
            description="Authorization token is missing or invalid.")

    token = token.split(' ')[1]  # extract token from "Bearer <token>"
    try:
        # Verify the token
        payload = verify_token(token)
    except BadRequest as e:
        return jsonify({"error": str(e)}), 401

    order = request.json
    if not order:
        return jsonify({"error": "No order data provided"}), 400

    # Check if the order exceeds the maximum allowed quantity
    apply_special_offer = payload.get('apply_special_offer', False)

    # Process the special offer
    total_price = process_special_offer(order, apply_special_offer)
    return jsonify({"total_price": total_price})


if __name__ == '__main__':
    app.run(debug=True)
