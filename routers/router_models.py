from fastapi import FastAPI
from routers import factorial
__all__ = [
    "RouterContainer",
]


class RouterContainer:

    __router__ = [
        factorial.router,
    ]

    @staticmethod
    def save_router(app: FastAPI):
        for router in RouterContainer.__router__:
            app.include_router(router)
