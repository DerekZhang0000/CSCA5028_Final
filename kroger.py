import requests

def get_products(params=None, access_token=''):
    url = 'https://api.kroger.com/v1/products'

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    
    except:
        return None

def get_product_infos(product, access_token='', limit=10):
    params = {
        'filter.term': f'{product}',
        'filter.limit': f'{limit}',
        'filter.locationId': '01400413',    # Loveland Kroger Store
    }
    
    result = get_products(params, access_token)
    
    if result:
        data_tups = []
        data = result['data']
        for product_data in data:
            product_id = product_data['productId']
            product_name = product_data['description']
            price = product_data['items'][0]['price']['regular']
            data_tups.append((int(product_id), product_name, float(price)))

        return data_tups