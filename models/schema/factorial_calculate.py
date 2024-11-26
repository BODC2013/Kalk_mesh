import typing

import pydantic
import typing


__all__ = [
    "FactorialCalculateCommand",
    "FactorialCalculateResponse",
]


class BaseFactorialModel(pydantic.BaseModel):
    """Base factorial model."""
    pass


class FactorialCalculateCommand(BaseFactorialModel):
    """Command to create factorial."""
    calculate_value: int


class FactorialCalculateResponse(BaseFactorialModel):
    """Response calculate model."""
    calculate_value: pydantic.PositiveInt
    traceback: typing.List
