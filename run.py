from app import create_app
import os
import config
from app import cacheConfig
import sys

def start(port, server_name):
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    application=create_app(os.path.join(BASE_DIR, 'config.py'), server_name)
    application.run(host="127.0.0.1", port=port, debug=True)

if __name__ == "__main__":
    port  = sys.argv[1]
    server_name = sys.argv[2]
    start(port, server_name)