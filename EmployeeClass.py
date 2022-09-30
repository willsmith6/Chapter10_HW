#Write a class named Employee that holds the following data about an employee in attributes:
# name, ID number, department, job title and monthly salary.

# The Employee class’s __init__ method should accept an argument for each attribute. 
# #The Employee class should have accessor methods for each attribute.
# #All attribute should be hidden.

import random

class Employee:

    def __init__(self,name,emp_id,dept,job_title,monthly_salary):
        self.__name = name
        self.__emp_id = emp_id
        self.__dept = dept
        self.__job = job_title
        self.__mn_salary = monthly_salary


    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__emp_id

    def get_dept(self):
        return self.__dept

    def get_job(self):
        return self.__job

    def get_monthly_salary(self):
        return self.__mn_salary