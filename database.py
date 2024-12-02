#Handles database setup and connections. This file ensures that 
#the necessary tables (users and work_orders) exist and 
#provides a function to connect to the database.
#Programmer: Trevone Graves
#Date: 12-1-2024

import sqlite3

def initialize_db():
    conn = sqlite3.connect('work_order.db')
    cursor = conn.cursor()

    # Create the table for users
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT,
            role TEXT
        )
    ''')

    # Create the table for work orders
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS work_orders (
            id INTEGER PRIMARY KEY, 
            title TEXT NOT NULL,
            description TEXT,
            priority TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Open',
            created_at TEXT NOT NULL,
            updated_at TEXT
        )
    ''')

    conn.commit()
    conn.close()

def connect_db():
    return sqlite3.connect('work_order.db')
