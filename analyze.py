import sqlite3
import matplotlib.pyplot as plt
import pandas as pd

import db
import io

product_dict = {
    'product_1111040101': 'Milk',
    'product_1111009434': 'Cheese',
}

def plot_prices(table_name):
    conn = sqlite3.connect('products.db')
    query = f"SELECT price, timestamp FROM {table_name} ORDER BY timestamp"
    data = pd.read_sql_query(query, conn)
    conn.close()

    data['timestamp'] = pd.to_datetime(data['timestamp'])

    plt.figure(figsize=(10, 6))
    plt.plot(data['timestamp'], data['price'], marker='o', linestyle='-', color='b')
    plt.title(f"Price vs. Time of {product_dict[table_name]}")
    plt.xlabel('Timestamp')
    plt.ylabel('Price')
    plt.grid(True)

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    return buf.getvalue()