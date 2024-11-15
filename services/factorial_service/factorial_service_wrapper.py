from services.factorial_service.service import FactorialService
from models.schema import factorial_calculate

__all__ = [
    "FactorialServiceWrapper"
]


class FactorialServiceWrapper:

    __factorial_service:  FactorialService

    def __init__(
        self
    ):
        self.__factorial_service: FactorialService = FactorialService()
        print(f"type after init {type(self.__factorial_service)}")

    def pipeline(
        self,
        cmd: factorial_calculate.FactorialCalculateCommand
    ) -> factorial_calculate.FactorialCalculateResponse:
        result = self.__factorial_service.calculate_factorial(cmd=cmd)
        print(f"result: {result}")
        print(f"cmd: {cmd}")
        return factorial_calculate.FactorialCalculateResponse(
            calculate_value=result,
            traceback=self.__factorial_service.traceback,
        )
