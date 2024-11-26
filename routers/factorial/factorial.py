from fastapi import APIRouter, status
from services.factorial_service import FactorialServiceWrapper
from models.schema import factorial_calculate

__all__ = [
    "router",
]
router = APIRouter(prefix="/factorial", tags=["Test router special for you"])


@router.post(
    path="",
    status_code=status.HTTP_200_OK,
    description="Calculate factorial.",
    response_model=factorial_calculate.FactorialCalculateResponse,
)
def calculate_factorial(
    cmd: factorial_calculate.FactorialCalculateCommand,

) -> factorial_calculate.FactorialCalculateResponse:

    wrapper = FactorialServiceWrapper()
    print(f"Cmd: {cmd}")
    return wrapper.execute (cmd=cmd)
