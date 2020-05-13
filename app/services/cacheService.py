from flask import Flask
import requests
import json
from .baseService import BaseService
from ..store.cacheStore import LRUCache
from ..models.operations import operations
from ..models.faliureQueue import faliureQueue


class cacheService:

    __instance = None
    SET_URL = "/set_internal"
    DELET_URL = "/delete_internal"
    FETCHALL_URL = "/fetchall"

    @staticmethod 
    def getInstance(config):
      if cacheService.__instance == None:
         cacheService(config)
      return cacheService.__instance

    @staticmethod
    def fetchInstance():
        return cacheService.__instance

    def __init__(self, config):
      if cacheService.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         self.cacheStore = LRUCache()
         servers = config["SERVERS"]
         self.serverList = {}
         numer_of_node = config["NUMBER_OF_NODES"]
         for server in servers:
             if server["name"] != config["CURRENT_SERVER"]:
                 setUrl = "http://"+server["HOST"]+":"+server["PORT"]+self.SET_URL
                 deleteUrl = "http://"+server["HOST"]+":"+server["PORT"]+self.DELET_URL
                 fetchAllUrl = "http://"+server["HOST"]+":"+server["PORT"]+ self.FETCHALL_URL
                 self.serverList[server["name"]] = {"setUrl": setUrl, "deleteUrl": deleteUrl, "fetchAllUrl": fetchAllUrl}
                 numer_of_node = numer_of_node - 1
                 if numer_of_node == 0:
                     break
        
         self.setupInitialData(config)

         print(self.serverList)
         self.faliureQueue = []
         cacheService.__instance = self

    def setupInitialData(self, config):
         for server in self.serverList:
            if server != config["CURRENT_SERVER"]:
                try:
                    resp = requests.post(self.serverList[server]["fetchAllUrl"])
                    if resp.status_code and resp.status_code== 200:
                        json_data = resp.json()
                        found = False
                        for key in json_data:
                            self.setData(key, json_data[key], False)
                            found = True
                    
                        if found:
                            return
                except Exception:
                    pass



    def fetchData(self , key):
        return self.cacheStore.get(key)

    def setData(self, key , value, callOtherCache):
        try:
            response = self.cacheStore.put(key, value)
            print(response, callOtherCache)
            if response == True and callOtherCache == True:
                response = self.saveDataInOtherCache(key, value)
            return response
        except  Exception as e:
            print("exception raised in delete data", e)
            return False

    def saveDataInOtherCache(self, key, value):

        params = {"key":key,"value":value}
        for server in self.serverList:
            try:
                operationFailed = False
                print("calling another cache", self.serverList[server]["setUrl"], key, value)
                resp = requests.post(self.serverList[server]["setUrl"], json=params)
                print("response:", resp.status_code)

                if not resp.status_code:
                    operationFailed = True
                else:
                    if resp.status_code != 200:
                       operationFailed = True

                if operationFailed == True:
                    qEntry = faliureQueue(operations.SET, server["name"], params)
                    self.faliureQueue.push(qEntry)

            except  Exception as e:
                print("exception raised in setting data to cache server", e)
                operationFailed = False

        if operationFailed == True:
            return False
        return True

    
    def deleteData(self, key , callOtherCache):
        response = self.cacheStore.delete(key)
        print("on delete", response, callOtherCache)
        if callOtherCache == True:
            response = self.removeDataInOtheCase(key)
        return response


    def removeDataInOtheCase(self, key):

        params = {"key":key}
        for server in self.serverList:
            try:
                operationFailed = False
                resp = requests.post(self.serverList[server]["deleteUrl"], json=params)
                print("response from other cache", resp.status_code)
                if not resp.status_code:
                    # operation failed
                    operationFailed = True
                else:
                    if resp.status_code != 200:
                       operationFailed = True
                if operationFailed == True:
                    qEntry = faliureQueue(operations.DELETE, server["name"], params)
                    self.faliureQueue.push(qEntry)

            except  Exception as e:
                print("exception raised in delete data", e)
                operationFailed = False

        if operationFailed == True:
            return False
        return True

    def fetchall(self):
        return self.cacheStore.fetchall()
