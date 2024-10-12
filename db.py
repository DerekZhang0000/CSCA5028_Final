import sqlite3
import time

def create_database():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        last_price REAL
    )
    ''')

    connection.commit()
    connection.close()

def add_product(product_id, product_name, new_price):
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('''
    SELECT id FROM Products WHERE id = ?
    ''', (product_id,))
    result = cursor.fetchone()

    if result is None:
        cursor.execute('''
        INSERT INTO Products (id, name, last_price)
        VALUES (?, ?, ?)
        ''', (product_id, product_name, new_price))

        table_name = f'product_{product_id}'
        cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            price REAL,
            timestamp TEXT
        )
        ''')
        
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(f'''
        INSERT INTO {table_name} (price, timestamp)
        VALUES (?, ?)
        ''', (new_price, timestamp))
    
    else:
        table_name = f'product_{product_id}'
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        
        cursor.execute(f'''
        INSERT INTO {table_name} (price, timestamp)
        VALUES (?, ?)
        ''', (new_price, timestamp))

    cursor.execute('''
    UPDATE Products SET last_price = ? WHERE id = ?
    ''', (new_price, product_id))

    connection.commit()
    connection.close()

def get_price_history(identifier):
    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    
    table_name = f'product_{identifier}'
    c.execute(f'''
    SELECT price, timestamp FROM {table_name}
    ''')
    price_history = c.fetchall()

    conn.close()

    if price_history:
        return price_history
    else:
        return None