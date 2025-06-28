# Copyright (c) 2025, imran and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
	conditions = []
	if filters.get("month"):
		conditions.append(f"fee_month = '{filters.get('month')}'")
	if filters.get("class"):
		conditions.append(f"class = '{filters.get('class')}'")
    if filters.get("status"):
		conditions.append(f"status = '{filters.get('status')}'")

	where_clause = " and ".join(conditions)
	if where_clause:
		where_clause = f"WHERE {where_clause}"

	data = frappe.db.sql(f"""
	       SELECT 
		        fee_month, class, status, COUNT(name) as count
				FROM `tabStd Fee Registration`
				{where_clause}
				GROUP BY fee_month, class, status
	       """, as_dict=1)

	columns = [
		{"label": _("Month"), "fieldname": "fee_month", "fieldtype": "Data", "width":120},
		{"label": _("Class"), "fieldname": "class", "fieldtype": "Data", "width": 120},
        {"label": _("Status"), "fieldname": "status", "fieldtype": "Data", "width": 120},
        {"label": _("Count"), "fieldname": "count", "fieldtype": "Int", "width": 100},
	]	   
	return columns, data
