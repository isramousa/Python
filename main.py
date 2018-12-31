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
    self.employeeString = ""
    self.departmentString = ""

  #this method for creating correct path for file to be opend
  def make_file_path(self, file_path):
    dir = os.path.dirname(os.path.realpath('__file__'))
    abs_file_path = os.path.join(dir, file_path)
    return abs_file_path
  
  #read employees from file and added to list_of_emp
  def read_emp_from_db(self):
    self.employees = []
    file_name = self.make_file_path(self.file_emp)
    with open(file_name, "r") as file:
      employee_row_data = file.readlines()
    for line in employee_row_data:
      self.employeeString += line
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
    self.departments = []
    file_name = self.make_file_path(self.file_dep)
    with open(file_name, "r") as file:
      department_row_data = file.readlines()
    for line in department_row_data:
      self.departmentString += line
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
    '''file_name = self.make_file_path(self.file_emp)
    with open(file_name, "r") as file:
      for line in file:'''
    result = re.findall(exp, self.employeeString, re.M)
    if result:
      count = len(result)
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

    entry_returned = "employee with this number not found!"
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


def print_emp_list(emp_list):
  print('ID\t\tname\tphoneNumber\tposition')
  for emp in emp_list:
    print('{0}\t{1}\t{2}\t{3}'.format(emp.empId, emp.empName, emp.empPhoneNumber, emp.empPosition))

def print_main_menu():
  print("""\
  please enter the choice you need:
  1- Return emp_num and emp_name for any input field.
  2- Sort the employee list by names.
  3- Sort the employee list by Ids.
  4- Fetch data depends on Emp_id.
  5- Return the count of employees born in specific month.
  6- Return the employees that their position matches specific word.
  7- Return the employees that their position doesn't match specific word.
  """)

def print_for_choice_one():
  print("""\
  please choose the input field:
  1- by name.
  2- by phone number.
  3- by employee id.
  4- by date of birth.
  5- by position.
  6- by manager id.
  7- by department id.
  """)

def print_for_choice_four():
  print("""\
  please choose the entry you want to retrive:
  1-  name.
  2-  phone number.
  3-  date of birth.
  4-  position.
  5-  manager id.
  6-  department id.
  """)

obj = Main()
obj.read_emp_from_db()
obj.read_department_from_db()
while True:
  
  print_main_menu()
  choice = input("Enter your choice please!")
  
  if choice == 1: # global choice to return data by specific input type
    print_for_choice_one()
    enter_field = input("Enter your input type please!")
    searched_data = input('Enter the value you want to search ')
    if enter_field in range(1, 4):
      obj.search_employee_data(enter_field, searched_data)
    else:
      obj.search_employee_data(0, searched_data)

  elif choice == 2: #sort by name
    sorted_list_name = obj.sort_employees_name()
    print_emp_list(sorted_list_name)

  elif choice == 3: #sort by id 
    sorted_list_id = obj.sort_employees_id()
    print_emp_list(sorted_list_id)

  elif choice == 4: #fetch any data depends on emp_num
    print_for_choice_four()
    fetched_field = input("Enter your field you want to fetch please!")
    emp_num = input("Enter the employee number:")
    if fetched_field in range(1, 7):
      returned_entry = obj.get_entry_by_emp_num(emp_num, fetched_field)
      print(returned_entry)

  elif choice == 5: #return the count of employee depends on month
    month = input("Please enter the month you want to search for:")
    if month >= 1 and month <= 12 :
      count = obj.get_count_with_same_month(month)
      if count == 0 :
	print("No employee in this month")
      else:
	print("The number of employee born in this month is:", count)
    else:
	print("please enter a correct month number")

  elif choice == 6: #return employees that their position match some word
    position = input("Please enter the position you want to search for:")
    obj.emp_with_pos(position, 1)

  elif choice == 7: #return employees that their position doesn't match some word
    position = input("Please enter the position to return employees who don't match it :")
    obj.emp_with_pos(position, 0)

  else:
    print("UNVALID CHOICE!")












