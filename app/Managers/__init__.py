from ..services.cacheService import cacheService

def init_app(config):
    cacheService.getInstance(config)
