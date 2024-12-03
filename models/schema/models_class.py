from pydantic import BaseModel
from enum import Enum
import typing

## Здесь происходит создание моделей для ввода данных и модели которые приходят из роутера
# при использовании инструкции from module import
# ни один из элементов модуля не будет экспортирован
__all__ = [

]
# Модель ввода данных для марки стали
class SteelGrade(Enum):
    DOPED = '09Г2С'
    NODOPED = 'СT3'
# Создание модели
# модель CalculateModel наследуется от BaseModel
class CalculateModel(BaseModel):
    name: str = "1235"
    steel_grade: SteelGrade
    brand: str
    breaking_force: typing.List[float]
    thickness_initial_plate: float = 8.0
    sample_thickness: float = 8.0
    width_thickness: float = 20.0

## модель TestModel наследуется от BaseModel
class TestModel(BaseModel):
    name: str = "12356"
    steel_grade: str
    brand: str
    breaking_force:  typing.Optional[typing.List[float]] = None
    thickness_initial_plate: float = 8.0
    sample_thickness: float = 8.0
    width_thickness: float = 20.0

# !!!Модель ответа которая придет из temporary_resistanse_router????
# !!!!или из service???????
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