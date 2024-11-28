import typing
from services.temporary_resistance.service import Calculate
from models.schema import models_class

class TemporaryResistanceCalculateWrapper:
    __temporary_resistance_calculate_service: Calculate

    def __init__(
        self,
        name: str,
        steel_grade: str,
        brand: str,
        breaking_force: typing.List[float],
        thickness_initial_plate: int,
        sample_thickness: int,
        width_thickness: int,

    ):
        self.__temporary_resistance_calculate_service = Calculate(
            cmd = models_class.CalculateModel(
                name=name,
                steel_grade=steel_grade,
                brand=brand,
                breaking_force=breaking_force,
                thickness_initial_plate=thickness_initial_plate,
                sample_thickness=sample_thickness,
                width_thickness=width_thickness,

            )
        )
        # def execute

    def execute(
        self,

    ):
        return self.__temporary_resistance_calculate_service.sorting()
