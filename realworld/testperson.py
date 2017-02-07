"""A collection of class Person tests"""
import unittest
from person import Person
class PersonClassTest(unittest.TestCase):
	"""Person class tests implementations"""
	def test_person_instance(self):
		"""Tests if the object is an instance of class `Person`"""
		man = Person('larry')
		self.assertIsInstance(man, Person)

	def test_person_object_type(self):
		"""Tests if the object should be a type of `Person`"""
		man = Person('larry')
		self.assertIsTrue((type(man) is Person), Person)




