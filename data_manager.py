import json
import os
import hashlib

def hash_password(password):
    """Returns a SHA-256 hash of the given password string."""
    return hashlib.sha256(password.encode()).hexdigest()

def load_data(filename, default_type):
    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        return default_type
    with open(filename, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return default_type

def save_data(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)