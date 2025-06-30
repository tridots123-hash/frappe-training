# Copyright (c) 2025, imran and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
# from frappe.model.utils.tree import get_descendants_of
# from frappe.query_builder.functions import Concat
# from frappe.query_builder.functions import Extract
# from frappe.query_builder.functions import Now
# from frappe.query_builder.functions import IfNull
# from frappe.query_builder.functions import Abs
# from pypika.functions import Count
# from pypika.functions import Sum
# from pypika.functions import Avg
# from pypika.functions import Min
# from pypika.functions import Max


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
# --------------------------------------------------------------------------------------
	# child table total_amount sum
	# class_records = frappe.qb.DocType("Class Records")
	# student_amount = frappe.qb.DocType("Student Amount Records")

	# query = (
	# 	frappe.qb.from_(class_records)
	# 	.join(student_amount)
	# 	.on(class_records.name == student_amount.parent)
	# 	.select(
	# 		class_records.student_name,
    #         Count(student_amount.total_amount).as_("min_total_amount"),
	# 	)
	# 	.where(class_records.name == "3")
	# )

	# queries = query.run(as_dict=True)
	# print("QB Output:", queries)
# --------------------------------------------------------------------------------------
	# child table total_amount sum
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
    #     .where(class_records.name == "3")
    # )
    
    # queries = query.run(as_dict=True)
    # print("QB Output:", queries)
# --------------------------------------------------------------------------------------
    # child table total_amount Avg
	# class_records = frappe.qb.DocType("Class Records")
	# student_amount = frappe.qb.DocType("Student Amount Records")

	# query = (
	# 	frappe.qb.from_(class_records)
	# 	.join(student_amount)
	# 	.on(class_records.name == student_amount.parent)
	# 	.select(
	# 		class_records.student_name,	
	# 		Avg(student_amount.total_amount).as_("total_amount"),
	# 	)
	# 	.where(class_records.name == "3")
	# )

	# queries = query.run(as_dict=True)
	# print("QB Output:", queries)
# --------------------------------------------------------------------------------------
	# child table total_amount Min
	# class_records = frappe.qb.DocType("Class Records")
	# student_amount = frappe.qb.DocType("Student Amount Records")

	# query = (
	# 	frappe.qb.from_(class_records)
	# 	.join(student_amount)
	# 	.on(class_records.name == student_amount.parent)
	# 	.select(
	# 		class_records.student_name,
    #         Min(student_amount.total_amount).as_("min_total_amount"),
	# 	)
	# 	.where(class_records.name == "3")
	# )

	# queries = query.run(as_dict=True)
	# print("QB Output:", queries)
# --------------------------------------------------------------------------------------
    #  child table total_amount Max
	# class_records = frappe.qb.DocType("Class Records")
	# student_amount = frappe.qb.DocType("Student Amount Records")

	# query = (
	# 	frappe.qb.from_(class_records)
	# 	.join(student_amount)
	# 	.on(class_records.name == student_amount.parent)
	# 	.select(
	# 		class_records.student_name,
    #         Max(student_amount.total_amount).as_("min_total_amount"),
	# 	)
	# 	.where(class_records.name == "3")
	# )

	# queries = query.run(as_dict=True)
	# print("QB Output:", queries)
# --------------------------------------------------------------------------------------
	# Scalar Functions ABS, IFNULL, CONCAT, EXTRACT, NOW
	# Scalar functions like Abs avoid the negative value like (-10 the using abs(-10)=>10)
    # class_records = frappe.qb.DocType("Class Records")
    # student_amount = frappe.qb.DocType("Student Amount Records")
    
    # query = (
    #     frappe.qb.from_(class_records)
    #     .join(student_amount)
    #     .on(class_records.name == student_amount.parent)
    #     .select(
    #         class_records.student_name,
    #         Abs(student_amount.total_amount).as_("abs_total_amount")
    #     )
    #     .where(class_records.name == "5")
    # )
    
    # queries = query.run(as_dict=True)
    # print("QB Output:", queries)
# --------------------------------------------------------------------------------------
    # IfNull using to replace null values with a default value
    # class_records = frappe.qb.DocType("Class Records")
    # student_amount = frappe.qb.DocType("Student Amount Records")
    
    # query = (
    #     frappe.qb.from_(class_records)
    #     .join(student_amount)
    #     .on(class_records.name == student_amount.parent)
    #     .select(
    #         class_records.student_name,
    #         IfNull(student_amount.total_amount, "no_value").as_("total_amount")
    #     )
    #     .where(class_records.name == "10")
    # )
    
    # queries = query.run(as_dict=True)
    # print("QB Output:", queries)

	# class_records = frappe.qb.DocType("Class Records")
	
	# query = (
	# 	frappe.qb.from_(class_records)
	# 	.select(
	# 		class_records.class_name,
	# 		class_records.student_name,
	# 		IfNull(class_records.student_email, "this record is currently null").as_("student_email_id"),
	# 	)
	# 	.where(class_records.name == "15")
	# )
	
	# queries = query.run(as_dict=True)
	# print("QB Output:", queries)
