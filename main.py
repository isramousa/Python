# -*- coding: iso-8859-1 -*-
import os
import re
import department
import employee

class Main(object):
  def __init__(self):
    self.employees = []
    self.departments = []

  def make_file_path(self, file_path):
    dir = os.path.dirname(os.path.realpath('__file__'))
    abs_file_path = os.path.join(dir, file_path)
    return abs_file_path
  
  def read_emp_from_db(self):
    file_name = self.make_file_path("./DB/emp.txt")
    file = open(file_name, "r")
    employee_row_data = file.readlines()
    file.close()
    for line in employee_row_data:
      words = re.split(r"\s+",line)
      emp = employee.Employee()
      emp.empName = words[0]
      emp.empPhoneNumber = words[1]
      emp.empId = words[2]
      emp.empDOB = words[3]
      emp.empPosition = words[4]
      emp.empManagerId = words[5]
      emp.empDepartmentId = words[6]
      self.employees.append(emp)

  def read_department_from_db(self):
    file_name = self.make_file_path("./DB/dep.txt")
    file = open(file_name, "r")
    department_row_data = file.readlines()
    file.close()
    for line in department_row_data:
      words = re.split(r"\s+",line)
      dep = department.Department()
      dep.managerId = words[0]
      dep.departmentId = words[1]
      dep.departmentName = words[2]
      self.departments.append(dep)
  
  def sort_employees_name(self):
    sorted_name_list = self.employees[:]
    return sorted(sorted_name_list, key = lambda emp:emp.empName)
    
    
  def sort_employees_id(self):
    sorted_id_list = self.employees[:]
    return sorted(sorted_id_list, key = lambda emp:emp.empId)

  def print_emp(emp_obj):
    print('here')
    print('employee with name: {0}, and born in:{1} with mobile number:{2} and his position is:{3}'.format(emp_obj.empName, emp_obj.empDOB, emp_obj.empPhoneNumber, emp_obj.empPosition))


  def get_emp_info(self, employee_id):
    for emp in self.employees:
      temp_id = emp.empId
      print(temp_id == employee_id)
      if temp_id == employee_id:
	print('found')
	emp_temp = emp
	self.print_emp(emp_temp)

  def print_emp(emp_obj):
    print('here')
    print('employee with name: {0}, and born in:{1} with mobile number:{2} and his position is:{3}'.format(emp_obj.empName, emp_obj.empDOB, emp_obj.empPhoneNumber, emp_obj.empPosition))



