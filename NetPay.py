#write a program that will create the following employee instance 
#as well as payroll deduction instances as shown below :

#Employee: Name 	
# ID Number 	Department 	Job Title	Monthly Salary
#Jimmy Smith	58475	Information Systems	Developer	 $ 6,800.00
#
# Payroll deductions 
# Description	Date	Charge	EmployeeID
#food court	8/14/2022	22.50	39119
#gift contribution	8/12/2022	25.00	58475
#food court	8/17/2022	15.25	21547
#vending machine	8/22/2022	3.00	58475
#vending machine	8/5/2022	2.75	58475

import EmployeeClass as emp

import PayrollDeductionClass as pay

employee = emp.Employee('Jimmy Smith',58475,'Information Systems','Developer', 6800)

deduction1 = pay.Payroll_Deduction('food court','8/14/2022',22.50,39119)
deduction2 = pay.Payroll_Deduction('gift contribution','8/12/2022',25.00,58475)
deduction3 = pay.Payroll_Deduction('food court','8/17/2022',15.25,21547)
deduction4 = pay.Payroll_Deduction('vending machine','8/22/2022',3.00,58475)
deduction5 = pay.Payroll_Deduction('vending machine','8/5/2022',2.75,58475)

#net_pay = (deduction2.get_crg_amt() - deduction4.get_crg_amt() - deduction5.get_crg_amt())

print('*** Employee Pay ***')
print('Name:', employee.get_name())
print('ID Number:', employee.get_id())
print('Department', employee.get_dept())
print('Gross Pay: $', float(employee.get_monthly_salary()), sep='')
print('Net Pay: $', employee.get_monthly_salary() - deduction2.get_crg_amt() - deduction4.get_crg_amt() - deduction5.get_crg_amt(), sep='')