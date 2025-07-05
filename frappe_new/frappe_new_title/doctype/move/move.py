# Copyright (c) 2025, imran and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document

class Move(Document):
    pass 

@frappe.whitelist()
def get_movies():
    # get_list data
    # movies = frappe.db.get_list("Move")
    # print(movies)
    # return movies 
# ------------------------------------------
    # with pluck
    # movies = frappe.db.get_list('Move', fields=["movie_name"] pluck='name')
    # print(movies)
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
    # print(movies)
    # return movies
# ------------------------------------------ 
# Tasks with date after 2019-09-08
    # movies = frappe.db.get_list(
    #     'Move',
    #     filters={
    #         'release_date': ['<', '2025-08-01']
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
    #         'movie_name': ['like', '%theri%']
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
# as dict
    # movies = frappe.db.get_value('Move', 'Move-008', ['movie_name', 'genre'], as_dict=True)
    # return movies
# ------------------------------------------ 
# with filters, will return the first record that matches filters
    #  movies = frappe.db.get_value('Move',{'genre': 'Fight'},['movie_name', 'genre'])
    #  return movies
# ------------------------------------------ 
# update a field value
    # movies = frappe.db.set_value('Move','Move-001','movie_name', 'Bahubali')
    # return movies
# ------------------------------------------ 
# update multiple values
    # movies = frappe.db.set_value('Move', 'Move-001',{'movie_name':'Maari', 'genre':'Action'})
    # return movies
# ------------------------------------------ 
# update without updating the `modified` timestamp
    # movies = frappe.db.set_value('Move', 'Move-001',{'movie_name':'Maari', 'genre':'Action'}, update_modified=False)
    # return movies
# ------------------------------------------ 
# Returns true if a document record exists.
# Tries to get result from Redis memory first =>cache avoid DB hit,speed up response,reduce load in production apps
    # movies = frappe.db.exists("Move", "Move-002", cache=True)
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
    #  movies = frappe.db.delete('Move', 'Move-004')
    #  return movies
# ------------------------------------------ 



