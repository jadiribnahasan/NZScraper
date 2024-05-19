from bson import json_util
from flask import Flask, request, jsonify
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['quotes_db']
collection = db['quotes']

app = Flask(__name__)

@app.route('/quotes', methods=['GET'])
def get_quotes():
    quotes = list(collection.find({}, {"quote": 1, "author": 1, "_id": 0}))
    return json_util.dumps(quotes), 200

@app.route('/quotes/<id>', methods=['PUT'])
def update_quote(id):
    quote = request.json['quote']
    collection.update_one({'_id': id}, {'$set': {'quote': quote}})
    return jsonify({'message': 'Quote updated'}), 200

@app.route('/quotes/<id>', methods=['DELETE'])
def delete_quote(id):
    collection.delete_one({'_id': id})
    return jsonify({'message': 'Quote deleted'}), 200

if __name__ == '__main__':
    app.run(port=5001)