# Copyright (c) 2025, tharun and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class CompanyDetails(Document):
	pass

@frappe.whitelist()
def calculate_total_amount_form(amount, quantity):
    try:
        amount = float(amount)
        quantity = int(quantity)
        total = amount * quantity
        return total
    except Exception as e:
        frappe.throw(f"Error calculating total: {str(e)}")
