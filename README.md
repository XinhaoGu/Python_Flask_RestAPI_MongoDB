# Python_Flask_RestAPI_MongoDB
![](/images/Flask+Mongo.jpg)

## Project Title: 
Build a simple RESTful API web service using Python Flask and Swagger UI 

## Motivation: 
First things first, A RESTful API is an application program interface (API) that uses HTTP requests to GET, PUT, POST and DELETE data. A RESTful API -- also referred to as a RESTful web service or REST API -- is based on representational state transfer (REST) technology, an architectural style and approach to communications often used in web services development. The REST design does not require a specific format for the data provided with the requests. In general data is provided in the request body as a JSON blob, or sometimes as arguments in the query string portion of the URL.

![](/images/REST.png)

Secondly, a quick overview what's MongoDB and what are the differences in compare to any traditional relational databases. 
MongoDB stores data in documents, and documents are not just key/value pairs but can include arrays and subdocuments. The data itself can be different data types like geospatial, decimal, and ISODate to name a few. Internally MongoDB stores a binary representation of JSON known as BSON. This allows MongoDB to provide data types like decimal that are not defined in the JSON specification. For more information on the BSON spec check out the following URL: http://bsonspec.org.

A collection in MongoDB is a container for documents. A database is the container for collections. This grouping is similar to relational databases and is pictured below:

![](/images/MongoDB.png)

Finally, let go over what's is this project does - the project adheres to the REST guidelines then becomes an exercise in identifying the resources that will be exposed and how they will be affected by the different request methods.The goal for this exercise is to create an end-to-end Proof-of-Concept for a products API, which will create a RESTful service that can retrieve product and price details by ID, and aggregate product data from multiple sources and return it as JSON to the caller. 

## Pre-requisites

One must have Python installed in his local system for deploying this RESTFUL-API easily. Other than Python one must also have to install Python-Flask and its dependencies.

```
Python v3.7+ 
MogoDB v3.2+
PIP v20+
pip install Flask 
pip install flask-restplus
pip install Flask-PyMongo
pip install bson
pip install Werkzeug 0.16.0
```

## Running the RESTFUL-API Service

Run local none DB version
```
python .\myRetail-Local-Version.py
```
Run local + MongoDB version
```
python .\myRetail-MongoDB-Version.py
```

## Checking the User Interface
```
https://localhost:5000/
```

## Checking the Swagger UI 
```
https://localhost
```
![](/images/Swagger.png)

## Checking MongoDB Server
```
https://localhost:27017
```

### to start MongoDB server
```
cd C:\Program Files (x86)\MongoDB\Server\3.2\bin
mongod.exe --dbpath C:\MongoDB\data\db
```

### to start MongoDB client 
```
cd C:\Program Files (x86)\MongoDB\Server\3.2\bin
mongo.exe
```

### remove lock and repair db
```
mongod --dbpath C:\MongoDB\data\db --repair
mongod --storageEngine=mmapv1 --dbpath C:\MongoDB\data\db
```

### (basic commands ---> start MongoDB client ---> list all the databases)
``` 
show dbs 
```
### switch to db testDB
```
use testDB 
```
### show collections under testDB
```
show collections
```
### delete database 
```
db.dropDatabase()
```
### create new DB 
```
user testDB
```
### check which DB you are in 
```
db
```
### create collections 
```
db.createCollection('yourCollection')
```
### show collections 
```
show collections
```
### insert record into collection 
```
db.<yourCollection>.insert({yourRecord})

example: db.products.insert(
    {
        'id': 13860428,
        'name': 'The Big Lebowski (Blu-ray) (Widescreen)',
        'current_price': {
            'value':13.49,
            'currency_code':'USD'
        }
    }
)
```
### bulk insert records into collection 
```
db.<yourColleciton>.insertMany([{},{},{}....])

example: 
db.products.insertMany([
    {
        "id": 13860428,
        "name": "The Big Lebowski (Blu-ray) (Widescreen)",
        "current_price": {
            "value":13.49,
            "currency_code":"USD"
        }
    },
    {
        "id": 15117729,
        "name": "Star Wars - The Reise of Skywalker (Blu-Ray)",
        "current_price": {
            "value":24.99,
            "currency_code":"USD"
        }
    },
    {
        "id": 16483589,
        "name": "Frozen II - (Blu-Ray + DVD + Digital)",
        "current_price": {
            "value":20.00,
            "currency_code":"USD"
        }
    },
    {
        "id": 16696652,
        "name": "1917 (Blu-Ray + DVD + Digital)",
        "current_price": {
            "value":24.99,
            "currency_code":"USD"
        }
    },
    {
        "id": 16752456,
        "name": "Joker (2019) Digital HD",
        "current_price": {
            "value":24.99,
            "currency_code":"USD"
        }
    },
    {
        "id": 15643793,
        "name": "Jumanji (Blu-Ray + DVD + Digital)",
        "current_price": {
            "value":22.99,
            "currency_code":"USD"
        }
    }
])

```