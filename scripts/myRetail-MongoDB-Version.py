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

def getProducts():
    try: 
        products = list(mongo.db.products.find())
        if not products or len(products)==0:
            #Not Found
            return {'Error - products not found'},404
        else:
            #Successfully retrieved product(s)
            return json.dumps(products, default=json_util.default)
    except:
         return {"Error - Faild when retrieving products"},500

def getProductById(product_id):
    try: 
        product = list(mongo.db.products.find({"id":product_id}))
        if not product or len(product)==0:
            #Not Found
            return {'Error - product not found'},404
        else: 
            #Successfully retrieved product(s)
            return json.dumps(product, default=json_util.default)
    except:
         return {"Error - Faild when retrieving a product by id"},500

def insertProduct(product):
    try:
        mongo.db.products.insert(product)
        new_product = list(getProductById(product['id']))
        if not new_product or len(new_product)==0:
            #Not Found
            return {'Error - Faild insert - product not found'},404
        else: 
            #Successfully retrieved product(s)
            return json.dumps(new_product, default=json_util.default)
    except:
         return {"Error - Faild when inserting a product"},500

def updateProduct(old_product, new_product):
    try:
        update_count = mongo.db.products.replace_one(old_product, new_product)
        if update_count > 0:
            #Successfully updated
            return getProduct(new_product['id']),204
        else:
            #Not Found
            return {'Error - Faild update - product not found'},404
    except:
        return {"Error - Faild when updating a product"},500

def deleteProduct(product_id):
    try:
        product = getProductById(product_id)
        delete_count = mongo.db.products.delete_one({"id":product_id})
        delete_count = mongo.db.products.delete_one(product)
        if delete_count > 0:
            #Successfully deleted
            return {'Product successfuly deleted'},204
        else:
            #Not Found
             return {'Error - Faild delete - product not found'},404
    except:
        return {"Error - Faild when deleting a product"},500

# making a class for a particular resource 
# the get, post methods correspond to get and post requests 
# they are automatically mapped by flask_restful. 
# other methods include put, delete, etc. 
@api.route('/api/products', endpoint='products')
class GetProducts(Resource):
    # corresponds to the GET request 
    def get(self):
        return {'products':getProducts()} 

    # Corresponds to POST request 
    def post(self):
        product = request.get_json()
        return {'new product inserted': insertProduct(product)}, 201 # status code 

# adding the defined resources along with their corresponding urls 
@api.route('/api/product/<int:product_id>', endpoint='product')
class GetProductById(Resource): 
    # corresponds to the GET request
    def get(self, product_id): 
        product = getProductById(product_id)
        return {'product': product}

    # Corresponds to PUT request 
    def put(self, product_id):
        new_product = request.get_json()
        old_product = getProductById(product_id)
        updated_product = updateProduct(old_product, new_product)
        return {'updated product': updated_product}, 202 # status code 

    # Corresponds to DELETE request 
    def delete( self,product_id):
        product = getProductById(product_id)
        deleteProduct(product_id)
        return {'product has been deleted': product} 

# driver function 
if __name__ == '__main__':
    app.run(debug=True)