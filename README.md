# Python_Flask_RestAPI_MongoDB

## Project Title: 
Build a simple RESTful API web service using Python Flask and Swagger UI 

## Motivation: 
First things first, A RESTful API is an application program interface (API) that uses HTTP requests to GET, PUT, POST and DELETE data. A RESTful API -- also referred to as a RESTful web service or REST API -- is based on representational state transfer (REST) technology, an architectural style and approach to communications often used in web services development. The REST design does not require a specific format for the data provided with the requests. In general data is provided in the request body as a JSON blob, or sometimes as arguments in the query string portion of the URL.

![](/images/REST.png)

This project adheres to the REST guidelines then becomes an exercise in identifying the resources that will be exposed and how they will be affected by the different request methods.The goal for this exercise is to create an end-to-end Proof-of-Concept for a products API, which will create a RESTful service that can retrieve product and price details by ID, and aggregate product data from multiple sources and return it as JSON to the caller. 

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
