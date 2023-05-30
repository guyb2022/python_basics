from employee import Employee
from developer import Developer
from manager import Manager
# import datetime


emp_1 = Employee("mo","bo",10000)
emp_2 = Employee("sho","do",20000)
emp_3_str = 'lo-po-30000'
emp_3 = Employee.from_string(emp_3_str)

dev_1 = Developer('devy','dov',40000, 'pyhton')
# my_date = datetime.date(2016, 7, 11)
# print(Employee.is_work_day(my_date))

man = Manager("mr","manager",60000, [emp_1,emp_2,emp_3,dev_1])
# print(man.full_name)
# man.print_employees

## Check if object is intance or subclass
# print(isinstance(man, Employee))
# print(issubclass(Manager, Employee))

print(man)
# print(len(man))
man.full_name = "mr big"
print(man)
del man
