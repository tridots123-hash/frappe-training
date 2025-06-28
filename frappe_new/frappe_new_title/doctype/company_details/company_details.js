// Copyright (c) 2025, tharun and contributors
// For license information, please see license.txt




// frappe.ui.form.on('Company Details', {
// 	refresh(frm) {
// 		frappe.msgprint("Hi, I'm coming ")
// 	}
// })


// frappe.ui.form.on('Company Details', {
// 	before_save(frm){
// 	   console.log("im here")
// 	}
// })



// frappe.ui.form.on('Company Details', {

//     refresh : function(frm){
//         frm.add_custom_button('Change', function(){
//             frm.set_value("description", "Good")
//         })
//     }
// })


// frappe.ui.form.on('Company Details', {
//     refresh: function(frm) {
//         // Always hide the status field initially
//         frm.set_df_property('status', 'hidden', 0);
//         frm.clear_custom_buttons();

//         if (!frm.doc.status || frm.doc.status === 'LogOut') {
//             frm.add_custom_button('Check In', function() {
//                 frm.set_value('status', 'Login');
//                 // Show the field after setting value
//                 frm.set_df_property('status', 'hidden', 0);
//                 frm.refresh_field('status');
//                 frappe.msgprint('Login');
//             }, 'Actions');
//         }

//         if (frm.doc.status === 'Login') {
//             frm.set_df_property('status', 'hidden', 0); // Show field if already login
//             frm.refresh_field('status');

//             frm.add_custom_button('Check Out', function() {
//                 frm.set_value('status', 'LogOut');
//                 frm.set_df_property('status', 'hidden', 0);
//                 frm.refresh_field('status');
//                 frappe.msgprint('LogOut');
//             }, 'Actions');
//         }
//     }
// });

// frappe.ui.form.on('Company Details', {
//     refresh: function(frm) {
//         // Add a button to calculate total amount
//         frm.add_custom_button('Calculate Total Amount', function() {
//             if (frm.doc.amount && frm.doc.quantity) {
//                 const total = frm.doc.amount * frm.doc.quantity;
//                 frm.set_value('total_amount', total);
//                 frappe.msgprint(`Total Amount calculated: ₹${total}`);
//             } else {
//                 frappe.msgprint('Please enter both Amount and Quantity.');
//             }
//         }); // Optional: You can group it under 'Actions'
//     }
// });



// frappe.ui.form.on('Company Details', {
//     // Triggered when Amount or Quantity is changed
//     amount: function(frm) {
//         if (frm.doc.amount && frm.doc.quantity) {
//         const total = frm.doc.amount * frm.doc.quantity;
//         frm.set_value('total_amount', total);
//     } else {
//         frm.set_value('total_amount', 0);
//     }
//     },
//     quantity: function(frm) {
//         if (frm.doc.amount && frm.doc.quantity) {
//         const total = frm.doc.amount * frm.doc.quantity;
//         frm.set_value('total_amount', total);
//     } else {
//         frm.set_value('total_amount', 0);
//     }
//     }
// });

// function calculate_total(frm) {
//     if (frm.doc.amount && frm.doc.quantity) {
//         const total = frm.doc.amount * frm.doc.quantity;
//         frm.set_value('total_amount', total);
//     } else {
//         frm.set_value('total_amount', 0);
//     }
// }


// frappe.ui.form.on('Company Details', {
//     amount :function(frm){
//         frappe.msgprint(`Amount changed to: ${frm.doc.amount}`);
//     }
// })

// frappe.ui.form.on('Company Details', {
//     refresh: function(frm) {
//         // Always hide the status field initially
//         frm.set_df_property('status', 'hidden', 1);
//         frm.clear_custom_buttons();

//         // If status is empty or LogOut, show "Check In" button
//         if (!frm.doc.status || frm.doc.status === 'LogOut') {
//             frm.add_custom_button('Check In', function() {
//                 frm.set_value('status', 'Login');
//                 frm.set_df_property('status', 'hidden', 0);
//                 frm.refresh_field('status');
//                 frappe.msgprint('Login');
//             }, 'Actions');
//         }

