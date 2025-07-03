frappe.ready(function() {

	frappe.web_form.on('amount', (field, value)=>{
		let qty = frappe.web_form.get_value('quantity')
		frappe.web_form.set_value('total_amount', value * qty)
	})
	frappe.web_form.on('quantity', (field, value) => {
        let amt = frappe.web_form.get_value('amount') || 0;
        frappe.web_form.set_value('total_amount', value * amt);
    });

	frappe.web_form.on('status', (field, value)=>{
		frappe.msgprint('You selected status: '+ value)
	})


	frappe.web_form.set_df_property('total_amount', 'read_only', 1);

	frappe.web_form.validate = () => {
    let amount = frappe.web_form.get_value('amount');
    let qty = frappe.web_form.get_value('quantity');

    if (!amount || !qty) {
        frappe.msgprint("Amount and Quantity are required!");
        return false;
    }

    if (qty <4) {
        frappe.msgprint("Quantity cannot be less then  4");
        return false;
    }

	frappe.web_form.after_load = () => {
		frappe.msgprint("Web form loaded successfully!");

	}

    return true;
};

// frappe.web_form.validate = () => {
//     let contacts = frappe.web_form.get_value("contact_person") || [];

//     // Loop through the child table rows
//     contacts.forEach(row => {
//         if (row.contact_person && row.contact_person.toLowerCase() === "john") {
//             row.email = "john@gmail.com";
//         }
//     });

//     // Set the modified child table back to the form
//     frappe.web_form.set_value("contact_person", contacts);

//     return true; // allow save
// };

})

//  body {
//             background-color: #f4f4f9;
//         }

//         .web-form .form-control {
//             border: 2px solid #007bff;
//             border-radius: 6px;
//         }

//         .web-form .form-section {
//             background: #e9f5ff;
//             padding: 15px;
//             border-radius: 10px;
//             margin-bottom: 20px;
//         }

//         .web-form .btn-primary {
//             background-color: #0056b3;
//             border: none;
//         }

//         .web-form .btn-primary:hover {
//             background-color: #004494;
//         }