# --------------------------------------------------------------------------------------
	# Concat using to concatenate two or more strings
	# class_records = frappe.qb.DocType("Class Records")

	# query = (
	# 	frappe.qb.from_(class_records)
	# 	.select(
	# 		Concat(class_records.student_name, "(", class_records.class_name,"-",class_records.class_section,")").as_("student_join_record_using_concat")
	# 	)
	# 	.where(class_records.name == "3")
	# )

	# queries = query.run(as_dict=True)
	# print("QB Output:", queries)
# --------------------------------------------------------------------------------------
# # Extract using to extract a specific part of a date or time
# 	class_records = frappe.qb.DocType("Class Records")
# 	student_amount = frappe.qb.DocType("Student Amount Records")

# 	query = (
# 		frappe.qb.from_(class_records)
# 		.join(student_amount)
# 		.on(class_records.name == student_amount.parent)
# 		.select(
# 			class_records.student_name,
# 			Extract("month", student_amount.month).as_("month"),
# 		)
# 		.where(class_records.name == "3")
# 	)

# 	queries = query.run(as_dict=True)
# 	print("QB Output:", queries)
# --------------------------------------------------------------------------------------
	# Now using to get the current date and time
	# class_records = frappe.qb.DocType("Class Records")

	# query = (
	# 	frappe.qb.from_(class_records)
	# 	.select(
	# 		class_records.student_name,
	# 		Now().as_("current_date_time")
	# 	)
	# 	.where(class_records.name == "3")
	# )

	# queries = query.run(as_dict=True)
	# print("QB Output:", queries)
# --------------------------------------------------------------------------------------
#    dictory filters
	# queries = frappe.qb.get_query(
	# 	"Class Records",
	# 	fields=["name", "class_name", "student_name", "student_email"],
	# 	filters={"student_name": "Imran"}
	# )
	# queries = queries.run(as_dict=True)
	# print("QB Output:", queries)
# --------------------------------------------------------------------------------------
# Example of using Query Builder to fetch records with filters
	# class_records = frappe.qb.DocType("Class Records")
	
	# query = (
	# 	frappe.qb.from_(class_records)
	# 	.select(
	# 		class_records.name,
	# 		class_records.class_name,
	# 		class_records.student_name,
	# 		class_records.student_email
	# 	)
	# 	.where(class_records.student_name.like("%Mohammed%"))
	# )
	
	# result = query.run(as_dict=True)
	# print("QB Output:", result)
# --------------------------------------------------------------------------------------
# Example of using Query Builder to fetch records with multiple filters
    # as_dict, as_list, plunk, debug
    # class_records = frappe.qb.DocType("Class Records")
    # student_amount = frappe.qb.DocType("Student Amount Records")
    
    # query = (
    #     frappe.qb.from_(class_records)
    #     .join(student_amount)
    #     .on(class_records.name == student_amount.parent)
    #     .select(
    #         class_records.student_name,
    #         class_records.student_email,
    #         student_amount.month,
    #     )
    #     .where(
    #         (class_records.name == "3") & 
    #         (student_amount.month > "2025-06-28")
    #     )
    # )
    
    # queries = query.run(as_dict=True)
    # print("QB Output:", queries)
# --------------------------------------------------------------------------------------
    # isIn using to filter records based on a list of values
	# class_records = frappe.qb.DocType("Class Records")
	# query = (
	# 	frappe.qb.from_(class_records)
	# 	.select(
	# 		class_records.class_name,
	# 	    Count(class_records.class_name).as_("total_students_in_section"),
	# 	)
	# 	.where(class_records.class_name.isin(["10th", "11th"])).groupby(class_records.class_name)
	# )

	# queries = query.run(as_dict=True)
	# print("QB Output:", queries)
# --------------------------------------------------------------------------------------
	# isNotIn using to filter records based on a list of values
	# class_records = frappe.qb.DocType("Class Records")
	# query = (
	# 	frappe.qb.from_(class_records)
	# 	.select(
	# 		class_records.class_name,
	# 		Count(class_records.class_name).as_("total_students_in_section"),
	# 	)
	# 	.where(class_records.class_name.notin(["10th", "11th"])).groupby(class_records.class_name)
	# )

	# queries = query.run(as_dict=True)
	# print("QB Output:", queries)
# --------------------------------------------------------------------------------------
	# class_records = frappe.qb.DocType("Class Records")

	# query = (
	# 	frappe.qb.from_(class_records)
	# 	.select(
	# 		Count(*).as_("total_records"),
	# 	)
	# )

	# queries = query.get_sql()
	# print("QB Output:", queries)
# --------------------------------------------------------------------------------------
	# class_records = frappe.qb.DocType("Class Records")

	# query = (
	# 	frappe.qb.from_(class_records)
	# 	.select(
	# 		class_records.name,
	# 		class_records.class_name,
	# 		class_records.student_name,
	# 		class_records.student_email
	# 	)
	# 	.limit(5)
	# )

	# queries = query.run(as_dict=True)
	# print("QB Output:", queries)
# --------------------------------------------------------------------------------------
    class_records = frappe.qb.DocType("Class Records").Distinct()

	query = (
		frappe.qb.from_(class_records)
		.select(
			class_records.name,
			class_records.class_name,
			class_records.student_name,
			class_records.student_email
		)
	)

	queries = query.run(as_dict=True)
	print("QB Output:", queries)