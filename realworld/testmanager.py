"""
A class Manager that demonstrates use of inheritance,
class methods and static methods
"""

import unittest
import datetime
from manager import Manager
from person import Person

class TestClassManager(unittest.TestCase):
    """A collection of class Manager testscases """
    def test_person_instance(self):
        """Tests if the object is an instance of class `Person`"""
        man = Manager('larry')
        self.assertIsInstance(man, Person)

    def test_is_instance_manager(self):
        """Tests if man is an instance of `Manager`"""
        man = Manager('larry')
        self.assertIsInstance(man, Manager)

    def test_object_type_is_a_type_of_manager(self):
        """Tests if the object is of type `Manager`"""
        woman = Manager()
        self.assertTrue((type(man) is Manager))

    def test_object_type_is_a_type_of_manager(self):
        """Tests if the object is of type `Person`"""
        man = Manager()
        self.assertFalse((type(man) is Person))

    def test_default_gender(self):
        """Tests if the default gender is female"""
        jane = Manager()
        self.assertEqual('Female', jane.gender)

    def test_objects_email(self):
        """Test if the persons email is generated using the first and the last name"""
        paul = Manager('Paul', 'Othis')
        self.assertEqual('paul_othis@gmail.com', paul.email)

    def test_if_a_person_name_is_correct(self):
        """Test if the person name comprises of the first name and second name"""
        paul = Person('Paul', 'Othis')
        self.assertEqual('I am Paul Othis', paul.full_name())

    def test_if_it_outputs_correct_gender(self):
        """Test if it returns true if persons gender is female"""
        step = Person('steph', 'wafula', 'F')
        self.assertTrue(step.is_female())

    def test_default_pay(self):
    	"""Tests if the default pay is 200000"""
        alice = Manager()
        self.assertListEqual([alice.pay], [200000])

    def test_if_pay_can_be_set_to_the_desired_pay(self):
        """Test if it sets the pay to 200100 and accepts datatype int"""
        fatuma = Manager()
        self.assertEqual(200100, fatuma.set_pay(200100))

    def test_if_the_day_is_a_weekday_or_not(self):
    	"""Tests if a day is a working day or not"""
    	vicky = Manager()
    	my_date = datetime.date(2017, 3, 21)
    	self.assertTrue(vicky.is_working_day(my_date))

    def test_default_project_number(self):
    	"""Tests if the default number of projects is None"""
    	gir = Manager()
    	self.assertListEqual([gir.projects], [None])

    def test_add_projects_number(self):
    	"""Tests if it adds projects given into a list"""
    	man = Manager(projects=["inventory","receivables"])
        self.assertEqual(man.projects, ['inventory', 'receivables'])



