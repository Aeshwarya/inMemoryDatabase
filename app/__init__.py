import os
from flask import Flask

def create_app(config=None, servername="server1"):

    from . import models, controllers, services, store, cacheConfig, Managers
    from app.Managers import cacheManager
    app = Flask(__name__)
    app.config.from_object('app.settings')
    if 'FLASK_CONF' in os.environ:
        app.config.from_envvar('FLASK_CONF')
    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith('.py'):
            app.config.from_pyfile(config)

    server_config = {}
    server_config["NUMBER_OF_NODES"] = cacheConfig.NUMBER_OF_NODES
    server_config["SERVERS"] = cacheConfig.SERVERS
    server_config["CURRENT_SERVER"] = servername
    controllers.init_app(app , server_config)
    models.init_app(app)
    services.init_app(app)
    Managers.init_app(server_config)

    return app
