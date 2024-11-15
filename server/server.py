from fastapi import FastAPI
from routers.router_models import RouterContainer

class Server:
    debug = True
    def __init__(self):
        self.__app = self.__create_app()
        self.register_router()

    def __create_app(self) -> FastAPI:
        """сюда можно добавлять кастомные хендлеры"""
        return FastAPI(
            debug=self.debug
        )

    def register_router(self):
        RouterContainer.save_router(app=self.__app)

    def get_app(self):
        return self.__app
