from arteria.web.app import AppService
from template.handlers import EchoHandler


def start():
    app_svc = AppService.create(__package__)

    # Setup the routing. Help will be automatically available at /api, and will
    # be based on the doc strings of the get/post/put/delete methods
    args = dict(config_svc=app_svc.config_svc)
    routes = [
        (r"/api/1.0/echo/([\w_-]+)", EchoHandler, args)
    ]
    app_svc.start(routes)
