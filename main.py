# -*- coding: iso-8859-1 -*-
import os
import re
import department
import employee

class Main(object):
  def __init__(self):
    self.employees = []
    self.departments = []
    self.file_emp = "./DB/emp.txt"
    self.file_dep = "./DB/dep.txt"

  #this method for creating correct path for file to be opend
  def make_file_path(self, file_path):
    dir = os.path.dirname(os.path.realpath('__file__'))
    abs_file_path = os.path.join(dir, file_path)
    return abs_file_path
  
  #read employees from file and added to list_of_emp
  def read_emp_from_db(self):
    file_name = self.make_file_path(self.file_emp)
    with open(file_name, "r") as file:
      employee_row_data = file.readlines()
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
  
  #read department_info from file and added to list_of_dep
  def read_department_from_db(self):
    file_name = self.make_file_path(self.file_dep)
    with open(file_name, "r") as file:
      department_row_data = file.readlines()
    for line in department_row_data:
      words = re.split(r"\s+",line)
      dep = department.Department()
      dep.managerId = words[0]
      dep.departmentId = words[1]
      dep.departmentName = words[2]
      self.departments.append(dep)
    
  #sort by name
  def sort_employees_name(self):
    self.read_emp_from_db()
    sorted_name_list = self.employees[:]
    return sorted(sorted_name_list, key = lambda emp:emp.empName)
    
  #sort by id  
  def sort_employees_id(self):
    self.read_emp_from_db()
    sorted_id_list = self.employees[:]
    return sorted(sorted_id_list, key = lambda emp:emp.empId)

  #get employee that match position or doesn't match position
  def emp_with_pos(self, word, eq):
    matched_list = []
    title = ''
    if eq == 1:
      title = 'The employee with matched position ' + word
      eq_exp = r".*(?={0})".format(word)
    else:
      #put the data that doent match specific word
      title = 'The employee with unmatched position ' + word
      eq_exp = r"^([^\s]*)\s([^\s]*)\s([^\s]*)\s([^\s]*)\s(?!{0})".format(word)
    file_name = self.make_file_path(self.file_emp)
    with open(file_name, "r") as file:
      for line in file:
	result = re.search(eq_exp, line)
	if result:
	  data = result.group().split()
	  temp_tuple = (data[0], data[2])
	  matched_list.append(temp_tuple)
    if len(matched_list) == 0:
      print('No matched items!')
    else:
      print(title)
      for tpl in matched_list:
	print(tpl)
    
  #count of employee with same month
  def get_count_with_same_month(self, month_num):
    count = 0
    exp = r"\/{0}\/".format(month_num)
    file_name = self.make_file_path(self.file_emp)
    with open(file_name, "r") as file:
      for line in file:
	result = re.search(exp, line)
	if result:
	  count += 1
    return count
  
  #search by any type of data
  def search_employee_data(self, search_type, searched_item):
    list_of_search = []
    if search_type == 0:
      #general issue
      exp = "^([^\s]*)\s([^\s]*)\s([^\s]*)\s.*{0}".format(searched_item)
    elif search_type == 1:
      #by name
      exp = r"^({0})\s([^\s]*)\s([^\s]*)".format(searched_item)
    elif search_type == 2:
      #by phone
      exp = r"^([^\s]*)\s{0}\s([^\s]*)".format(searched_item)
    elif search_type == 3:
      #by id
      exp = r"^([^\s]*)\s.*{0}".format(searched_item)
      
    file_name = self.make_file_path(self.file_emp)
    with open(file_name, "r") as file:
      for line in file:
	result = re.search(exp, line)
	if result:
	  data = result.group().split()
	  temp_tuple = (data[0], data[2])
	  list_of_search.append(temp_tuple) 
    if len(list_of_search) == 0:
      print('No matched items!')
    else:
      for tpl in list_of_search:
	print(tpl)

  #get any entry using emp_num
  def get_entry_by_emp_num(self, emp_num, entry):
    entry_returned = ""
    
    exp = r".*({0}).*".format(emp_num)
    file_name = self.make_file_path(self.file_emp)
    with open(file_name, "r") as file:
      for line in file:
	result = re.search(exp, line)
	if result:
	  data = result.group().split()
	  if entry == 1:#name
	    entry_returned = "emp_name: " + str(data[0])
	  elif entry == 2:#phoneNumber
	    entry_returned = "phone_number: " + str(data[1])
	  elif entry == 3:#DOB
	    entry_returned = "date_of_birth: " + str(data[3])
	  elif entry == 4:#position
	    entry_returned = "emp_position: " + str(data[4])
	  elif entry == 5:#mangerId
	    entry_returned = "emp_manager_id: " + str(data[5])
	  elif entry == 6:#departmentId
	    entry_returned = "emp_department_id: " + str(data[6])
    return entry_returned


m = Main()
for i in range(1,7):
  x = m.get_entry_by_emp_num(11315376, i)
  print(x)	  