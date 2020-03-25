#Hello, this is a local version of myRetial app, which it can run 
#without connecting to a persistent Database. 
#
#Xinhao Gu -- 3/20/2020

# using flask_restful 
from flask import Flask, request, json
from flask_restplus import Resource, Api

# using db provider 
import importlib.util

# using file path util
import os
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

# read json data from a local repository 
def pull_data():
    data_folder = Path("../util")
    file_to_open = data_folder / "json-Reader.py"
    exists = os.path.isfile(file_to_open)
    try: 
        if exists:
            json_Reader = module_from_file("jsonReaderHelper", file_to_open)
            products = json_Reader.jsonReaderHelper("product").GetJsonData()
            return products
    except FileNotFoundError: 
        return {}

# retrieve product by product id
def lookupProductById(product_id, products):
    product = [product for product in products if product['id'] == product_id][0]
    return product

# update product
def updateProduct(new_product, products):
    for product in products:
        if product['id'] == new_product['id']:
            product['name'] = new_product['name']
            product['current_price'] = new_product['current_price']
    return products

# remove product
def removeProduct(product, products):
    prod_dict = { i : products[i] for i in range(0, len(products) ) }
    for key, value in prod_dict.items():
        if value['id'] == product['id']:
            products.pop(key)
    return products

# write json data to a local repository 
def push_data(file_name, data):
    data_folder = Path("../util")
    file_to_open = data_folder / "json-Writer.py"
    exists = os.path.isfile(file_to_open)
    try: 
        if exists:
            json_writer = module_from_file("jsonWriterHelper", file_to_open)
            products = json_writer.jsonWriterHelper("product", data).PostJsonData()
            return products
    except FileNotFoundError: 
        return {}

# making a class for a particular resource 
# the get, post methods correspond to get and post requests 
# they are automatically mapped by flask_restful. 
# other methods include put, delete, etc. 
@api.route('/api/products', endpoint='products')
class GetProducts(Resource):
    # corresponds to the GET request. 
    def get(self):
        products = pull_data()
        return {'products':products} 

    # Corresponds to POST request 
    def post(self):
        try:
            products = pull_data()
            new_product = request.get_json()
            products.append(new_product)
            push_data('product', products)
            return {'new product added': products}, 201 # status code 
        except: 
            return "Error when posting resource", 500

# adding the defined resources along with their corresponding urls 
@api.route('/api/product/<int:product_id>', endpoint='product')
class GetProductById(Resource): 
    # corresponds to the GET request
    def get(self, product_id): 
        try:
            products = pull_data()
            product = lookupProductById(product_id, products)
            return {'product':product}, 200
        except: 
            return "product id not found'", 404

    # Corresponds to PUT request 
    def put(self, product_id): 
        try:
            products = pull_data()
            if not products:
                return {'Failed to update none existing product'}, 404
            else: 
                old_product = lookupProductById(product_id, products)
                new_product = request.get_json()
                products = updateProduct(new_product, products)
                push_data('product', products)
                return {'product updated': products}, 200
        except: 
            return {'Error when deleting resource'}, 500
        

    # Corresponds to DELETE request 
    def delete(self, product_id):
        try:
            products = pull_data()
            if not products:
                return {'Failed to delete none existing product'}, 404
            else: 
                product = lookupProductById(product_id, products)
                products = removeProduct(product, products) 
                push_data('product', products)
                return {'product removed': products}, 200
        except: 
            return {'Error when deleting resource'}, 500

# driver function 
if __name__ == '__main__':
    app.run(debug=True)
