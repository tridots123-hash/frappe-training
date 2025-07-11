# Copyright (c) 2025, imran and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import nowdate
import random
from frappe import msgprint

class SalesCount(Document):
    pass

def create_random_sales_entry():
    item_list = ['iphone', 'ipad', 'macbook']
    for item in item_list:
        doc = frappe.get_doc({
            'doctype': 'Sales Count',
            'item_name': item,
            'count': random.randint(10, 100),
            'date': nowdate()
        })
        doc.insert(ignore_permissions=True)

@frappe.whitelist()
def get_chart_data():
    data = {
        "key": "value"
    }
    frappe.publish_realtime('event_name', data)



