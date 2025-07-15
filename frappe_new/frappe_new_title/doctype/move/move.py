# Copyright (c) 2025, imran and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document

class Move(Document):
    pass 

@frappe.whitelist()
def get_movies():
    # movies = frappe.db.get_list("Move")
    # return movies 
# ------------------------------------------
    # with pluck
    # movies = frappe.db.get_list('Move', pluck='name')
    # return movies
# ------------------------------------------ 
# Combining filters and other arguments:
    # movies = frappe.db.get_list('Move',
    #     filters={
    #         'genre': 'Fight'
    #     },
    #     fields=['name','movie_name', 'rating', 'genre', 'release_date'],
    #     order_by='name asc',
    #     start=2,
    #     page_length=3,
    #     as_list=True
    # )
    # return movies
# ------------------------------------------ 
# Tasks with date after 2019-09-08
    # movies = frappe.db.get_list(
    #     'Move',
    #     filters={
    #         'release_date': ['<=', '2025-07-31']
    #     },
    #     fields=['name', 'movie_name', 'rating', 'genre', 'release_date'],
    #     order_by='release_date asc'
    # )
    # return movies
# ------------------------------------------ 
# Tasks with date between 2025-07-05 and 2025-07-31 (both inclusive)
    # movies = frappe.db.get_list(
    #     'Move',
    #     filters=[
    #         ['release_date', 'between', ['2025-07-05', '2025-07-31']]
    #     ],
    #     fields=['name', 'movie_name', 'rating', 'genre', 'release_date'],
    #     order_by='release_date asc'
    # )
    # return movies
# ------------------------------------------ 
# Tasks with movie_name that contains "test"
    # movies = frappe.db.get_list(
    #     'Move',
    #     filters = {
    #         'movie_name': ['like', 'i%']
    #     },
    #     fields=['name', 'movie_name', 'rating', 'genre', 'release_date'],
    #     order_by='release_date asc'
    # )
    # return movies
# ------------------------------------------ 
# Count number of Move grouped by status
    # movies = frappe.db.get_list(
    #     'Move',
    #     fields=['count(genre) as count', 'genre'],
    #     group_by='genre'
    # )
    # return movies
# ------------------------------------------ 
# single value
    # movies = frappe.db.get_value('Move', 'Move-008', 'movie_name')
    # return movies
# ------------------------------------------ 
# multiple values
    # movie, genre = frappe.db.get_value('Move', 'Move-008', ['movie_name', 'genre'])
    # return movie, genre
# ------------------------------------------ 
# as dict =>with fieldname as list without fieldname
    # movies = frappe.db.get_value('Move', 'Move-008', ['movie_name', 'genre'], as_dict=True)
    # return movies
# ------------------------------------------ 
# with filters, will return the first record that matches filters
    #  movies = frappe.db.get_value('Move',{'genre': 'fight'},['movie_name', 'genre'])
    #  return movies
# ------------------------------------------ 
# update a field value
    # movies = frappe.set_value('Move','Move-001','movie_name', 'Maari')
    # return movies
# ------------------------------------------ 
# update multiple values
    # movies = frappe.db.set_value('Move', 'Move-001',{'movie_name':'Don', 'genre':'Action'})
    # return movies
# ------------------------------------------ 
# update without updating the `modified` timestamp
    # movies = frappe.db.set_value('Move', 'Move-001',{'movie_name':'Don', 'genre':'Comedy'}, update_modified=False)
    # return movies
# ------------------------------------------ 
# Returns true if a document record exists.
# Tries to get result from Redis memory first =>cache avoid DB hit,speed up response,reduce load in production apps
    # movies = frappe.db.exists("Move", "Move-022", cache=True)
    # return movies
# ------------------------------------------ 
# total number of Move records
    # movies = frappe.db.count('Move')
    # return movies
# ------------------------------------------ 
# total number of Action Move
    # movies = frappe.db.count('Move', {'genre': 'Comedy'})
    # return movies
# ------------------------------------------ 
# delete the filter records
    # movies = frappe.db.delete('Move', 'Move-002')
    # return movies
# ------------------------------------------ 
# frappe db sql raw query
    # movies = frappe.db.sql("""
    #      SELECT * FROM `tabMove`
    # """)
    # return movies
# ------------------------------------------ 
# frappe db multisql raw query
    # results = frappe.db.multisql({
    # "mariadb": [
    #     ("SELECT * FROM `tabMove`"),
    #     ("SELECT * FROM `tabClass Records`")
    # ]
    # })
    # print(results)
# ------------------------------------------ 
# Returns a tuple of the table description for given DocType.
    # results = frappe.db.describe('Move')
    # return results

    # results = frappe.db.add_unique("Move",["movie_name","genre"])
    # return results


