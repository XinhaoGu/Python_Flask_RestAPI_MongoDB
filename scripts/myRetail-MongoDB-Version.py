# Hello, down below is a MongoDB version of myRetail app 
# to run this app, you need to have MongoDB installed and create a document called 'myRetail'
# and then create a db called 'products', run the MongoDB server at port 27017 
# Xinhao -- 03/20/2020

# using flask_restful 
from flask import Flask, request, json
from flask_restplus import Resource, Api
from flask_pymongo import PyMongo
from bson import json_util

# using db provider 
import importlib.util

# using file path util
from pathlib import Path

def module_from_file(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# creating the flask app 
app = Flask(__name__)

# creating an API object 
api = Api(app)

# configure MongoDB
data_folder = Path("../database")
file_to_open = data_folder / "db-Provider.py"
db_Provider = module_from_file("db-Provider", file_to_open)
app.config["MONGO_URI"] = db_Provider.DBHelper("MongoDB").GetURI()

mongo = PyMongo(app)


# making a class for a particular resource 
# the get, post methods correspond to get and post requests 
# they are automatically mapped by flask_restful. 
# other methods include put, delete, etc. 
@api.route('/api/products', endpoint='products')
class GetProducts(Resource):
    # corresponds to the GET request 
    def get(self):
        products = json.dumps(list(mongo.db.products.find()), default=json_util.default)
        return {'products':products} 

    # Corresponds to POST request 
    def post(self):
        new_product = request.get_json()
        mongo.db.products.insert(new_product)
        return {'new product': new_product}, 201 # status code 

# adding the defined resources along with their corresponding urls 
@api.route('/api/product/<int:product_id>', endpoint='product')
class GetProductById(Resource): 
    # corresponds to the GET request
    def get(self, product_id): 
        product = json.dumps(list(mongo.db.products.find({"id":product_id})), default=json_util.default)
        return {'product': product}

    # Corresponds to PUT request 
    def put(self, product_id):
        updated_product = request.get_json()
        mongo.db.products.remove({"id": product_id})
        mongo.db.products.insert(updated_product)
        return {'updated product': updated_product}, 202 # status code 

    # Corresponds to DELETE request 
    def delete( self,product_id):
        try:
            deleteCount = mongo.db.products.delete_one ({"id":product_id})
            if deleteCount > 0:
                #Successfully deleted
                return "",204
            else:
                #Not Found
                return "",404
        except:
            #Error when deleting resource
            return "",500

# driver function 
if __name__ == '__main__':
    app.run(debug=True)