# Copyright (c) 2025, imran and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
# from frappe.utils import now,unique,random_string,validate_json_string,money_in_words,comma_and, today, add_days, format_duration, date_diff, cint, pretty_date, month_diff
from frappe.utils import now
from frappe.utils import getdate
from frappe.utils import today 
from datetime import datetime 
from frappe.utils import add_to_date
from frappe.utils import date_diff
from frappe.utils import days_diff
from frappe.utils import month_diff
from frappe.utils import pretty_date 
from frappe.utils import format_duration 
from frappe.utils import comma_and 
from frappe.utils import money_in_words 
from frappe.utils import validate_json_string 
from frappe.utils import random_string
from frappe.utils import unique 
from frappe.utils.pdf import get_pdf

class ExpenseEntry(Document):
	pass
@frappe.whitelist()
def utilities():
# Utility Functions 
# now()
    # data = now()
    # return data
# ----------------------------------------------------------------------------------------------------------------
# getdate 
    # data = getdate()
    # return data
# ----------------------------------------------------------------------------------------------------------------
# today 
    # data = today()
    # return data
# ----------------------------------------------------------------------------------------------------------------
# add_to_date calculate the current now()
    # today = datetime.now().strftime('%Y-%m-%d')
    # return today

	# after_10_days = add_to_date(datetime.now(), days=10, as_string=True)
	# return after_10_days

    # after_2_months = add_to_date(datetime.now(), months=2)
    # return after_2_months

	# after_10_days_datetime = add_to_date(datetime.now(), days=10, as_string=True, as_datetime=True)
	# return after_10_days_datetime

	# after_2_years = add_to_date(None, years=2)
	# return after_2_years
# ----------------------------------------------------------------------------------------------------------------
# date_diff today + 10 days =>date_diff(date_2, date_1)=>10
    # date_1 = today() 
    # date_2 = add_to_date(date_1, days=10)
    # date_diff_data = date_diff(date_2, date_1)
    # return date_diff_data
# ----------------------------------------------------------------------------------------------------------------
# days_diff days like mon,tue,wed
    # date_1 = today()
    # date_2 = add_to_date(date_1, days=10)
    # days_diff_data = days_diff(date_2, date_1)
    # return days_diff_data
# ----------------------------------------------------------------------------------------------------------------
# month_diff
    # date_1 = today()
    # date_2 = add_to_date(date_1, days=60)
    # month_diff_data = month_diff(date_2, date_1)
    # return month_diff_data
# ----------------------------------------------------------------------------------------------------------------
# pretty_date 
    # data = pretty_date(now())
    # return data
# ----------------------------------------------------------------------------------------------------------------
# format_duration 60 sec = 1 minutes, 5000 sec = 1h 23m 20s, 1000000 sec = 11d 13h 46m 40s ,1000000 sec = 277h 46m 40s 
    # format_duration_data = format_duration(120) 
    # return format_duration_data

	# format_duration_data = format_duration(5000)
	# return format_duration_data

	# format_duration_data = format_duration(1000000)
	# return format_duration_data

	# format_duration_data = format_duration(1000000, hide_days=True)
	# return format_duration_data
# ----------------------------------------------------------------------------------------------------------------
# comma_and 
    # comma_and_data = comma_and(['1','2','3','4'])
    # return comma_and_data

    # comma_and_data = comma_and(['Apple','Orange','Banana'], add_quotes=False)
    # return comma_and_data
 
    # comma_and_data = comma_and('abcd')
    # return comma_and_data 
# ----------------------------------------------------------------------------------------------------------------
# money_in_words 
    # money_in_data = money_in_words(50)
    # return money_in_data

	# money_in_data = money_in_words(500.50)
	# return money_in_data

    # money_in_data = money_in_words(900.50,'USD')
    # return money_in_data

    # money_in_data = money_in_words(900.50, 'USD', 'Cents')
    # return money_in_data
# ----------------------------------------------------------------------------------------------------------------
# validate_json_string 
    # json_data = '{"name":"imran", "age": "67" }'
    # json_validate = validate_json_string(json_data) 
    # return json_validate
# ----------------------------------------------------------------------------------------------------------------
# random_string
    # random_string_data = random_string(40)
    # return random_string_data

    # random_string_data = random_string(5)
    # return random_string_data
# ----------------------------------------------------------------------------------------------------------------
# unique 
    # unique_data = unique(['1','2','3','1','1','1','2'])
    # return unique_data

    # unique_data = unique('adgfdgfdhh')
    # return unique_data

	# unique_data = unique(('Apple', 'Apple', 'Banana', 'Apple'))
	# return unique_data
# ----------------------------------------------------------------------------------------------------------------
# get_pdf 
    # cart = {
    #     'Samsung Galaxy s20': 10,
    #     'iphone 13': 80,
    #     'Redmi 13C': 50,
    #     'Vivo': 40,
    #     'Nokia': 80
    # }

    # html = '<h1>Invoice from Star Electronics e-store!</h1><ol>'
    # for item, qty in cart.items():
    #     html += f'<li>{item} - {qty}</li>'
    # html += '</ol>'

    # pdf = get_pdf(html)
    # timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    # file_doc = frappe.get_doc({
    # 	"doctype": "File",
    # 	"file_name": f"invoice_{timestamp}.pdf",
    # 	"content": pdf,
    # 	"is_private": 0
    # }).insert(ignore_permissions=True)
    # return file_doc.file_url
    


















	