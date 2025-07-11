# Copyright (c) 2025, tharun and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class CompanyData(Document):
    def after_insert(self):
        print("Publishing event for:", self.company_name)
        frappe.publish_realtime(
            event='new_company_created',
            message={'company': self.company_name},
            user='*'  # Broadcast to all users
        )

    
    def custom_process(self):
        frappe.msgprint(f"Processing company: {self.company_name}")

    def calculate_total_amount(self):
        if self.amount and self.quantity:
            self.total_amount = self.amount * self.quantity
            self.save()
            frappe.msgprint(f"Total Amount calculated: {self.total_amount}")
        else:
            frappe.msgprint("Amount or Quantity is missing.")

    @frappe.whitelist()
    def greet(self):
        return "this is my message"
        
@frappe.whitelist()
def get_value():
    if frappe.db.exists("Company Data", "CMD-033"):
        doc = frappe.get_doc("Company Data", "CMD-033")
        return f"Document Found: {doc.company_name}"
    else:
        doc = frappe.get_doc({
            "doctype": "Company Data",
            "company_name": "NewCo"
        })
        doc.insert()
        return f"New Document Created: {doc.name}"

# @frappe.whitelist()	
# def get_value():
# 	doc = frappe.get_last_doc('Company Data')
# 	return f"Document Found: {doc.company_name}"
    
# @frappe.whitelist()
# def get_new_value():
# 	doc = frappe.new_doc('Company Data')
# 	doc.company_name= "Tharun"
# 	doc.description = "kjasfd"
# 	doc.insert()

# @frappe.whitelist()
# def get_new_value():
# 	meta = frappe.get_meta("Company Data")
# 	fields = [df.fieldname for df in meta.fields]
# 	return fields

# @frappe.whitelist()
# def update_company():
#     doc = frappe.get_doc("Company Data", "CMD-010")
#     doc.description = "Updated Description"
#     doc.status = "LogOut"
#     doc.save(ignore_permissions=True)
#     return f"{doc.name} updated successfully"

# @frappe.whitelist()
# def delete_company():
#     if frappe.db.exists("Company Data", "CMD-011"):
#         doc = frappe.get_doc("Company Data", "CMD-011")
#         doc.delete()
#         return f"doc deleted"
#     else:
#         return f"not found"


# @frappe.whitelist()
# def old_doc_message(docname):
#     doc = frappe.get_doc("Company Data", docname)
#     old_doc = doc.get_doc_before_save()

#     messages = []

#     if old_doc:
#         if old_doc.amount != doc.amount:
#             messages.append(f"Amount changed from {old_doc.amount} to {doc.amount}")
#         if old_doc.status != doc.status:
#             messages.append(f"Status changed from {old_doc.status} to {doc.status}")

#     return "\n".join(messages) if messages else "No changes detected."


@frappe.whitelist()
def has_price_changed(docname):
    doc = frappe.get_doc("Company Data", docname)
    old_amount = doc.total_amount

    if old_amount != 2400:
        doc.db_set('total_amount', 2400)
        # frappe.db.commit()
        return f"Total Amount changed from {old_amount} to 2400"
    else:
        return "Total Amount was already 2400"

@frappe.whitelist()
def add_contact(docname):
    doc = frappe.get_doc("Company Data", docname)


    # Append new contact
    doc.append("contact_person", {
        "contact_person": "Jane Smith",
        "email": "jane@company.com",
        "number": "9876543210"
    })

    doc.save()
    return "Contact added successfully"

@frappe.whitelist()
def get_url(docname):
    doc = frappe.get_doc("Company Data", docname)
    doc = frappe.get_doc("Company Data", "CMD-001")
    url = doc.get_url()
    return f"URL: {url}"

@frappe.whitelist()
def add_comment(docname):
    doc = frappe.get_doc("Company Data", docname)
    # Python - server side
    doc = frappe.get_doc("Company Data", "CMD-001")
    # Type: Comment
    comment = doc.add_comment('Comment', text='This is a new note.')
    frappe.db.commit()
    # Type: Edit
    doc.add_comment('Edit', 'Updated amount and quantity.')
    return f"{comment} added"


@frappe.whitelist()
def log_company_view(docname):
    doc = frappe.get_doc("Company Data", docname)
    doc = frappe.get_doc("Company Data", "CMD-001")


    # Mark as viewed and seen
    doc.add_viewed()
    doc.add_seen()

    # Add comment
    doc.add_comment('Comment', text='User opened the document.')

    return f"Document viewed: {doc.get_url()}"

@frappe.whitelist()
def method_test(docname):
    doc = frappe.get_doc("Company Data", "CMD-001")
    doc.run_method("custom_process")
    

@frappe.whitelist()
def queue_test(docname):
    doc = frappe.get_doc("Company Data", "CMD-012")
    doc.queue_action("calculate_total_amount")

    frappe.db.commit()


# -------------------------------------------------------------------------------------------------------------------------------------------------------

@frappe.whitelist()
def list_view():
    data = frappe.db.get_list('Company Data')
    return data

@frappe.whitelist()
def get_approved_companies():
    return frappe.db.get_list('Company Data',
        filters={'status': 'Approved'},
        fields=['company_name', 'status']
    )


@frappe.whitelist()
def single_value():
    data = frappe.db.get_value('Company Data', 'CMD-001', 'company_name')
    return data


@frappe.whitelist()
def set_single_value():
    data = frappe.db.set_value('Company Data', 'CMD-002', 'company_name', "rahul")
    return {"status": "success", "updated_value": data}

@frappe.whitelist()
def set_count_value():
    data = frappe.db.count('Company Data', {'status': 'Approved'})
    return data

@frappe.whitelist()
def delete_value():
    data = frappe.db.delete('Company Data', {'status': 'Rejected'})
    return data

@frappe.whitelist()
def commit_value():
    data = frappe.db.set_value("Company Data", "CMD-001", "company_name", "Vijay")
    frappe.db.commit()  # Now saved permanently
    return data

@frappe.whitelist()
def set_single_value():
    frappe.db.set_value("Company Data", "CMD-001", "status", "Approved")
    frappe.db.rollback()
    status = frappe.db.get_value("Company Data", "CMD-001", "status")
    return f"Rollback done. Current status is still: {status}"

