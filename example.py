from Fly_Coco import Calculate
from models import CalculateModel, SteelGrade


calculate = Calculate(
    cmd=CalculateModel(
        name="1234",
        steel_grade=SteelGrade.DOPED,
    )
)
