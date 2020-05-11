import os
from flask import Flask

def create_app(config=None):
    from . import models, controllers, services
    app = Flask(__name__)

    app.config.from_object('app.settings')

    if 'FLASK_CONF' in os.environ:
        app.config.from_envvar('FLASK_CONF')
    
    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith('.py'):
            app.config.from_pyfile(config)

    models.init_app(app)
    controllers.init_app(app)
    services.init_app(app)
    return app
