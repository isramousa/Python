# -*- coding: iso-8859-1 -*-
class Employee(object):
    '''class for Employee '''
    def __init__(self):
        self.emp_id = 0
        self.emp_phone_number = 0
        self.emp_name = ' '
        self.emp_dob = 0
        self.emp_position = ' '
        self.emp_manager_id = ' '
        self.emp_department_id = 0

    def get_emp_id(self):
        return self.emp_id

    def set_emp_id(self, emp_id):
        self.emp_id = emp_id

    def get_emp_phone_number(self):
        return self.emp_phone_number

    def set_emp_phone_number(self, emp_phone_number):
        self.emp_phone_number = emp_phone_number

    def get_emp_name(self):
        return self.emp_name

    def set_emp_name(self, emp_name):
        self.emp_name = emp_name

    def get_emp_dob(self):
        return self.emp_dob

    def set_emp_dob(self, emp_dob):
        self.emp_dob = emp_dob

    def get_emp_position(self):
        return self.emp_position

    def set_emp_position(self, emp_position):
        self.emp_position = emp_position

    def get_emp_manager_id(self):
        return self.emp_manager_id

    def set_emp_manager_id(self, emp_manager_id):
        self.emp_manager_id = emp_manager_id

    def get_emp_department_id(self):
        return self.emp_department_id

    def set_emp_department_id(self, emp_department_id):
        self.emp_department_id = emp_department_id

    empId = property(get_emp_id, set_emp_id)
    empPhoneNumber = property(get_emp_phone_number, set_emp_phone_number)
    empName = property(get_emp_name, set_emp_name)
    empDOB = property(get_emp_dob, set_emp_dob)
    empPosition = property(get_emp_position, set_emp_position)
    empManagerId = property(get_emp_manager_id, set_emp_manager_id)
    empDepartmentId = property(get_emp_department_id, set_emp_department_id)