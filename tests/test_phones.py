

def get_access_token(test_client):
    response = test_client.post('/auth/login', json={
        "username": "Jedidah",
        "password": "Jeddy@1"
    })
    data = response.get_json()
    return data["access_token"]


def test_get_phones(test_client):
    token = get_access_token(test_client)
    response = test_client.get('/phones/', headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200


def test_post_phone(test_client):
    token = get_access_token(test_client)
    response = test_client.post('/phones/', headers={
        "Authorization": f"Bearer {token}"
    }, json={
        "brand": "TestBrand",
        "model": "TestModel",
        "price": 25000,
        "stock_quantity": 15
    })
    data = response.get_json()
    assert response.status_code == 201
    assert "id" in data
    assert data["brand"] == "TestBrand"
    assert data["model"] == "TestModel"


def test_put_phone(test_client):
    token = get_access_token(test_client)

    
    post_response = test_client.post('/phones/', headers={
        "Authorization": f"Bearer {token}"
    }, json={
        "brand": "BrandToUpdate",
        "model": "ModelToUpdate",
        "price": 30000,
        "stock_quantity": 20
    })
    phone_id = post_response.get_json()["id"]

    
    put_response = test_client.put(f'/phones/{phone_id}', headers={
        "Authorization": f"Bearer {token}"
    }, json={
        "price": 28000,
        "stock_quantity": 18
    })

    put_data = put_response.get_json()
    assert put_response.status_code == 200
    assert put_data["price"] == 28000
    assert put_data["stock_quantity"] == 18


def test_delete_phone_admin(test_client):
    token = get_access_token(test_client)

    
    post_response = test_client.post('/phones/', headers={
        "Authorization": f"Bearer {token}"
    }, json={
        "brand": "BrandToDelete",
        "model": "ModelToDelete",
        "price": 15000,
        "stock_quantity": 5
    })
    phone_id = post_response.get_json()["id"]

    
    delete_response = test_client.delete(f'/phones/{phone_id}', headers={
        "Authorization": f"Bearer {token}"
    })

    delete_data = delete_response.get_json()
    
    assert delete_response.status_code in [200, 403]

    if delete_response.status_code == 200:
        assert delete_data["message"] == "Phone deleted"
