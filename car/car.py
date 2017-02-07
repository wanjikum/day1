"""Andelab Car Assignment"""
class Car(object):
    """Collection of methods of class car"""
    def __init__(self, car_type, model = "GM", car_name = "General"):
        self.car_type = car_type
        self.model = model
        self.name = car_name

        if self.name in ['Porshe', 'Koenigsegg']:
            self.num_of_doors = 4
        else:
            self.num_of_doors = 2

        if self.car_type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4






