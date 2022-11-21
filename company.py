# Company
# class should handle the employees and have some calculation function to understand what is going on with DataLovers.
# • init dunder – get just a company name and set employees list 3(also index for iter dunder)
# • str dunder – prints the company’s name and how many employees there are.
# • Make this class iterable(using iter and next dunders)
# • add_employee(employee) – get an employee object and adds him into employees list o Raise a TypeError if someone
#   is trying to add object that is different from out employees objects
# • remove_employee(employee_id) – remove    employee    from employees list    by    his    ID
# • update_employees – overwrites    the    employees.json    file    with the new employees list \
# • load_employees – loads employees.json and set it as the new employees list

import employee
from employee import *
import json

class Company:
    def __init__(self, company_name):
        self.company_name = company_name  # Company name
        self.emp_list = []  # Employees list
        self.e_idx = -1  # iter index

    def __iter__(self):
        return self

    def __next__(self):
        self.e_idx += 1
        if self.e_idx > len(self.emp_list) - 1:
            raise StopIteration
        return self.emp_list[self.e_idx]

    def __str__(self):
        return f'{self.company_name}, {len(self.emp_list)} employees'

    def add_employee(self,new_emp):
        if isinstance(new_emp, employee.Employee):
            dup = filter(lambda x: x.e_id == new_emp.e_id, self.emp_list)
            dupl = list(dup)
            if len(dupl) > 0:
                raise ValueError('Added employee ID already exist')
            self.emp_list.append(employee)
        else:
            raise TypeError('object is not of class Employee')


    def remove_employee(self, employee_id):
        for e in self.emp_list:
            if e['employee_id'] == employee_id:
                self.emp_list.remove(e)
        return self.emp_list

    def load_employees(self):
        with open('employees.json', 'r') as l_file:
            self.employees = json.load(l_file)
            return self.employees

    def update_employees(self):
        with open('employees1.json', 'w') as e_file:
            e_file.write(json.dumps(self.employees, indent=1))

    def get_count_internal(self):
        count_inter = list(filter(lambda e: e.type == 'internal', self.emp_list))
        return len(count_inter)

    def get_count_contractor(self):
        count_contractor = list(filter(lambda e: e.type == 'contractor', self.emp_list))
        return len(count_contractor)

    def avg_salary(self):
        salary_avg = sum([item['salary'] for item in self.employees])/len(self.employees)
        return salary_avg

    def contractor_avg_salary(self):
        con_avg = sum([item['salary'] for item in self.employees if item['type'] == 'contractor'])/len(self.employees)
        return con_avg

    def internal_avg_salary(self):
        in_avg = sum([item['salary'] for item in self.employees if item['type'] == 'internal']) / len(self.employees)
        return in_avg

    def total_raise(self, percent):
        raise_cost = sum([item['salary'] * (percent / 100) for item in self.employees])
        return raise_cost



