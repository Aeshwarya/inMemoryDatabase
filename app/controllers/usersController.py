from flask import Flask, make_response, Blueprint, current_app, jsonify, request

CacheController = Blueprint('cache_controller', __name__)
cacheService = CacheService(current_app)

@UsersController.route("/set", methods=['POST'])
def set_data():
    data = request.get_json()
    response = cacheService.setData(data["key"] , data["value"], False)
    if response == True:
        response["message"] = "cache updated"
        response["status"] = 200
    else:
        response["error"] = "some error occured"
        response["status"] = 400
    return make_response(jsonify(response), response["status"])


@UsersController.route("/delete", methods=['POST'])
def delete_data():
    data = request.get_json()
    response = cacheService.deleteData(data["key"] , False)
    if response == True:
        response["message"] = "cache updated"
        response["status"] = 200
    else:
        response["error"] = "some error occured"
        response["status"] = 400 

    return make_response(jsonify(response), response["status"])

