from db import users_collection
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(username, password):
    if users_collection.find_one({"username": username}):
        return False, "User already exists"
    hashed_password = generate_password_hash(password)
    users_collection.insert_one({"username": username, "password": hashed_password})
    return True, "User created"

def validate_user(username, password):
    user = users_collection.find_one({"username": username})
    if user and check_password_hash(user["password"], password):
        return True
    return False
