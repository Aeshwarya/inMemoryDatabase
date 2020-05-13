import app.cacheConfig as cacheConfig
import requests

server_config = {}
server_config["NUMBER_OF_NODES"] = cacheConfig.NUMBER_OF_NODES
server_config["SERVERS"] = cacheConfig.SERVERS
server_config["CURRENT_SERVER"] = "server1"
base_url = "http://0.0.0.0:"
server_set_url = "/set"
server_del_url = "/expire"
server_get_url = "/get"
while(True):
    port= input("Port:")
    operation = input("Operation: ")
    if operation == "SET":
        key = input("enter key :")
        value = input("enter value :")
        params = {"key": key, "value": value}
        resp = requests.post(base_url+port+server_set_url, json=params)
        print("response:", resp.status_code, resp.json())
    elif operation == "GET":
        key = input("enter key :")
        params = {"key": key}
        resp = requests.post(base_url+port+server_get_url, json=params)
        print("response:", resp.json())
    elif operation == "DELETE":
        key = input("enter key :")
        params = {"key": key}
        resp = requests.post(base_url+port+server_del_url, json=params)
        print("response:", resp.status_code)
    else:
        print("invalid operation")
