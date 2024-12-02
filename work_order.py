#Handles operations related to 
#work orders, such as creating, listing, 
#and updating work orders.
#Programmer: Trevone Graves
#Date: 12-1-2024

import datetime
from database import connect_db

def create_work_order(title, description, priority):
    conn = connect_db()
    cursor = conn.cursor()

    created_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''
        INSERT INTO work_orders (title, description, priority, created_at)
        VALUES (?, ?, ?, ?)
    ''', (title, description, priority, created_at))

    conn.commit()
    conn.close()

def list_work_orders():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM work_orders')
    work_orders = cursor.fetchall()

    conn.close()
    return work_orders

def update_work_order_status(order_id, new_status):
    conn = connect_db()
    cursor = conn.cursor()

    updated_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''
        UPDATE work_orders
        SET status = ?, updated_at = ?
        WHERE id = ?
    ''', (new_status, updated_at, order_id))

    conn.commit()
    conn.close()
