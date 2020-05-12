from .cacheController import CacheController
from ..services.cacheService import cacheService

def init_app(app , config):
    cacheService.getInstance(config)
    app.register_blueprint(CacheController)

