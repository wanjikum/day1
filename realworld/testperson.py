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
        """Test if the persons email is generated using the first and the last name"""
        paul = Person('Paul', 'Othis')
        self.assertEqual('paul_othis@gmail.com', paul.email)

    def test_if_a_person_name_is_correct(self):
        """Test if the person name comprised of the first name and second name"""
        paul = Person('Paul', 'Othis')
        self.assertEqual('I am Paul Othis', paul.full_name())

    def test_if_it_outputs_correct_gender(self):
        """Test if it returns true if persons gender is female"""
        step = Person('steph', 'wafula', 'F')
        self.assertTrue(step.is_female())

    def test_age_data_can_be_set(self):
        """Test if it sets the age to 40 and accepts datatype int"""
        fatuma = Person()
        self.assertEqual(40, fatuma.set_age(40))

    def test_age_data_can_be_set(self):
        """Test if it sets the age to 40 and accepts datatype string"""
        fatuma = Person()
        self.assertEqual('forty', fatuma.set_age('forty'))

    def test_if_pay_is_an_attribute(self):
    	"""Tests if the attribute default value is 50000"""
    	jane = Person()
    	self.assertEqual(50000, jane.pay)