//         // If already logged in, show status and "Check Out" button
//         if (frm.doc.status === 'Login') {
//             frm.set_df_property('status', 'hidden', 0);
//             frm.refresh_field('status');

//             frm.add_custom_button('Check Out', function() {
//                 frm.set_value('status', 'LogOut');
//                 frm.set_df_property('status', 'hidden', 0);
//                 frm.refresh_field('status');
//                 frappe.msgprint('LogOut');

//                 // Cancel the document only if it's submitted
//                 if (frm.doc.docstatus === 1) {
//                     frm.save('Cancel');
//                 }
//             }, 'Actions');
//         }
//     }
// });


frappe.ui.form.on('Company Details', {
    onload: function(frm) {
        toggle_company_name_editable(frm);
    },

    refresh: function(frm) {
        toggle_company_name_editable(frm);
    },

    allow_edit_name: function(frm) {
        toggle_company_name_editable(frm);
    },

    after_save: function(frm) {
        toggle_company_name_editable(frm);
    }
});

function toggle_company_name_editable(frm) {
    if (frm.is_new()) {
        // Allow editing if new document
        frm.set_df_property('company_name', 'read_only', 0);
    } else {
        // If checkbox is checked, allow editing
        if (frm.doc.allow_edit_name == 1) {
            frm.set_df_property('company_name', 'read_only', 0);
        } else {
            // Otherwise, make it read-only after save
            frm.set_df_property('company_name', 'read_only', 1);
        }
    }
    frm.refresh_field('company_name');
}


    //     frm.set_df_property('company_name', 'read_only', 0);
     
    //     // If checkbox is checked, allow editing
    //     if (frm.doc.allow_edit_name == 1) {
    //         frm.set_df_property('company_name', 'read_only', 0);
    //     } else {
    //         // Otherwise, make it read-only after save
    //         frm.set_df_property('company_name', 'read_only', 1);
    //     }
    
    // frm.refresh_field('company_name');

    // }


frappe.ui.form.on('Company Contact', {
    contact_person: function (frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        console.log(row);
        console.log(cdt);
        console.log(cdn);
        if (row.contact_person === 'John') {
            frappe.model.set_value(cdt, cdn, 'email', 'john@example.com');
        } else if (row.contact_person === 'Jane') {
            frappe.model.set_value(cdt, cdn, 'email', 'jane@example.com');
        } else {
            frappe.model.set_value(cdt, cdn, 'email', '');
        }
    }
});


frappe.ui.form.on('Company Details', {
    refresh: function(frm) {
        frm.add_custom_button('Calculate Total', function() {
            frappe.call({
                method: 'frappe_new.frappe_new_title.doctype.company_details.company_details.calculate_total_amount_form',
                args: {
                    amount: frm.doc.amount,
                    quantity: frm.doc.quantity
                },
                callback: function(r) {
                    if (r.message !== undefined) {
                        frm.set_value('total_amount', r.message);
                        frappe.msgprint(`Total Amount: ${r.message}`);
                    }
                }
            });
        });
    }
});



// FORM SCRIPT

// frappe.listview_settings['Company Details'] = {
//     onload: function (listview) {
//         listview.page.add_inner_button('Click Me', function () {
//             frappe.msgprint('Hi from List View!');
//         });
//     }
// };


// frappe.listview_settings['Company Details'] = {
//     onload: function(listview) {
//         listview.page.add_button('Mark All as Logout', () => {
//             frappe.call({
//                 method: "frappe.client.set_value",
//                 args: {
//                     doctype: "Company Details",
//                     name: cur_list.data[0].name, // apply only to first item for now
//                     fieldname: {
//                         "status": "LogOut"
//                     }
//                 },
//                 callback: function() {
//                     frappe.msgprint("Updated to LogOut");
//                     listview.refresh();
//                 }
//             });
//         });
//     }
// };


