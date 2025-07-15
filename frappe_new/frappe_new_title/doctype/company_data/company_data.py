# # Copyright (c) 2025, tharun and contributors
# # For license information, please see license.txt

import frappe
from frappe.model.document import Document


class CompanyData(Document):
    def custom_process(self):
        frappe.msgprint(f"Processing company: {self.company_name}")

    def custom_process2(self):
        frappe.msgprint(f"Processing company2: {self.company_name}")


#     # def before_save(self):
#     #     # print(self.company_name, self.status, self.amount, self.quantity, self.total_amount)
#     #     # get_document(self)
#     #     # get_value2()
#     #     self


#     def after_insert(self):
#         print("Publishing event for:", self.company_name)
#         frappe.publish_realtime(
#             event='new_company_created',
#             message={'company': self.company_name},
#             user='*'  # Broadcast to all users
#         )

    


    def calculate_total_amount(self):
        if self.amount and self.quantity:
            self.total_amount = self.amount * self.quantity
            self.save()
            frappe.msgprint(f"Total Amount calculated: {self.total_amount}")
        else:
            frappe.msgprint("Amount or Quantity is missing.")

#     @frappe.whitelist()
#     def greet(self):
#         return "this is my message"

# # def get_document(self):
# #     doc = frappe.get_doc("Company Data", "CMD-001")
# #     frappe.msgprint(f"Document Found: {doc.company_name}")
# #     # return f"Document Found: {doc.company_name}"

# @frappe.whitelist()
# def get_new_record():
#     if frappe.db.exists("Company Data", "CMD-008"):
#         doc = frappe.get_doc("Company Data", "CMD-008")
#         return f"Document Found: {doc.company_name}"
#     else:
#         doc = frappe.get_doc({
#             "doctype": "Company Data",
#             "company_name": "NewCompany"
#         })
#         doc.insert()
#         return f"New Document Created: {doc.name}"


    
#     # frappe.msgprint(f"Document Found: {doc.company_name}")

#     # return f"Document Found: {doc.company_name}"


# # def get_value2():
# # 	doc = frappe.get_last_doc('Company Data')
# # 	return f"Document Found: {doc.company_name}"
    
# # @frappe.whitelist()
# # def get_new_value():
# # 	doc = frappe.new_doc('Company Data')
# # 	doc.company_name= "Dell"
# # 	doc.description = "kjasfd"
# # 	doc.insert()
#     # return f"New Document Created: {doc.company_name}"
#     # frappe.msgprint(f"New Document Created: {doc.company_name}")

# # @frappe.whitelist()
# # def delete_doc_value():
# #     doc = frappe.get_doc("Company Data", "CMD-004")
# #     doc.delete_doc()
# #     print(f"Document Deleted: {doc}")
# #     return f"Document  deleted successfully"

# # def rename_doc_value():
# #     # doc = frappe.get_doc("Company Data", "CMD-005")
# #     frappe.rename_doc("Comapany Data", "CMD-002", "CMD-022")
# #     print(f"Document Renamed: {doc.name}")
# #     return f"Document renamed successfully to {doc.name}"

# # @frappe.whitelist()
# # def get_new_value():
# # 	meta = frappe.get_meta("Company Data")
# # 	fields = [df.fieldname for df in meta.fields]
# # 	return fields

# @frappe.whitelist()
# def update_company():
#     doc = frappe.get_doc("Company Data", "CMD-007")
#     doc.description = "Updated Description"
#     doc.status = "LogOut"
#     doc.save(ignore_permissions=True)
#     # doc.reload()  
#     # frappe.reload_doc("frappe-new-title", "Company Data", "CMD-007") # Reload to get the latest data
#     return f"{doc.name} updated successfully"

# @frappe.whitelist()
# def delete_company():
#     if frappe.db.exists("Company Data", "CMD-010"):
#         doc = frappe.get_doc("Company Data", "CMD-010")
#         doc.delete_doc()
#         return f"doc deleted"
#     else:
#         return f"not found"


# # @frappe.whitelist()
# # def old_doc_message(docname):
# #     doc = frappe.get_doc("Company Data", docname)
# #     old_doc = doc.get_doc_before_save()

