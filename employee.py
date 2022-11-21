import logging

class Employee:
    # 1. Init dunder (__init__) – get employee id, name, surname, salary and city
    # 2. str dunder (__str__) – returns employee as string
    # 3. dict dunder (__dict__)– returns employee as dictionary (just return dictionary of the
    # employee, it will help you save the employees as JSON file)
    # 4. get_full_name – returns the employee’s full name (first surname)
    # 5. get_id – returns the employee’s ID
    # 6. get_salary – returns the employee’s salary
    # 7. get_city – returns the employee’s city
    # 8. raise_salary(percent) – get a percent and adds this percent to the employee’s salary
    def __init__(self, employee_id, name, surname, salary, city):
         self.employee_id = employee_id
         self.name = name
         self.surname = surname
         self.salary = salary
         self.city = city

    def __str__(self):
        # method so we can print an employee
        return f'ID {self.employee_id}"\n", Name {self.name}"\n", Surname {self.surname}"\n", Salary {self.salary} "\n", From  {self.city}'

    def __dict__(self):
        # method returns employee as dictionary
        return {
            "employee_id": self.employee_id,
            "name": self.name,
            "surname": self.surname,
            "salary": self.salary,
            "city": self.city
        }

    def get_full_name(self):
        # method returns the employee’s full name (first surname)
        return f'Name {self.name}"\n", Surname {self.surname}'

    def get_id(self):
        # method returns the employee’s ID
        return f' ID {self.employee_id}'

    def get_salary(self):
        # method returns the employee’s salary
        return f' salary {self.salary}'

    def get_city(self):
        # method returns the employee’s city
        return f' From {self.city}'

    def raise_salary(self,percent):
        # method get a percent and adds this percent to the employee’s salary
        self.salary += self.salary * (percent / 100)
        logging.info(f'Salary raise e_id:{str(self.get_id())} '
                     f'{str(self.get_salary())}')


class Conractor(Employee):
    # 1. Init dunder – inherit from Employee and adds also the other company name(for example, employee ID number 1000 works at Apple)
    # 2. str dunder – inherit from Employee and adds the word “Contractor” at the beginning of the string
    #   (Contractor Employee 1000 - Ashley West from Ramat Gan and salary – 15000)
    # 3. dict dunder – inherit from Employee but adds also {“type” : “contractor”, “company_name” : company_name}
    def __init__(self, employee_id, name, surname, salary, city, company_name):
        super().__init__(employee_id, name, surname, salary)
        self.company_name = company_name
        self.type = 'contractor'

    def __str__(self):
          # method so we can print an employee
          return f' Contractor {super().__str__()}'

    def __dict__(self):
        contractor_d = super().__dict__()
        contractor_d['type'] = self.type
        contractor_d['company_name'] = self.company_name
        return contractor_d

# "employee_id": 1000,
# "name": "Ashley",
# "surname": "West",
# "salary": 15000,
# "city": "Ramat Gan",
# "type": "contractor",
# "company_name": "Apple"


class CompanyEmployee(Employee):

    # CompanyEmployee
    # • Init dunder – inherit from Employee and adds also how many days off are left(any employee starts with 15 days)
    # • dict dunder – inherit from Employee but adds also {“type”: “internal”, “daysoff”: days off}
    # • decrease_daysoff(days) – get number of days and decrease it from user’s days off
    # • Create exception called “Daysoff Error” to handle a negative days off(“minus” days off are not allowed in DataLovers)

    def __init__(self, employee_id, name, surname, salary, city, days_off=15):
        super().__init__(employee_id, name, surname, salary, city)
        self.days_off = int(days_off)
        self.type = 'internal'

    def __dict__(self):
        employee_dict = super().__dict__()
        employee_dict['type'] = self.type
        employee_dict['days_off'] = self.days_off
        return employee_dict

    class DaysoffError(Exception):
        pass

    def decrease_daysoff(self, days):
        if days <= self.days_off:
            self.days_off -= days
        else:
            raise DaysoffError('"minus" days off are not allowed in DataLovers')


