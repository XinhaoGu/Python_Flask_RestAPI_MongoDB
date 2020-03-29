import requests
import json

# client is a fixture, injected by the `pytest-flask` plugin
# test GET products
def test_get_products(client):
    # Make a test call to /api/products
    response = client.get("/api/products")

    # Validate the response
    assert response.status_code == 200
    assert b'products' in response.data

# test GET product by product id
def test_get_product_by_id(client):
    # Make a test call to /api/product/id
    product_id = 13860428
    path = "http://localhost:5000/api/product/{0}".format(product_id)
    response = requests.get(path)

    # Validate the response
    product = {
        "product": {
            "id": 13860428,
            "name": "The Big Lebowski (Blu-ray) (Widescreen)",
            "current_price": {
                "value": 13.49,
                "currency_code": "USD"
            }
        }
    }
    assert response.status_code == 200
    assert response.json() == product

# test POST product 
def test_add_product(client):
    url = 'http://127.0.0.1:5000/api/products'
    
    # Additional headers.
    headers = {'Content-Type': 'application/json' } 

    # Body
    payload = {
        'id': 12345678, 
        'name': 'Xinhao\'s test', 
        'current_price': {
            "value": 19.99,
            "currency_code": "USD"
        }
    }
    
    # convert dict to json by json.dumps() for body data. 
    resp = requests.post(url, data = json.dumps(payload,indent=4))     
    assert resp.status_code == 201 # a new resource was successfully created in response to the request

    
# test PUT requesting - update an existing product by product id
def test_add_product(client):
    product_id = 13860428
    path = "http://localhost:5000/api/product/{0}".format(product_id)
    
    # Additional headers.
    headers = {'Content-Type': 'application/json' } 

    # Body
    payload = {
        "id": 13860428,
        "name": "The Big Lebowski (Blu-ray) (Widescreen)",
        "current_price": {
            "value": 99.99,
            "currency_code": "USD"
        }
    }
    
    # convert dict to json by json.dumps() for body data. 
    resp = requests.put(path, headers=headers, data = json.dumps(payload,indent=4))    
    assert resp.status_code == 200 