# #     messages = []

# #     if old_doc:
# #         if old_doc.amount != doc.amount:
# #             messages.append(f"Amount changed from {old_doc.amount} to {doc.amount}")
# #         if old_doc.status != doc.status:
# #             messages.append(f"Status changed from {old_doc.status} to {doc.status}")

# #     return "\n".join(messages) if messages else "No changes detected."


# @frappe.whitelist()
# def has_price_changed(docname):
#     doc = frappe.get_doc("Company Data", docname)
#     old_amount = doc.total_amount

#     if old_amount != 2400:
#         doc.db_set('total_amount', 2400)
#         # frappe.db.commit()
#         return f"Total Amount changed from {old_amount} to 2400"
#     else:
#         return "Total Amount was already 2400"

# @frappe.whitelist()
# def add_contact(docname):
#     doc = frappe.get_doc("Company Data", docname)


#     # Append new contact
#     doc.append("contact_person", {
#         "contact_person": "Jane Smith",
#         "email": "jane@company.com",
#         "number": "9876543210"
#     })

#     doc.save()
#     return "Contact added successfully"

# @frappe.whitelist()
# def get_url(docname):
#     doc = frappe.get_doc("Company Data", docname)
#     doc = frappe.get_doc("Company Data", "CMD-007")
#     url = doc.get_url()
#     return f"URL: {url}"

# @frappe.whitelist()
# def add_comment(docname):
#     doc = frappe.get_doc("Company Data", docname)
#     # Python - server side
#     doc = frappe.get_doc("Company Data", "CMD-003")
#     # Type: Comment
#     comment = doc.add_comment('Comment', text='This is a new note.')
#     frappe.db.commit()
#     # Type: Edit
#     doc.add_comment('Edit', 'Updated amount and quantity.')
#     return f"{comment} added"


# @frappe.whitelist()
# def log_company_view(docname):
#     doc = frappe.get_doc("Company Data", docname)
#     doc = frappe.get_doc("Company Data", "CMD-001")


#     # Mark as viewed and seen
#     doc.add_viewed()
#     doc.add_seen()

#     # Add comment
#     doc.add_comment('Comment', text='User opened the document.')

#     return f"Document viewed: {doc.get_url()}"

# @frappe.whitelist()
# def method_test(docname):
#     doc = frappe.get_doc("Company Data", "CMD-006")
#     doc.run_method("custom_process")
    

@frappe.whitelist()
def queue_test(docname):
    doc = frappe.get_doc("Company Data", "CMD-006")
    doc.queue_action("custom_process"),
    doc.queue_action("custom_process2")
    # doc.queue_action("calculate_total_amount")

    frappe.db.commit()


# # -------------------------------------------------------------------------------------------------------------------------------------------------------

# @frappe.whitelist()
# def list_view():
#     data = frappe.db.get_list('Company Data')
#     return data

# @frappe.whitelist()
# def get_approved_companies():
#     return frappe.db.get_list('Company Data',
#         filters={'status': 'Approved'},
#         fields=['company_name', 'status']
#     )


# @frappe.whitelist()
# def single_value():
#     data = frappe.db.get_value('Company Data', 'CMD-001', 'company_name')
#     return data


# @frappe.whitelist()
# def set_single_value():
#     data = frappe.db.set_value('Company Data', 'CMD-002', 'company_name', "rahul")
#     return {"status": "success", "updated_value": data}

# @frappe.whitelist()
# def set_count_value():
#     data = frappe.db.count('Company Data', {'status': 'Approved'})
#     return data

# @frappe.whitelist()
# def delete_value():
#     data = frappe.db.delete('Company Data', {'status': 'Rejected'})
#     return data

# @frappe.whitelist()
# def commit_value():
#     data = frappe.db.set_value("Company Data", "CMD-001", "company_name", "Vijay")
#     frappe.db.commit()  # Now saved permanently
#     return data

# @frappe.whitelist()
# def set_single_value():
#     frappe.db.set_value("Company Data", "CMD-001", "status", "Approved")
#     frappe.db.rollback()
#     status = frappe.db.get_value("Company Data", "CMD-001", "status")
#     return f"Rollback done. Current status is still: {status}"

