from flask import Blueprint, request, jsonify
from db import todos_collection
from bson import ObjectId

todo_bp = Blueprint('todo', __name__)

@todo_bp.route('/api/todos', methods=['GET'])
def get_todos():
    todos = []
    for todo in todos_collection.find():
        todos.append({"_id": str(todo["_id"]), "title": todo["title"]})
    return jsonify(todos)

@todo_bp.route('/api/todos', methods=['POST'])
def add_todo():
    data = request.json
    title = data.get('title')
    result = todos_collection.insert_one({"title": title})
    return jsonify({"_id": str(result.inserted_id), "title": title}), 201

@todo_bp.route('/api/todos/<id>', methods=['DELETE'])
def delete_todo(id):
    todos_collection.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Todo deleted"}), 200
