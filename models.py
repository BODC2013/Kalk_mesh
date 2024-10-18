from pydantic import BaseModel
from enum import Enum
from typing import List, Optional


class SteelGrade(Enum):
   DOPED = '09Г2С'
   NODOPED = 'Ст3'


class CalculateModel(BaseModel):
    name: str = "1235"
    steel_grade: SteelGrade
    brand: str
    breaking_force: List[float]
    thickness_initial_plate: int
    sample_thickness: int
    width_thickness: int
    ne_obyzatelno: Optional[int]
