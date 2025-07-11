// Copyright (c) 2025, tharun and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Company Data", {

//     setup(frm) {
//         frappe.msgprint("This is From Setup")
//     },

//     before_load(frm){
//         frappe.msgprint("This is From before_load")
//     },

//     onload(frm){
//         frappe.msgprint("This is From onload")
//     },
//     onload_post_render(frm){
//         frappe.msgprint("This is From onload_post_render")
//     },

//     validate(frm) {
//         if (frm.doc.amount && frm.doc.amount < 400) {
//             frappe.throw(`Amount cannot exceed 4. You entered: ${frm.doc.amount}`);
//         }
//     },

//     after_save(frm) {
//         if(frm.doc.company_name){
//             frappe.throw(`This is your company name ${frm.doc.company_name}`)
//         }

// 	},

//     before_discard(frm){
//         frappe.msgprint("this is from discard")
//     },

//     // timeline_refresh(frm){
//     //     frm.timeline.insert_comment("Alert", "This is from code")
//     // }
    
//     contact_person_on_form_rendered(frm, grid_row) {
//         frappe.msgprint("This is from child table row render.");
//     },

//     amount(frm){
//         frappe.msgprint(`${frm.doc.amount} is filled`)
//     }

// });


// frappe.ui.form.on("Company Contact", {
//     before_contact_person_remove(frm){
//         frappe.msgprint("row removed")
//     },

//     contact_person_add(frm){
//         frappe.msgprint("row added")
//     },

//     contact_person_move(frm){
//         frappe.msgprint("move")
//     },

//     form_render(frm){
//         frappe.msgprint("form render")                
//     }
// })



// function calculate_total(frm) {
//     if (frm.doc.amount && frm.doc.quantity) {
//         const total = frm.doc.amount * frm.doc.quantity;
//         frm.set_value('total_amount', total);
//     } else {
//         frm.set_value('total_amount', 0);
//     }

    
// }


// frappe.ui.form.on('Company Data', {
//     refresh: function(frm) {
//         frm.add_custom_button("Calculate", () => {
//             frm.call({
//                 method: "get_calculate",
//                 args: {
//                     amount: frm.doc.amount,
//                     quantity: frm.doc.quantity,
//                     name: frm.doc.name  // needed to access self
//                 },
//                 callback: function(r) {
//                     if (r.message !== undefined) {
//                         frm.set_value("total_amount", r.message);
//                         frappe.msgprint(`Total Amount Set: ${r.message}`);
//                     }
//                 }
//             });
//         }); 
//     }
// });


frappe.ui.form.on('Company Data', {
    refresh: function(frm) {
        frm.add_custom_button('Get Doc', function() {
            frappe.call({
                method: 'frappe_new.frappe_new_title.doctype.company_data.company_data.get_value',
                args: {
                    docname: frm.doc.name,
                },
                callback: function(r) {
                    if (r.message) {
                        frappe.msgprint(r.message);
                        frm.reload();
                    }
                }
            });
        });
    }
});

// database API
// frappe.ui.form.on('Company Data', {
//     refresh: function(frm) {
//         frm.add_custom_button('DB DOC', function() {
//             frappe.call({
//                 method: 'library_management.library_management.doctype.company_data.company_data.set_single_value',
//                 callback: function(r) {
//                     console.log(r.message);  // Logs list of documents
//                     frappe.msgprint("Check browser console for results");
//                 }
//             });
//         });
//     }
// });



frappe.ui.form.on('Company Data', {
    // refresh: function(frm) {
    //     frm.add_custom_button("Click", function () {
    //         frappe.call({
    //             method: "library_management.library_management.doctype.company_data.company_data.get_value",
    //             callback: function(r) {
    //                 if (r.message) {
    //                     frappe.msgprint(r.message);
    //                 }
    //             }
    //         });
    //     });
    // },


    

    refresh: function(frm){
        if(frm.is_new()){
            frm.add_custom_button("Present", ()=>{
                frappe.msgprint("Hiii")
            })
        }
    },

    refresh: function(frm) {
        if (frm.doc.description) {
            frm.set_intro('Please set the value', 'blue');
        }    
},


    before_save: function(frm){
        frm.refresh_field('description');
    },

    refresh: function(frm) {
        frm.set_df_property('description', 'reqd', 1);
        frm.remove_custom_button('Click');
        if (frm.doc.description === "test") {
            frm.doc.description = "Auto updated from script";
            frm.dirty(); // now form shows "Not Saved"
            frm.refresh_field('description');
        }
    }

    


});

// socket.io
frappe.ui.form.on('Company Data', {
    onload: function(frm) {
        frappe.realtime.on('amount_updated', function(data) {
            if (frm.doc.name === data.docname) {
                frappe.msgprint(`Amount changed to: ${data.amount}`);
                frm.reload_doc();
            }
        });
    }
});


console.log("company_data.js loaded");

frappe.realtime.on('new_company_created', function(data) {
    console.log("Realtime Event Triggered!");
    frappe.msgprint(__('New Company: ' + data.company));
});



frappe.listview_settings['Company Data'] = {
    formatters: {
        status(value) {
            if (value === 'Login') return '🟢 Login';
            if (value === 'LogOut') return '🔴 LogOut';
            if (value === 'Pending') return '🟡 Pending';
            if (value === 'Approved') return '✅ Approved';
            if (value === 'Rejected') return '❌ Rejected';
            return value;
        },                                      
        amount(value) {
            return `₹${parseFloat(value || 0).toFixed(2)}`;
        }
    }
};

frappe.ui.form.on('Company Data', {
    onload(frm) {
        frappe.meta.docfield_map['Company Data']['status'].formatter = function(value) {
            if (value === 'Login') return '🟢 Login';
            if (value === 'LogOut') return '🔴 LogOut';
            if (value === 'Pending') return '🟡 Pending';
            if (value === 'Approved') return '✅ Approved';
            if (value === 'Rejected') return '❌ Rejected';
            return value;
        };
    }
});
