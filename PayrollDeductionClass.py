#Write a class that represents a payroll deduction transaction. 
# Each instance should have the description, date, charge amount and employee ID as attributes. 
# The class’s __init__ method should accept an argument for each attribute. 
# The class should have accessor methods for each attribute.
# All attribute should be hidden.

import random

class Payroll_Deduction:

    def __init__(self,desc,date,crg_amt,emp_id):
        self.__desc = desc
        self.__date = date
        self.__crg_amt = crg_amt
        self.__emp_id = emp_id

    def get_desc(self):
        return self.__desc
    
    def get_date(self):
        return self.__desc

    def get_crg_amt(self):
        return self.__crg_amt

    def get_name(self):
        return self.__emp_id