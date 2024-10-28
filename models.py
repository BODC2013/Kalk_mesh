from pydantic import BaseModel
from enum import Enum
from typing import List, Optional


class SteelGrade(Enum):

   DOPED = '09Г2С'
   NODOPED = 'Ст3'


class CalculateModel(BaseModel):
    name: str = "1235"
    steel_grade: str
    brand: str
    breaking_force: List[float]
    thickness_initial_plate: float = 8.0
    sample_thickness: float = 8.0
    width_thickness: float = 20.0
#     ne_obyzatelno: Optional[int]

class TestModel(BaseModel):
    name: str = "12356"
    steel_grade: str
    brand: str
    breaking_force:  Optional[List[float]] = None
    thickness_initial_plate: float = 8.0
    sample_thickness: float = 8.0
    width_thickness: float = 20.0