from services import cacheService
from models import operations
from models import queue

class cacheManager(object):
    
    def __init__():
        self.cacheService = cacheService()

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










