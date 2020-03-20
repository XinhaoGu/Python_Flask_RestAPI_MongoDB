'''
Hello, down below is a MongoDB version of myRetail app 
to run this app, you need to have MongoDB installed and create a document called 'myRetail'
and then create a db called 'products', run the MongoDB server at port 27017 

Below is a list of json objects need to insert into myRetail.products database

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

Xinhao -- 03/20/2020
'''

# using flask_restful 
from flask import Flask, request, json
from flask_restful import Resource, Api
from flask_pymongo import PyMongo
from bson import json_util

# creating the flask app 
app = Flask(__name__)
# creating an API object 
api = Api(app)
# configure MongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/myRetail"
mongo = PyMongo(app)

# making a class for a particular resource 
# the get, post methods correspond to get and post requests 
# they are automatically mapped by flask_restful. 
# other methods include put, delete, etc. 
class GetProducts(Resource):
    # corresponds to the GET request. 
    def get(self):
        products = json.dumps(list(mongo.db.products.find()), default=json_util.default)
        return {'products':products} 

    # Corresponds to POST request 
    def post(self):
        newProduct = request.get_json()
        mongo.db.products.insert(newProduct)
        return {'new product': newProduct}, 201 # status code 

# another resource to calculate the square of a number
class GetProductById(Resource): 
    def get(self, product_id): 
        product = json.dumps(list(mongo.db.products.find({"id":product_id})), default=json_util.default)
        return {'product': product}

# adding the defined resources along with their corresponding urls 
api.add_resource(GetProducts, '/api/products')
api.add_resource(GetProductById, '/api/product/<int:product_id>', endpoint='product_ep')

# driver function 
if __name__ == '__main__':
    app.run(debug=True)