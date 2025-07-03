# Copyright (c) 2025, imran and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class DriverList(Document):
     pass
# @frappe.whitelist()	
# def get_diver_info(Driver_id):
# 	DriverList = frappe.get_doc("Driver List", Driver_id)
# 	return {
# 	    "Driver_List": DriverList.driver_name,
# 		"license_name": DriverList.license_name,
#         "phone_number": DriverList.phone_number,
# 		"joining_date": DriverList.joining_date,
# 		"salary": DriverList.salary,
# 	}
# ------------------------------------------------------------------------------------------
# @frappe.whitelist()
# def single_parameter(role_profile, person):
# 	print(person)
# 	if role_profile == 'Test':
# 		return "this is single parameter"
# 	else:
# 		return "Param Not Found"
# ------------------------------------------------------------------------------------------
# @frappe.whitelist()
# def options(role_profile):
#     return 'option'
# ------------------------------------------------------------------------------------------

# @frappe.whitelist()
# def send_email(docname):
#     doc = frappe.get_doc("Driver List", docname)
#     subject = "Driver Offer Letter"
#     message = f"""
#     <p>Hello {doc.driver_name}</p>
#     <p>Your License No: {doc.license_name}</p>
#     <p>Your Phone No: {doc.phone_number}</p>
#     <p>Joining Date: {doc.joining_date}</p>
#     <p>Salary: {doc.salary}</p><br><br>
#     <p>Thank you for joining us!</p><br><br>
#     <p>Best Regards,</p>
#     <p>Tridotstech</p>
#     """

#     try:
#         frappe.sendmail(
#             recipients=[doc.driver_email],
#             subject=subject,
#             message=message,
# 			now=True 
#         )
#         return "success"
#     except Exception as e:
#         return f"Failed: {e}"