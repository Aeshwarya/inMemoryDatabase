from services import cacheService
from models import operations
from models import queue

class cacheManager(object):
    
    def __init__():
        self.cacheService = cacheService()


    def set(self, key, value):
        return self.cacheService.setData(key , value, True)

    def expire(self, key):
        if key == None:
            return ""
        self.cacheService.pushOperation(key , True)


    def get(self , key ):
        return self.cacheService.fetchData(key)










