import frappe

@frappe.whitelist()
def get_actual_qty(product: str, location: str) -> float:
    """
    Return the current stock of *product* at *location* from Stock Balance.

    Called from Stock Movement Item (child table) when a product is picked.
    """
    qty = frappe.db.get_value("Stock Balance",{
        "product": product,
        "location": location},
        "actual_qty"                  
    )
    print(qty)

def handle_alert(doc, method=None):
    frappe.msgprint("This is a doc events alert")
   
@frappe.whitelist()
def get_fee_summary(month=None, class_section=None, status=None):
    filters = {}
    if month:
        filters["fee_month"] = month
    if class_section:
        filters["class"] = class_section
    if status:
        filters["status"] = status

    return frappe.get_all(
        "Std Fee Registration",
        filters=filters,
        fields=["fee_month", "class", "status", "name"]
    )