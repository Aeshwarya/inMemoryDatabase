from app import create_app
import os
import config
from app import cacheConfig
import sys

def start(port, server_name):
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    numer_of_server = cacheConfig.NUMBER_OF_NODES
    count = 1
    servers = cacheConfig.SERVERS
    #port = int(input())
    #name = input()

    name = server_name

    print(port)
    print(name)
    application=create_app(os.path.join(BASE_DIR, 'config.py'), name)
    application.run(host="127.0.0.1", port=port, debug=True)

if __name__ == "__main__":
    port  = sys.argv[1]
    server_name = sys.argv[2]
    start(port, server_name)