from flask import Flask, current_app, request
from app.services.cacheService import cacheService

class cacheManager(object):

    def __init__(self, config):
        self.cacheService = cacheService.getInstance(config)

    def set(self, key, value):
        if key == None and value == None:
            return {"Error": "Invalid key value pair", "status":"404"}
        return self.cacheService.setData(key , value, True)

    def expire(self, key):
        if key == None:
            return {"Error": "Invalid key", "status":"404"}
        self.cacheService.pushOperation(key , True)

    def get(self , key ):
        if key == None:
            return {"Error": "Invalid key", "status":"404"}
        return self.cacheService.fetchData(key)


