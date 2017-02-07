"""Andelab Car Assignment"""
class Car(object):
    """Collection of methods of class car"""
    def __init__(self, car_name="General", model="GM", car_type="saloon"):
        """Intialising car class"""
        self.car_type = car_type
        self.model = model
        self.name = car_name
        self.speed = 0

        if self.name == 'Porshe' or self.name == 'Koenigsegg':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        if self.car_type != "saloon":
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4

    def is_saloon(self):
        """The car type should be saloon if it is not a trailer"""
        if self.car_type == 'trailer':
            return False
        else:
            return True

    def drive(self, speed):
        """The car_type should have speed 0 km/h until you put
        `the pedal to the metal"""
        if self.car_type != 'trailer':
            if speed != 0:
                speeds = 10 ** speed #10**3 = 1000
            self.speed = speeds
            return self
        else:
            self.speed = 11 * speed # 11*7
            return self











