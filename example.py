from unittest import TestProgram
#from Fly_Coco import Calculate
from Fly_Coco import Test
from models import CalculateModel, TestModel


#calculate = Calculate(
#     cmd=CalculateModel(
#         name="1234",
#         steel_grade='09г2с',
#         brand="Бе",
#         breaking_force=[100, 100, 100]
#     )
#)
test = Test(
    cmd=TestModel(
        name="1234",
        steel_grade='09г2с',
        brand="Бе",
            )
)
