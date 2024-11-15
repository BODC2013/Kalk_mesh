from typing import List
from models.schema import factorial_calculate


class FactorialService:

    traceback: List = []

    def calculate_factorial(
        self,
        cmd: factorial_calculate.FactorialCalculateCommand,
        value: int = 1
    ) -> int:

        value = cmd.calculate_value*(cmd.calculate_value-1)*value

        self.traceback.append(value)
        if cmd.calculate_value - 1 > 1:
            return self.calculate_factorial(
                cmd=factorial_calculate.FactorialCalculateCommand(
                    calculate_value=cmd.calculate_value-1
                ),
                value=value,
            )
        else:
            return value

