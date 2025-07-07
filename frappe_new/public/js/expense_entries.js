frappe.listview_settings['Expense Entry'] = {
    onload: function(listview) {
        listview.page.add_inner_button('Python Utiities', function() {
            frappe.call({
                method: "frappe_new.frappe_new_title.doctype.expense_entry.expense_entry.utilities",
                callback: function(r) {
                    if (r.message) {
                           window.open(r.message, "_blank"); 
                    }
                }
            });
        });
    }
};
