from fastapi import FastAPI
from routers.router_models import RouterContainer

# Управление и создание приложения FastAPI, регистрация маршрутизаторов
class Server:
    # !!!!как работает debug???? зачем
    debug = True
    def __init__(self):
        # метод создает и возвращает экземпляр приложения FastAPI и результат сохраняется в приватном атрибуте __app
        self.__app = self.__create_app()
        # регистрация роутеров в приложении
        self.register_router()

    # метод создает и возвращает экземпляр приложения FastAPI
    def __create_app(self) -> FastAPI:
        """сюда можно добавлять кастомные хендлеры"""
        # параметр debug устанавливает значение атрибута debug  класса server
        return FastAPI(
            debug=self.debug
        )
    # регистрация маршрутизаторов в приложении
    # Вызывает метод save_router класса RouterContainer передавая ему экземпляр приложения _app
    def register_router(self):
        RouterContainer.save_router(app=self.__app)

    # этот метод возвращает экземпляр приложения FastAPI, сохраненный в приватном атрибуте _app
    def get_app(self):
        return self.__app
