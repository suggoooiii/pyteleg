# app.py
from flask import Flask, jsonify, request
from products import add_product, list_products, edit_product, delete_product

app = Flask(__name__)

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