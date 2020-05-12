from flask import Flask, make_response, Blueprint, current_app, jsonify, request
from ..services.cacheService import cacheService

CacheController = Blueprint('cache_controller', __name__)

@CacheController.route("/set_internal", methods=['POST'])
def set_data_intenal():
    resp = {}
    try:
        print(request)
        data = request.get_json()
        print("setting data")
        print(data)
        if "key" not in data or data["key"] == None  or "value" not in data or data["value"] == None:
            return {"Error": "Invalid key value pair", "status":"404"}
        response = cacheService.fetchInstance().setData(data["key"], data["value"], False)
        if response == True:
            resp["message"] = "cache updated"
            resp["status"] = 200
        else:
            resp["error"] = "some error occured"
            resp["status"] = 400
    except:
        resp["error"] = "some error occured"
        resp["status"] = 400
    return make_response(jsonify(resp), resp["status"])

@CacheController.route("/set", methods=['POST'])
def set_data():
    resp = {}
    try:
        print(request)
        data = request.get_json()
        print("setting data")
        print(data)
        if "key" not in data or data["key"] == None  or "value" not in data or data["value"] == None:
            return {"Error": "Invalid key value pair", "status":"404"}
        response = cacheService.fetchInstance().setData(data["key"] , data["value"], True)
        if response == True:
            resp["message"] = "cache updated"
            resp["status"] = 200
        else:
            resp["error"] = "some error occured"
            resp["status"] = 400
    except:
        resp["error"] = "some error occured"
        resp["status"] = 400
    return make_response(jsonify(resp), resp["status"])


@CacheController.route("/delete_internal", methods=['POST'])
def delete_data_internal():
    print(request)
    data = request.get_json()
    print("deleting data")
    print(data)
    resp = {}
    try:
        if "key" not in data or data["key"] == None:
            return {"Error": "Invalid key", "status":"404"}
        response = cacheService.fetchInstance().deleteData(data["key"], False)
        if response == True:
            resp["message"] = "cache updated"
            resp["status"] = 200
        else:
            resp["error"] = "some error occurred"
            resp["status"] = 400
    except:
        resp["error"] = "some error occurred"
        resp["status"] = 400
    return make_response(jsonify(resp), resp["status"])


@CacheController.route("/expire", methods=['POST'])
def delete_data():
    print(request)
    data = request.get_json()
    print("deleting data")
    print(data)
    resp = {}
    try:
        if "key" not in data or data["key"] == None:
            return {"Error": "Invalid key", "status": "404"}
        response = cacheService.fetchInstance().deleteData(data["key"], True)
        if response == True:
            resp["message"] = "data deleted"
            resp["status"] = 200
        else:
            resp["error"] = "some error occurred"
            resp["status"] = 400
    except:
        resp["error"] = "some error occurred"
        resp["status"] = 400
    return make_response(jsonify(resp), resp["status"])


@CacheController.route("/get", methods=['POST'])
def get():
    print(request)
    data = request.get_json()
    print("fetching data")
    print(data)
    resp = {}
    try:
        if "key" not in data or data["key"] == None:
            return {"Error": "Invalid key", "status":"404"}
        response = cacheService.fetchInstance().fetchData(data["key"])
        print("get response", response)
        if response != None:
            return make_response(jsonify(response), 200)
        else:
            resp["error"] = "some error occured"
            resp["status"] = 400
    except:
        resp["error"] = "some error occured"
        resp["status"] = 400

    return make_response(jsonify(resp), resp["status"])


@CacheController.route("/fetchall", methods=['POST'])
def fetch_data():
    try:
        print("fetching all data")
        response = cacheService.fetchInstance().fetchall()
        return make_response(jsonify(response), 200)
    except:
        return make_response(jsonify({"Error":"some error occured"}), 404)

