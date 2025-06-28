# Copyright (c) 2025, imran and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from pypika.functions import Avg
# from pypika.functions import Sum


class ClassRecords(Document):
	# query = frappe.qb.get_query("Class Records")
	# queries = query.run(as_dict=True)
	# print("QB Output:",queries)
	# query = frappe.qb.get_query("Class Records", fields=["name", "class_name"])
	# queries = query.run(as_dict=True)
	# print("QB Output:", queries)
	# query = frappe.qb.get_query("Class Records", fields=["name as class_record_id", "class_name as name_of_class"], filters={"name": "2"})
	# queries = query.run(as_dict=True)
	# print("QB Output:", queries)
	# left join using child doctype attached to the parent doctype like class records Child Table Fields
	# query = frappe.qb.get_query("Class Records", fields=["student_amount.total_amount", "student_amount.total_gst", "student_amount.month"], filters={"name": "2"})
	# queries = query.run(as_dict=True)
	# print("QB Output:", queries)
	# Linked Document Fields using left join
	# query = frappe.qb.get_query('Class Records', fields=["name", "student_name", "subject_records.subject_name"], filters={"name": "2"})
	# queries = query.run(as_dict=True)
	# print("QB Output:", queries)
	# Fetching Child Table Records complete records
	# query = frappe.qb.get_query('Class Records', fields=["name", "student_name",{"student_amount": ["total_amount", "total_gst", "month"]}], filters={"name": "2"}, limit=5)
	# queries = query.run(as_dict=True)
	# print("QB Output:", queries)
	# Aggregation Functions COUNT, SUM, AVG, MIN, MAX
    # query = frappe.qb.get_query(
    #     'Class Records',
    #     fields=["class_section", {"COUNT": "name", "as": "total_users"}],
    #     group_by="class_section"
    # )
	# class_records = frappe.qb.DocType("Class Records")
    # student_amount = frappe.qb.DocType("Student Amount Records")
    # query = (
    #     frappe.qb.from_(class_records)
    #     .join(student_amount)
    #     .on(class_records.name == student_amount.parent)
    #     .select(
    #         class_records.student_name,
    #         Sum(student_amount.total_amount).as_("total_amount")
    #     )
    #     .where(class_records.name == "2")
    # )
    # queries = query.run(as_dict=True)
    # print("QB Output:", queries)
	
	class_records = frappe.qb.DocType("Class Records")
	student_amount = frappe.qb.DocType("Student Amount Records")
	query = (
		frappe.qb.from_(class_records)
		.join(student_amount)
		.on(class_records.name == student_amount.parent)
		.select(
			class_records.student_name,	
			Avg(student_amount.total_amount).as_("total_amount"),
		)
		.where(class_records.name == "2")
	)
	queries = query.run(as_dict=True)
	print("QB Output:", queries)

