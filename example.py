from unittest import TestProgram
from services.temporary_resistance.service import Calculate
from services.temporary_resistance.service import Test
from models import schema


calculate = Calculate(
    cmd=schema.models_class.CalculateModel(
        name="1234",
        steel_grade='09г2с',
        brand="Бе",
        breaking_force=[100, 100, 100]
    )
)
test = Test(
    cmd=schema.models_class.TestModel(
        name="124",
        steel_grade='09г2с',
        brand="Бе",
            )
)