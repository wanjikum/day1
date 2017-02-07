"""
A class Manager that demonstrates use of inheritance,
class methods and static methods
"""
from person import Person

class Manager(Person):
    pay = 200000
    def __init__(self, first = "jim", last="jam", gender="Female", projects=None):
        """A constructor of class Manager"""
        Person.__init__(self, first, last, gender)
        self.projects = projects
        if self.projects == None:
        	return None
        else:
        	self.projects = projects

    @classmethod
    def set_pay(cls, amount):
    	"""An example of a class method"""
    	cls.pay = amount
    	return cls.pay

    @staticmethod
    def is_working_day(day):
    	"""An example of a static method"""
    	if day.weekday() == 5 or day.weekday() == 6:
    		return False
    	return True



