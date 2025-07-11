import frappe
import random

def push_disease_chart_data():
    fever_count = random.randint(1, 10)
    cold_count = random.randint(1, 10)

    data = {
        'label': frappe.utils.nowtime(),
        'points': [fever_count, cold_count]
    }

    # This event name should match what your JS listens to
    frappe.publish_realtime('disease_realtime_event', data)