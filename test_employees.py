import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()

    def setUp(self):
        """ Create the employee for all tests """
        self.emp1 = Employee('Mr', 'doode', 10000)

    def tearDown(self):
        """ Destroy the employee after test is done """
        pass

    def test_email(self):
        """ Test the email creation """
        self.assertEqual(self.emp1.email, 'Mr.doode@blabla.com')

        self.emp1.first = 'Big'
        self.assertEqual(self.emp1.email, 'Big.doode@blabla.com')

    def test_fullname(self):
        """ Test the fullname correctnece """
        self.assertEqual(self.emp1.full_name, 'Mr doode')

        self.emp1.first = 'Big'
        self.assertEqual(self.emp1.full_name, 'Big doode')

    def test_apply_raise(self):
        """ Test the raise action """
        self.emp1.apply_raise()
        self.assertEqual(self.emp1.pay, 10500)

    def test_set_raise_amount(self):
        """ Test the raise amount action """
        Employee.set_raise_amount(1.1)
        self.assertEqual(Employee.raise_amount, 1.1)

    def test_monthly_schedulae(self):
        """ Mock a web request test"""
        with patch('employee.requests.get') as mocked_get:
            # Seting the desire return value from the web
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
            # Run the function
            schedulae = self.emp1.monthly_scheduale('May')
            # Check the assertions
            mocked_get.assert_called_with('https://company.com/doode/May')
            self.assertEqual(schedulae, 'Success')

            # Seting the desire return value from the web
            mocked_get.return_value.ok = False
            # Run the function
            schedulae = self.emp1.monthly_scheduale('June')
            # Check the assertions
            mocked_get.assert_called_with('https://company.com/doode/June')
            self.assertEqual(schedulae, 'Bad Response!')



if __name__ == "__main__":
    unittest.main()



