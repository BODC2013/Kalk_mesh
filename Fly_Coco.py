from enum import Enum
from typing import List
from random import randrange
from models import CalculateModel
#class SteelGrade(Enum):
#    DOPED = '09Г2С'
#    NODOPED = 'Ст3'

class Calculate:
    bend_angle_doped = 120
    temporary_resistance_standart_doped = {
        (0, 10): [[490, 1000]], (11, 20): [[470, 1000]], (21, 32): [[460, 1000]],
        (33, 60): [[450, 1000]], (61, 80): [[440, 1000]], (81, 160): [[430, 1000]]}

    bend_angle_NOdoped = 80
    temporary_resistance_standart_NOdoped = {
        (0, 10): [[380, 490]], (11, 20): [[370, 480]],
        (21, 40): [[370, 480]], (41, 100): [[370, 480]]}

    bend_angle: int

    def __init__(self, cmd: CalculateModel):
        self.name = cmd.name
        self.steel_grade = cmd.steel_grade
        self.brand = cmd.brand
        self.breaking_force = cmd.breaking_force
        self.thickness_initial_plate = cmd.thickness_initial_plate
        self.sample_thickness = cmd.sample_thickness
        self.width_thickness = cmd.width_thickness
        self.temporary_resistance = []
        self.value_calculator()
        self.sorting()
        self.res_calculation = {}

    def value_calculator(self):
        for i in self.breaking_force:
            results = (i / (self.sample_thickness * self.width_thickness) * 1000)
            self.temporary_resistance.append(round(results, 2))

#        print("Значение временного сопротивления:", self.temporary_resistance)

    def sorting(self):
        if self.steel_grade.upper() == '09Г2С':
            standard_resistance = self.temporary_resistance_standart_doped.copy()
            self.bend_angle = self.bend_angle_doped
        elif self.steel_grade.upper() == 'СТ3':
            standard_resistance = self.temporary_resistance_standart_NOdoped.copy()
            self.bend_angle = self.bend_angle_NOdoped
        else:
            print('Введите корректную марку стали или обновите справочник')
            raise ValueError

        for thickness_range in standard_resistance.keys():
            if thickness_range[0] <= self.thickness_initial_plate <= thickness_range[1]:
                for i in standard_resistance[(thickness_range)]:
                    for temp in self.temporary_resistance:
                        if i[0] <= temp <= i[1]:
                            print('Значение', temp, 'соответствует ГОСТу')
                        else:

                            print('Значение', temp, 'НЕ СООТВЕТСТВУЕТ ГОСТу')


       # print('угол загиба ', self.bend_angle, 'градусов')
        self.res_calculation = {'Имя': self.name, 'Марка стали': self.steel_grade,
                                'Клейио':self.brand,'Толщина исходной пластины':self.thickness_initial_plate,
                                'Толщина образца': self.sample_thickness, 'Ширина образца': self.width_thickness
                                ,'Разрушающее усилие':self.breaking_force, 'Предел прочности': self.temporary_resistance,
                                'Угол загиба в градусах': self.bend_angle}
        print(self.res_calculation)

class Test:
    range_doped = {
        (0, 10): [[495, 520]], (11, 20): [[475, 500]], (21, 32): [[465, 490]],
        (33, 60): [[455, 480]], (61, 80): [[445, 470]], (81, 160): [[435, 460]]
    }
    range_NOdoped = {(0, 10): [[385, 489]], (11, 100): [[375, 478]]}

    def __init__ (self, name: str, steel_grade: str, brand: str, thickness_initial_plate= 8, sample_thickness = 8, width_thickness= 20):
        self.name = name
        self.steel_grade = steel_grade
        self.brand = brand
        self.thickness_initial_plate = thickness_initial_plate
        self.range_test = {}
        self.range_values_test = []
        self.breaking_force = []
        self.sample_thickness = sample_thickness
        self.width_thickness = width_thickness
        self.meaning_calculate()

    def meaning_calculate(self):
        if self.steel_grade.upper() == '09Г2С':
            self.range_test = self.range_doped
        elif self.steel_grade.upper () == 'СТ3':
            self.range_test = self.range_NOdoped
        else:
            print('Введите корректную марку стали')
            return

        for range_selection in self.range_test.keys():
            if range_selection[0] <= self.thickness_initial_plate <= range_selection[1]:
                self.range_values_test = self.range_test[range_selection][0]
#                print('Тестовое значение', 'толщины стали', 'принято в расчет')
                break
        else:
            print('Толщина образца', 'не соответствует ГОСТу(Test)')
            return

        i = [randrange(self.range_values_test[0] , self.range_values_test[1])
             for _ in range(3)]
        self.breaking_force = [round(value / 1000 * self.thickness_initial_plate * self.width_thickness, 1) for value in i]
#        print(self.breaking_force)



        test_job = Calculate(self.name, self.steel_grade, self.brand, self.breaking_force)
        return test_job

root= Test('aнтон', 'ст3', 'Чё', )
#low= Calculate(name='Пупс', steel_grade='09Г2С', brand='Бе', breaking_force=[100, 100, 100])
