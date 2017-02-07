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
		self.assertTrue((type(man) is Person), Person)

	def test_default_first_and_second_name(self):
		"""Tests if the default first and last name is jim jam"""
		woman = Person()
		self.assertListEqual(['Jim','Jam'], [woman.first, woman.last])

	def test_default_gender(self):
		"""Tests if the default gender is female"""
		jane = Person()
		self.assertEqual('Female', jane.gender)

	def test_objects_email(self):
		"""Test if the persons email is generated automatically"""
		paul = Person('Paul', 'Othis')
		self.assertEqual('paul_othis@gmail.com', paul.email)
		




