"""
A class Person that makes use methods, attributes, 
polymorphism and encapsulation
"""
class Person(object):
    """Class person implementation"""
    pay = 50000
    def __init__(self, first="Jim", last="Jam", gender="Female"):
        """Class constructor"""
        self.first = first
        self.last = last
        self.gender = gender
        self.email = '{}_{}@gmail.com'.format(self.first, self.last).lower()

    def full_name(self):
        """A method that returns persons fullname"""
        return 'I am ' + self.first + " " + self.last
        pass

    def is_female(self):
    	"""A method returns true if gender is female"""
    	if self.gender not in ["Female", "F", "f"]:
    		return False
    	return True

    def set_age(self, age=0):
    	"""A method that demonstrates polymorphism"""
    	self.age = age
    	return self.age

    def __keep_happy(self):
    	"""A method that demonstrates encapsulation"""
    	print('Keep happy and calm')

    



       