# -*- coding: iso-8859-1 -*-
class Department(object):
    '''class for department '''
    def __init__(self):
        self.department_id = 0
        self.manager_id = 0
        self.department_name = ' '

    def get_department_id(self):
        return self.department_id

    def set_department_id(self, department_id):
        self.department_id = department_id

    def get_manager_id(self):
        return self.manager_id

    def set_manager_id(self, manager_id):
        self.manager_id = manager_id

    def get_department_name(self):
        return self.department_name

    def set_department_name(self, department_name):
        self.department_name = department_name

    departmentId = property(get_department_id, set_department_id)
    departmentName = property(get_department_name, set_department_name)
    managerId = property(get_manager_id, set_manager_id)
