from flask import Flask, request, jsonify
from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')
db = client['quotes_db']
collection = db['quotes']

app = Flask(__name__)

@app.route('/store', methods=['POST'])
def store_data():
    data = request.json
    collection.insert_one(data)
    return jsonify({'message': 'Data stored'}), 201

if __name__ == '__main__':
    app.run(port=5000)