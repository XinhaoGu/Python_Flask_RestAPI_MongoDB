#Hello, this is a local version of myRetial app, which it can run 
#without connecting to a persistent Database. 
#
#Xinhao Gu -- 3/20/2020

# using flask_restful 
from flask import Flask, request
from flask_restplus import Resource, Api

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
@api.route('/api/products', endpoint='products')
class GetProducts(Resource):
    # corresponds to the GET request. 
    def get(self):
        return {'products':products} 

    # Corresponds to POST request 
    def post(self):
        new_product = request.get_json()
        products.append(new_product)
        return {'new product': new_product}, 201 # status code 


# adding the defined resources along with their corresponding urls 
@api.route('/api/product/<int:product_id>', endpoint='product')
class GetProductById(Resource): 
    # corresponds to the GET request
    def get(self, product_id): 
        product = lookupProductById(product_id)
        return {'product': product}

    # Corresponds to PUT request 
    def put(self, product_id): 
        old_product = lookupProductById(product_id)
        index_old_product = products.index(old_product)
        new_product = request.get_json()
        products[index_old_product] = new_product
        return {'updated product': new_product}

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
