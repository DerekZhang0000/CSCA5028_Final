import auth
import kroger
import db
import fake_db

def test_integration():
    milk_points = db.get_price_history('1111040101')
    fake_milk_points = fake_db.get_price_history('1111040101')

    access_token = auth.get_access_token()
    data = kroger.get_product_infos('milk', access_token, limit=10)
    for id, name, price in data:
        db.add_product(id, name, price)
        fake_db.add_product(id, name, price)
    new_milk_points = db.get_price_history('1111040101')
    new_fake_milk_points = fake_db.get_price_history('1111040101')
    assert new_milk_points == milk_points + 1
    assert new_fake_milk_points == fake_milk_points + 1

test_integration()