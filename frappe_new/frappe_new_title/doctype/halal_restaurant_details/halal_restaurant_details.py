# Copyright (c) 2025, imran and contributors
# For license information, please see license.txt

import frappe
import re
from frappe.model.document import Document
from frappe.utils import format_time
from frappe.query_builder import DocType
from pypika.terms import Criterion

class HalalRestaurantDetails(Document):
    pass
def strip_html_tags(text):
    return re.sub('<[^<]+?>', '', text) if text else ""

@frappe.whitelist()
def show_restaurants():
    get_restaurants = frappe.db.get_all(
        "Halal Restaurant Details",
        fields=["name", "restaurant_name", "description__about_us", "opening_time", "closing_time", "restaurant_image"]
    )

    for restaurant in get_restaurants:
        restaurant["description__about_us"] = strip_html_tags(restaurant.get("description__about_us"))
        restaurant["restaurant_image"] = frappe.utils.get_url() + restaurant['restaurant_image']
    return get_restaurants

# @frappe.whitelist()
# def get_restaurant_with_foods(restaurant_name):
#     data = frappe.db.sql("""
#            SELECT 
#             a.name AS restaurant_id, 
#             a.restaurant_name,
#             a.description__about_us,
#             a.opening_time,
#             a.closing_time,
#             a.restaurant_image,
#             a.full_address,
#             a.contact_number,
#             b.food_name,
#             b.food_img
#            FROM `tabHalal Restaurant Details` a
#            LEFT JOIN `tabHalal Food List` b ON a.name = b.parent
#            WHERE a.restaurant_name = %s
#            """, (restaurant_name,), as_dict=True)
    
#     return data

@frappe.whitelist()
def get_restaurant_with_foods(restaurant_name):
    # restaurant = frappe.db.get_value(
    #     "Halal Restaurant Details",
    #     restaurant_name,
    #     ["name", 
    #     "restaurant_name",
    #     "description__about_us",
    #     "opening_time",
    #     "closing_time",
    #     "restaurant_image",
    #     "full_address",
    #     "contact_number"], as_dict=True)   
    # food_list = frappe.db.sql("""
    #     SELECT food_name, food_img
    #     FROM `tabHalal Food List`
    #     WHERE parent = %s
    # """, (restaurant_name), as_dict=True)

    # if restaurant:
    #     restaurant["description__about_us"] = strip_html_tags(restaurant.get("description__about_us"))
    #     restaurant["restaurant_image"] = frappe.utils.get_url() + restaurant['restaurant_image']
  
    # for food in food_list:
    #     if food.get("food_img"):
    #         food["food_img"] = frappe.utils.get_url() + food["food_img"]

    # return {
    #     "restaurant": restaurant,
    #     "foods": food_list
    # }
    
    HalalRestaurant = DocType("Halal Restaurant Details")
    HalalFoodList  = DocType("Halal Food List")

    restaurant_data = (
        frappe.qb
        .from_(HalalRestaurant)
        .select(
            HalalRestaurant.name,
            HalalRestaurant.restaurant_name,
            HalalRestaurant.description__about_us,
            HalalRestaurant.opening_time,
            HalalRestaurant.closing_time,
            HalalRestaurant.restaurant_image,
            HalalRestaurant.full_address,
            HalalRestaurant.contact_number
        )
        .where(HalalRestaurant.name == restaurant_name)
    ).run(as_dict=True)

    restaurant = restaurant_data[0]

    food_list = (
        frappe.qb.from_(HalalFoodList)
        .select(
            HalalFoodList.food_name,
            HalalFoodList.food_img
        )
        .where(HalalFoodList.parent == restaurant_name)
    ).run(as_dict=True)

    if restaurant:
        restaurant["description__about_us"] = strip_html_tags(restaurant.get("description__about_us"))
        restaurant["restaurant_image"] = frappe.utils.get_url() + restaurant['restaurant_image']
    for food in food_list:
        if food.get("food_img"):
            food["food_img"] = frappe.utils.get_url() + food["food_img"]

    return {
        "restaurant": restaurant,
        "foods": food_list
    }