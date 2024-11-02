from fastapi import FastAPI



class Server:

    def ___init__(self, app: FastAPI):
        self.__app = app

    def __call__(self):
        return self.__app

    @staticmethod
    def register_routes(self):
        """Register new routes."""
        pass

    @staticmethod
    def register_middleware(self):
        """Register middleware."""

    @staticmethod
    def register_event(self):
        """Register on startup event."""

