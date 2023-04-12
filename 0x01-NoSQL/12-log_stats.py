#!/usr/bin/env python3
"""
Log stats
"""
from pymongo import MongoClient

if __name__ == "__main__":
    # connect to client
    client = MongoClient('mongodb://127.0.0.1:27017')
    # connect to database
    nginx = client.logs.nginx

    # get number of documents in collection
    log = nginx.count_documents({})
    get = nginx.count_documents({"method": "GET"})
    post = nginx.count_documents({"method": "POST"})
    put = nginx.count_documents({"method": "PUT"})
    patch = nginx.count_documents({"method": "PATCH"})
    delete = nginx.count_documents({"method": "DELETE"})
    status = nginx.count_documents({"$and": [{"method": "GET"}, {"path": "/status"}]})

    print('''{} logs
Methods:
    method GET: {}
    method POST: {}
    method PUT: {}
    method PATCH: {}
    method DELETE: {}
{} status check'''
          .format(log, get, post, put, patch, delete, status)
          )
