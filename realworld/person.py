"""
A class Person that makes use methods, attributes, 
polymorphism and encapsulation
"""
class Person(object):
    """Class person implementation"""
    def __init__(self, first="Jim", last="Jam", gender="Female"):
        """Class constructor"""
        self.first = first
        self.last = last
        self.gender = gender
        self.email = '{}_{}@gmail.com'.format(self.first, self.last).lower()

    def full_name(self):
        """A method that returns persons fullname"""
        pass

    def is_female(self):
    	"""A method that returns true if the persons gender is female"""
    	pass

       