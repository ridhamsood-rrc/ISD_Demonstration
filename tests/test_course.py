"""
Description: Unit tests for the Course class.
Author: ACE Faculty
Modified by: Ridham Sood
Date: 29-8-2025
Usage: To execute all tests in the terminal execute 
the following command (replace test_file_name.py with 
the appropriate file name.):
    python -m unittest tests/test_file_name.py
"""
import unittest
from course.course import Course
from department.department import Department


class TestClass(unittest.TestCase):

    def setUp(self):
        # this setUp gets runs before any tests.
        self.course = Course("ISD", Department.COMPUTER_SCIENCE, 6)

    def test_init_valid(self):
        # Arrange & Act
        course = Course("ISD", Department.COMPUTER_SCIENCE, 6)

        # Assert (use name mangling to obtain private attributes)
        self.assertEqual("ISD", course._Course__name)
        self.assertEqual(Department.COMPUTER_SCIENCE, course._Course__department)
        self.assertEqual(6, course._Course__credit_hours)

    def test_init_invalid_name_raises_exception(self):
        # Arrange & Act
        with self.assertRaises(ValueError):
            course = Course("", Department.COMPUTER_SCIENCE, 6)


    def test_init_invalid_department_raises_exception(self):
        # Arrange and act
        with self.assertRaises(ValueError):
            course = Course("ISD", "Invalid", 6)

    def test_init_invalid_credit_hours_raises_exception(self):
        # Arrange and act
        with self.assertRaises(ValueError):
            course = Course("ISD", Department.COMPUTER_SCIENCE , "six")

    def test_accessors(self):
        # Arrange is now done above
        # Act and assert here
        self.assertEqual("ISD", self.course.name)

    def test_department_accessor(self):
        # Arrange setUp above
        # Act and assert here
        self.assertEqual(Department.COMPUTER_SCIENCE, self.course.department)

    def test_credit_hours_accessor(self):
        # Arrange done above
        # Act and assert here
        self.assertEqual(6, self.course.credit_hours)

    def test_str(self):
        # arrange done by setup
        expected = ("Course: ISD\n"
                    + "Department: Computer Science\n"
                    + "Credit Hours: 6")

        # act and assert
        self.assertEqual(expected, str(self.course))