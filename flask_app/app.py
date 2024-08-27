from flask import Flask, request, jsonify
from dotenv import load_dotenv
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson import ObjectId
import os

load_dotenv()

app = Flask(__name__)
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
mongo = PyMongo(app)

CORS(app)

db = mongo.db.users

@app.route("/", defaults={"filename": "index.html"})
@app.route("/<path:filename>")
def static_file(filename):
    return app.send_static_file(filename)

def parse_user_data(user):
    """Helper function to parse user data."""
    return {
        '_id': str(user['_id']),
        'name': user.get('name', ''),
        'email': user.get('email', ''),
        'contact': user.get('contact', ''),
        'address': user.get('address', '')
    }

@app.route("/api/users", methods=["GET"])
def get_all_users():
    try:
        users = db.find()
        user_list = [parse_user_data(user) for user in users]
        return jsonify(user_list), 200

    except Exception as e:
        return jsonify({'msg': f'Error: {str(e)}'}), 500

@app.route("/api/users", methods=["POST"])
def create_user():
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')

        if not name or not email:
            return jsonify({'msg': 'Name and Email are required fields'}), 400

        result = db.insert_one({
            'name': name,
            'email': email,
            'contact': data.get('contact', ''),
            'address': data.get('address', '')
        })

        return jsonify({'id': str(result.inserted_id), 'msg': "User Added Successfully"}), 201

    except Exception as e:
        return jsonify({'msg': f'Error: {str(e)}'}), 500

@app.route("/api/user/<id>", methods=['GET'])
def get_user_by_id(id):
    try:
        user = db.find_one({'_id': ObjectId(id)})

        if not user:
            return jsonify({'msg': 'User not found'}), 404

        return jsonify(parse_user_data(user)), 200

    except Exception as e:
        return jsonify({'msg': 'Invalid ID format'}), 400

@app.route("/api/users/<id>", methods=['DELETE'])
def delete_user_by_id(id):
    try:
        result = db.delete_one({'_id': ObjectId(id)})
        
        if result.deleted_count == 0:
            return jsonify({'msg': 'User not found'}), 404
        
        return jsonify({'msg': 'User Deleted Successfully'}), 200
    
    except Exception as e:
        return jsonify({'msg': f'Error: {str(e)}'}), 400

@app.route("/api/users/<id>", methods=['PUT'])
def update_user(id):
    try:
        user = db.find_one({'_id': ObjectId(id)})

        if not user:
            return jsonify({'msg': 'User not found'}), 404

        updated_data = {
            'name': request.json.get('name', user.get('name')),
            'email': request.json.get('email', user.get('email')),
            'contact': request.json.get('contact', user.get('contact')),
            'address': request.json.get('address', user.get('address'))
        }

        db.update_one({'_id': ObjectId(id)}, {'$set': updated_data})

        return jsonify({'msg': "User Updated Successfully"}), 200

    except Exception as e:
        return jsonify({'msg': 'Invalid ID format'}), 400

if __name__ == '__main__':
    app.run(debug=True)