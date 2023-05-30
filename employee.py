import requests

class Employee:
    """
    A class to demonstrate differents methods and behave in OOP,
    including: testing with unittest,inharitence, abstract and static methods
    geters, seters
    """
    raise_amount = 1.05
    num_of_emps = 0

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emps += 1

    @property
    # To call full_name as property instead of a function with ()
    def full_name(self):
        """ Set the full name property in its format"""
        return f"{self.first} {self.last}"

    @property
    def email(self):
        """ Set the email property """
        return f"{self.first}.{self.last}@blabla.com"

    @full_name.setter
    def full_name(self, name):
        """ Set an employee name with fullname as input"""
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @full_name.deleter
    def full_name(self):
        """ Delete an employee name (first + last)"""
        self.first = None
        self.last = None

    def apply_raise(self):
        """ Aplly the raise for the employee"""
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        """ Set the raise amout for the Employee class"""
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, employee):
        """ Create an EMployee instance from a string """
        first, lasy, pay = employee.split('-')
        return cls(first, lasy, pay)

    @staticmethod
    def is_work_day(day):
        """ Check if the current day is a working day"""
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        """ For debug method to repreduce an instance of Employee"""
        return f"Employee({self.first},{self.last},{self.pay})"

    def __str__(self):
        """ Set the print method"""
        return f"{self.full_name} - {self.email}"

    def __add__(self, other):
        """ Add two employees by their pay field"""
        return self.pay + other.pay

    def __len__(self):
        """ Rturn how many charecters the fullnmae has """
        return len(self.full_name)

    def monthly_scheduale(self, month):
        """ Mock function to simulate web request"""
        response = requests.get(f'https://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return "Bad Response!"
