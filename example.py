from Fly_Coco import Calculate

from models import CalculateModel




calculate = Calculate(
    cmd=CalculateModel(
        name="1234",
        steel_grade='09г2с',
        brand="Бе",
        breaking_force=[100, 100, 100]
    )
)
