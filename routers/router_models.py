from fastapi import FastAPI
from routers import factorial
from routers import temporary_resistanse
__all__ = [
    "RouterContainer",
]


class RouterContainer:
    #список маршрутизаторов
    __router__ = [
        factorial.router,
        temporary_resistanse.router,
    ]

    @staticmethod
    def save_router(app: FastAPI):
        for router in RouterContainer.__router__:
            app.include_router(router)

#   @staticmethod принимает экземпляр приложения FasApi в качестве аргумента
#   def save_router(app: FastAPI):
#       for router in RouterContainer.__router__: в дальнейшем суда импортируется _app из server.py
#           app.include_router(router)      Метод проходит по всем маршрутизаторам и регистрирует их