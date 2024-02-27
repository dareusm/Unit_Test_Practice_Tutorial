import unittest
from unittest.mock import patch
import employee 

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        print('setUp')
        self.emp_1 = employee.Employee("John", "Doe", 50000)
        self.emp_2 = employee.Employee("Jane", "Doe", 50000)
        self.emp_3 = employee.Employee("greg", "Smith", 60000)
        self.emp_4 = employee.Employee("Friedrich", "Nietzsche", 1000000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, "John.Doe@email.com")
        self.assertEqual(self.emp_2.email, "Jane.Doe@email.com")
        self.assertEqual(self.emp_3.email, "greg.Smith@email.com")
        self.assertEqual(self.emp_4.email, "tiana.trump@email.com")

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, "John Doe")
        self.assertEqual(self.emp_2.fullname, "Jane Doe")

        self.emp_1.first = "Dareus"
        self.emp_2.first = "Courtney"

        self.assertEqual(self.emp_1.fullname, "Dareus Doe")
        self.assertEqual(self.emp_2.fullname, "Courtney Doe")

    def test_apply_raise(self):
        print('test_apply_raise')
        self.assertEqual(self.emp_1.pay, 50000)
        self.assertEqual(self.emp_2.pay, 50000)

        self.emp_1.apply_raise()
        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 50000)

        self.emp_2.apply_raise()
        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 52500)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule("April")
            mocked_get.assert_called_with("http://company.com/Doe/April")
            self.assertEqual(schedule, "Success")


            mocked_get.return_value.ok = False

            schedule = self.emp_3.monthly_schedule("June")
            mocked_get.assert_called_with("http://company.com/Smith/June")
            self.assertEqual(schedule, "Bad Response")

if __name__ == "__main__":
    unittest.main()
