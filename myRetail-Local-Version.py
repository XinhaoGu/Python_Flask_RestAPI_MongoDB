'''
Hello, this is a local version of myRetial app. By all means, my may run it 
without connecting to a persistent Database. 

Xinhao -- 3/20/2020
'''

# using flask_restful 
from flask import Flask, request
from flask_restful import Resource, Api, abort

# creating the flask app 
app = Flask(__name__)
# creating an API object 
api = Api(app)

products = [
    {
        'id': 13860428,
        'name': 'The Big Lebowski (Blu-ray) (Widescreen)',
        'current_price': {
            'value':13.49,
            'currency_code':'USD'
        }
    },
    {
        'id': 15117729,
        'name': 'Star Wars - The Reise of Skywalker (Blu-Ray)',
        'current_price': {
            'value':24.99,
            'currency_code':'USD'
        }
    },
    {
        'id': 16483589,
        'name': 'Frozen II - (Blu-Ray + DVD + Digital)',
        'current_price': {
            'value':20.00,
            'currency_code':'USD'
        }
    },
    {
        'id': 16696652,
        'name': '1917 (Blu-Ray + DVD + Digital)',
        'current_price': {
            'value':24.99,
            'currency_code':'USD'
        }
    },
    {
        'id': 16752456,
        'name': 'Joker (2019) Digital HD',
        'current_price': {
            'value':24.99,
            'currency_code':'USD'
        }
    },
    {
        'id': 15643793,
        'name': 'Jumanji (Blu-Ray + DVD + Digital)',
        'current_price': {
            'value':22.99,
            'currency_code':'USD'
        }
    }
]

def lookupProductById(product_id):
     product = [product for product in products if product['id'] == product_id]
     return product

# making a class for a particular resource 
# the get, post methods correspond to get and post requests 
# they are automatically mapped by flask_restful. 
# other methods include put, delete, etc. 
class GetProducts(Resource):
    # corresponds to the GET request. 
    def get(self):
        return {'products':products}, 

    # Corresponds to POST request 
    def post(self):
        newProduct = request.get_json()
        products.append(newProduct)
        return {'new product': newProduct}, 201 # status code 

class GetProductById(Resource): 
    # corresponds to the GET request
    def get(self, product_id): 
        product = lookupProductById(product_id)
        return {'product': product}

    # Corresponds to PUT request 
    def put(self, product_id): 
        oldProduct = lookupProductById(product_id)
        indexOldProduct = products.index(oldProduct)
        newProduct = request.get_json()
        products[indexOldProduct] = newProduct
        return {'updated product': newProduct}

# adding the defined resources along with their corresponding urls 
api.add_resource(GetProducts, '/api/products')
api.add_resource(GetProductById, '/api/product/<int:product_id>', endpoint='product_ep')

# driver function 
if __name__ == '__main__':
    app.run(debug=True)