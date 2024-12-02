from fastapi import APIRouter, status
from models.schema import models_class
from models.schema.models_class import CalculateModel
from services.temporary_resistance.temporary_resistanse_calculate_wrapper import TemporaryResistanceCalculateWrapper

#Конструкция __all__ позволяет вам явно указать,
# какие элементы модуля должны быть доступны при
# импорте всех элементов, что может быть полезно
# для управления доступом к внутренним деталям модуля
# и предотвращения непреднамеренного использования внутренних функций или классов.
__all__ = [
    "router",
]
##Создание маршрутизатора, все параметры добавленные через него будут
# иметь рефикс /temporary_resistanse

router = APIRouter(prefix="/temporary_resistance", tags=["Temporary Resistance"])

# определение HTTP-POST запросов
@router.post(
    path="",
    status_code=status.HTTP_200_OK,

    description="Temporary Resistance.",
    response_model=models_class.ResponseCalculateModel
)
# path="",    Это путь для обращения
# status_code=status.HTTP_200_OK, Напишет в свагере при удачном выполнении
# description="Temporary Resistance.",   Название раздела, который   отразится в Swagger
# response_model=models_class.ResponseCalculateModel   Модель ответа которая будет использована


## Здесь определяется функция, которая принимается в качестве аргумента и возвращяется другая функция.

def calculate_temporary_resistance(
    cmd:models_class.CalculateModel
) ->models_class.ResponseCalculateModel:
    wrapper = TemporaryResistanceCalculateWrapper(**cmd.model_dump())
    print(f"Cmd: {cmd.model_dump()}")
    return wrapper.execute()

# def calculate_temporary_resistance (          определяет ф -ю с именем calculate_temporary_resistance
#     cmd:models_class.CalculateModel           указывает что ф-я принимает аргумент cmd, который должен быть экземпляром
#                                               CalculateModel  из модуля model_class
# ) ->models_class.ResponseCalculateModel:      возвращяет обЪект модели ResponseCalculateModel из модуля model_class
#     wrapper = TemporaryResistanceCalculateWrapper(**cmd.model_dump())     Этот класс принимает параметры для инициализации
#                                                                           (** cmd.model_dump() возвращает словарь с данными модели.
#                                                                             ** позволяет передать ключи и значения в качестве именованных аргументов
#     print(f"Cmd: {cmd.model_dump()}") выводит на печать данные модели в формате словаря
#     return wrapper.execute()  Вызов метода execute у обЪекта wrapper и возврат модели соответствующей ResponseCalculateModel

