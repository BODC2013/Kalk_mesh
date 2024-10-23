from pydantic import BaseModel

class Roll(BaseModel):
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