#Manages user authentication and registration. This file is responsible for securing 
#user credentials and interacting with the users table 
#in the database.
#Programmer: Trevone Graves
#Date: 12-1-2024

import hashlib
from database import connect_db

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password, role):
    conn = connect_db()
    cursor = conn.cursor()

    hashed_password = hash_password(password)
    cursor.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)',
                   (username, hashed_password, role))
    conn.commit()
    conn.close()

def login_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()

    hashed_password = hash_password(password)
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?',
                   (username, hashed_password))
    user = cursor.fetchone()

    conn.close()
    return user
