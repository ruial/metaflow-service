import os
from services.utils import handle_exceptions, web_response

from ..features import get_features


class FeaturesApi(object):
    def __init__(self, app):
        app.router.add_route("GET", "/features", self.get_all_features)

    @handle_exceptions
    async def get_all_features(self, request):
        return web_response(200, get_features())
