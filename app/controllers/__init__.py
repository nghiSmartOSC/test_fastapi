from app.controllers.accounts.user import router as user_router

class RouterConf:
    def __init__(self, route, prefix):
        self.route = route
        self.prefix = prefix


routers = [
    RouterConf(user_router, "/api/v1/user"),
]