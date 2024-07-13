# app.py
from flask import Flask, jsonify, request, send_from_directory, redirect
from products import add_product, list_products, edit_product, delete_product
import logging

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__,static_folder='static')

@app.before_request
def log_request_info():
    app.logger.debug('Headers: %s', request.headers)
    app.logger.debug('Body: %s', request.get_data())

@app.before_request
def before_request():
    if not request.is_secure:
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=301)


@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(list_products())

@app.route('/products', methods=['POST'])
def add_new_product():
    data = request.get_json()
    add_product(data['name'], data['price'])
    return jsonify({'status': 'success'}), 201

@app.route('/products/<int:index>', methods=['PUT'])
def update_product(index):
    data = request.get_json()
    edit_product(index, data['name'], data['price'])
    return jsonify({'status': 'success'})

@app.route('/products/<int:index>', methods=['DELETE'])
def remove_product(index):
    delete_product(index)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)