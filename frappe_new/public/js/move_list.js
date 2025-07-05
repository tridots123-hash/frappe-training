frappe.listview_settings['Move'] = {
    onload: function(listview) {
        listview.page.add_inner_button('Load Movies', function() {
            frappe.call({
                method: "frappe_new.frappe_new_title.doctype.move.move.get_movies",
                callback: function(r) {
                    if (r.message) {
                        console.log(r.message)
                    }
                }
            });
        });
    }
};
