fake_db = {'id_1': [1], 'id_2': [1, 2], 'id_3': [1, 2, 3], '1111040101': [1, 2, 3]}

def get_price_history(id):
    return fake_db[id]

def add_product(id, name, price):
    fake_db[id].append(price)