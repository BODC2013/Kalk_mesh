from pydantic import BaseModel
from enum import Enum
import typing
import pydantic

__all__ = [

]



class CalculateModel(BaseModel):
    name: str = "1235"
    steel_grade: str
    brand: str
    breaking_force: typing.List[float]
    thickness_initial_plate: float = 8.0
    sample_thickness: float = 8.0
    width_thickness: float = 20.0
#     ne_obyzatelno: Optional[int]

class TestModel(BaseModel):
    name: str = "12356"
    steel_grade: str
    brand: str
    breaking_force:  typing.Optional[typing.List[float]] = None
    thickness_initial_plate: float = 8.0
    sample_thickness: float = 8.0
    width_thickness: float = 20.0


class ResponseCalculateModel(BaseModel):
    name: str
    steel_grade: str
    brand: str
    breaking_force: typing.List[float]
    thickness_initial_plate: float
    sample_thickness: float
    width_thickness: float
    temporary_resistance: typing.List[float]
    bend_angle :float