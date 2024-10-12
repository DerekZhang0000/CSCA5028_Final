import auth
import kroger

def test_auth_token():
    token = auth.get_access_token()
    assert type(token) == str and token != ''

def test_kroger_api():
    token = auth.get_access_token()
    infos = kroger.get_product_infos('milk', access_token=token, limit=10)
    assert len(infos) == 10
    infos = kroger.get_product_infos('milk', access_token=token, limit=3)
    assert len(infos) == 3

def test_all():
    test_auth_token()
    test_kroger_api()

test_all()