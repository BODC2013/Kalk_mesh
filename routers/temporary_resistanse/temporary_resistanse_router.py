from fastapi import APIRouter, status
from models.schema import models_class
from services.temporary_resistance.temporary_resistanse_calculate_wrapper import TemporaryResistanceCalculateWrapper


__all__ = [
    "router",
]


router = APIRouter(prefix="/temporary_resistance", tags=["Temporary Resistance"])

@router.post(
    path="",
    status_code=status.HTTP_200_OK,
    description="Temporary Resistance.",
    response_model=models_class.ResponseCalculateModel
)
def calculate_temporary_resistance(
    cmd:models_class.CalculateModel
) ->models_class.ResponseCalculateModel:
    wrapper = TemporaryResistanceCalculateWrapper(**cmd.model_dump())
    print(f"Cmd: {cmd.model_dump()}")
    return wrapper.execute()
