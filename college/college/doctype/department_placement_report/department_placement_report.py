# -*- coding: utf-8 -*-
# Copyright (c) 2020, mvit ise and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class DepartmentPlacementReport(Document):
	def get_usn(self,department,company):
		recruited_student_usn = list(frappe.db.sql("""select usn from `tabRecruited Students list` where parent="{0}" """.format(company)))
		student_usn = list(frappe.db.sql("""select usn from `tabStudent` where department="{0}" """.format(department)))
		self.get_department_recruited_list (recruited_student_usn,student_usn)


	def get_department_recruited_list(self,recruited_student_usn,student_usn):
		recruited_student_usn.sort()
		student_usn.sort()
		count1=len(recruited_student_usn)
		count2=len(student_usn)
		i=j=0
		department_recruited_student=list()
		while i<count1 and j<count2:
			if(recruited_student_usn[i]<student_usn[j]):
				i+=1
			elif(recruited_student_usn[i]>student_usn[j]):
				j+=1
			else:
				department_recruited_student.append(recruited_student_usn[i])
				i+=1
				j+=1
		self.update_data(department_recruited_student)	

	def update_data(self,department_recruited_student):
		department_recruited_student_list = list(sum(department_recruited_student, ()))
		for student in department_recruited_student_list:
			a=fill_student_data(get_student_name(student),student)
			self.append("department_placed_student_list",a)


def get_student_name(student):
	student_details = frappe.get_doc("Student",student)
	return " ".join(filter(None,[student_details.first_name,student_details.middle_name,student_details.last_name]))


def fill_student_data(student_detail,usn):
	student_entry = frappe.new_doc("Student_id")
	student_entry.usn  = usn
	student_entry.name1 = student_detail
	return student_entry
