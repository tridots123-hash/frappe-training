frappe.pages['demo-page-'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Test',
		single_column: true
	});
	page.set_indicator('Pending', 'orange')
	let btn = page.set_secondary_action('Refresh', () => refresh(), 'octicon octicon-sync')


// add a standard menu item
	page.add_menu_item('Send Email', () => open_email_dialog(), true)

	page.add_action_item('Delete', () => delete_items())

	$(page.body).html(`
        <div class="my-ui-container" style="padding: 20px;">
            <h2 style="color: #4B4B4B;">Welcome to My Custom Page</h2>
            <p>This UI is rendered using HTML inside JavaScript.</p>

            <div class="row">
                <div class="col-md-4">
                    <div class="card" style="padding: 15px; background: #f9f9f9; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                        <h4>Card 1</h4>
                        <p>This is the first card.</p>
                        <button class="btn btn-primary">Action</button>
                    </div>
                </div>

                <div class="col-md-4">
                    <div class="card" style="padding: 15px; background: #eef6ff; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                        <h4>Card 2</h4>
                        <p>This is the second card.</p>
                        <button class="btn btn-success">Another Action</button>
                    </div>
                </div>
            </div>

            <div style="margin-top: 30px;">
                <input type="text" class="form-control" placeholder="Type something..." />
                <button class="btn btn-info mt-2">Submit</button>
            </div>
        </div>
		`);
}