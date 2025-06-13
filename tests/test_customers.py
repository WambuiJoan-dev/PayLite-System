import json


def get_access_token(test_client):
    response = test_client.post('/auth/login', json={
        "username": "Jedidah",
        "password": "Jeddy@1"
    })
    data = response.get_json()
    return data["access_token"]


def test_get_customers(test_client):
    token = get_access_token(test_client)
    response = test_client.get('/customers/', headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200


def test_post_customer(test_client):
    token = get_access_token(test_client)
    response = test_client.post('/customers/', headers={
        "Authorization": f"Bearer {token}"
    }, json={
        "name": "Test Customer",
        "national_id": "98765432",
        "credit_status": "Active"
    })
    data = response.get_json()
    assert response.status_code == 201
    assert "id" in data
    assert data["name"] == "Test Customer"


def test_put_customer(test_client):
    token = get_access_token(test_client)

    
    post_response = test_client.post('/customers/', headers={
        "Authorization": f"Bearer {token}"
    }, json={
        "name": "Customer To Update",
        "national_id": "12344321",
        "credit_status": "Active"
    })
    customer_id = post_response.get_json()["id"]

    
    put_response = test_client.put(f'/customers/{customer_id}', headers={
        "Authorization": f"Bearer {token}"
    }, json={
        "name": "Updated Name",
        "national_id": "12344321",
        "credit_status": "Completed"
    })

    put_data = put_response.get_json()
    assert put_response.status_code == 200
    assert put_data["name"] == "Updated Name"
    assert put_data["credit_status"] == "Completed"


def test_delete_customer_admin(test_client):
    token = get_access_token(test_client)

    
    post_response = test_client.post('/customers/', headers={
        "Authorization": f"Bearer {token}"
    }, json={
        "name": "Customer To Delete",
        "national_id": "11223344",
        "credit_status": "Active"
    })
    customer_id = post_response.get_json()["id"]

    
    delete_response = test_client.delete(f'/customers/{customer_id}', headers={
        "Authorization": f"Bearer {token}"
    })

    delete_data = delete_response.get_json()
    
    assert delete_response.status_code in [200, 403]

    if delete_response.status_code == 200:
        assert delete_data["message"] == "Customer deleted"
