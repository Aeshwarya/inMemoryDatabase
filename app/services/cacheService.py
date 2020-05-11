from store import cacheStore
import cacheConfig
from models import operations
from models import faliureQueue


class cacheService():


    __instance = None

    @staticmethod 
    def getInstance():
   
      if cacheService.__instance == None:
         cacheService()
      return cacheService.__instance

    def __init__(self):
    
      if cacheService.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         self.cacheStore = cacheStore
         servers = cacheConfig.servers
         for server in range(0 , cacheConfig.NUMBER_OF_NODES):
             if server["name"] != self.current.server:
                 setUrl = "http://"+server["host"]+":"+server["port"]+"/set"
                 deleteUrl = "http://"+server["host"]+":"+server["port"]+"/delete"
                 serverList[server["name"]] = {"setUrl":setUrl, "deleteUrl":deleteUrl}
         self.faliureQueue = []
         cacheService.__instance = self


    def fetchData(self , key):
        return self.cacheStore.get(key)


    def setData(self, key , value):
        self.cacheStore.get(key)
        saveDataInOtherCache(key, value)


    def saveDataInOtherCache(key, value):
        try:
            params = {"key":key , "value":value}
            for server in serverList:
                resp = requests.post(server["setUrl"], params)

        Exception:
            # failed operation can be pushed to queue and asked to reregister
            


    def removeDataInOtheCase():
        try:
            params = {"key":key , "value":value}
            for server in serverList:
                operationFailed = False
                resp = requests.post(server["setUrl"], params)
                if not resp:
                    # operation failed
                    operationFailed = True
                else:
                    if resp["status"] != 200:
                       operationFailed = True
                if operationFailed == True:
                    
                    self.faliureQueue.push()
        Exception:
            # failed operation can be pushed to queue and asked to reregister

    

    def pushOperation(self, op):
        operation = operations.GET
        data = key
        op = queue(operation, data)

