frappe.pages['amazon'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'this is Amazon page',
		single_column: true
	});
}