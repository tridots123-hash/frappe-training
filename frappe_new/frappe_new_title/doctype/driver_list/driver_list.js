// Copyright (c) 2025, imran and contributors
// For license information, please see license.txt

frappe.ui.form.on("Driver List", {
	refresh(frm) {
    //    frm.add_custom_button('Get Route', () => {
    //        let route = frappe.get_route();
    //        let Driver_id = route[2];
    //        frappe.call({
    //            method: "frappe_new.frappe_new_title.doctype.driver_list.driver_list.get_diver_info",
    //            args: {
    //                Driver_id: Driver_id
    //            },
    //            callback: function(res) {
    //                  msgprint("Driver Info: " + JSON.stringify(res.message));
    //            }
    //        })
    //    })
// # ------------------------------------------------------------------------------------------
    //    frm.add_custom_button('Set Route', () => {
    //     //    frappe.set_route('List', 'Driver List', 'List'); 
    //     //    frappe.set_route(['Form', 'Driver List', 'LIC-002'])
    //     //    frappe.set_route('List/Driver List/List')
    //     //    frappe.set_route('List', 'Driver List', 'List', { status: 'Close' })
    //    })
// # ------------------------------------------------------------------------------------------
    //   frm.add_custom_button('Utilities format Date', () => {
    //        let route = frappe.get_route();
    //        let Driver_id = route[2];
    //        frappe.call({
    //            method: "frappe_new.frappe_new_title.doctype.driver_list.driver_list.get_diver_info",
    //            args: {
    //            Driver_id: Driver_id
    //         },
    //         callback: function(res) {
    //             if (res.message) {
    //                 let data = res.message;
    //                 let formatted_date = data.joining_date
    //                     ? frappe.format(data.joining_date, {fieldtype: "Date"})
    //                     : "N/A";
    //                 let msg = `
    //                    <b>Driver Name:</b> ${data.Driver_List || 'N/A'}<br>
    //                    <b>Joining Date:</br> ${formatted_date}
    //                 `;
    //                 frappe.msgprint(msg)
    //             }
    //         }
    //        })
    //   })
// # ------------------------------------------------------------------------------------------       
    //  frm.add_custom_button('Utilities format Amount', () => {
    //        let route = frappe.get_route();
    //        let Driver_id = route[2];
    //        frappe.call({
    //             method: "frappe_new.frappe_new_title.doctype.driver_list.driver_list.get_diver_info",
    //             args: {
    //                 Driver_id: Driver_id
    //             },
    //             callback: function(res) {
    //                 if (res.message) {
    //                     let data = res.message;
    //                     let formatted_amount = data.salary
    //                         ? frappe.format(data.salary, {fieldtype: "Currency"}, { inline: true })
    //                         : "N/A";
    //                     let msg = `
    //                         <b>Driver Name:</b> ${data.Driver_List || 'N/A'} <br>
    //                         <b>Salary:</b> ${formatted_amount}
    //                     `;
    //                     frappe.msgprint(msg);
    //                 }
    //             }
    //        })
    //  })
// # ------------------------------------------------------------------------------------------
    // frm.add_custom_button('frappe provide', () => {
    //     let a = 20;
    //     let b = 10;
    //     let result = frappe.frappe_new.provider.add_numbers(a, b);
    //     frappe.msgprint("result:" + result)
    // });
// # ------------------------------------------------------------------------------------------
    // frappe.require is used to dynamically load JS or CSS files 
        // frm.add_custom_button('Frappe Require', () => {
        // frappe.require('/assets/frappe_new/js/Require.js', function() {
        //     show_alert_message() 
        //     })
        // })
//# ------------------------------------------------------------------------------------------
    // frm.add_custom_button('Send Email', () => {
    //     frappe.call({
    //         method: "frappe_new.frappe_new_title.doctype.driver_list.driver_list.send_email",
    //         args: {
    //             docname: frm.doc.name
    //         },
    //         callback: function(res) {
    //             if (res.message) {
    //                 if (res.message == "success") {
    //                     frappe.msgprint("Email sent successfully!");
    //                 } else {
    //                     frappe.msgprint("Failed to send email.");
    //                 }
    //             }
    //         }
    //     })
    // })
// ------------------------------------------------------------------------------------------------------------------------------------------------
// server.call(ajax)
// call with no parameters
// frm.add_custom_button('call with para', () => {
//     frappe.call('ping')
//     .then(r => {
//         console.log(r)
//     })
// })
// ------------------------------------------------------------------------------------------
// call with a single parameter
// frm.add_custom_button('single parameter', () => {
//     frappe.call('frappe_new.frappe_new_title.doctype.driver_list.driver_list.single_parameter', {
//         role_profile: 'Test',
//         person: "Test2"
//     }).then(r => {
//         frappe.msgprint(r.message)
//     })
// })
// ------------------------------------------------------------------------------------------
// call with all options
// frm.add_custom_button('options', () => {
//     frappe.call({
//         method:'frappe_new.frappe_new_title.doctype.driver_list.driver_list.options',
//         args:{
//             role_profile: 'Test'
//         },
//         freeze: true,
//         btn: $('.primary-action'),
//         callback: function(r) {
//             if(r.message){
//                frappe.msgprint(r.message)
//             }
//         },
//         error: function() {
//             frappe.msgprint("Not Found")
//         }
//     })
// })
// ------------------------------------------------------------------------------------------
// frappe.db.get_doc 
//  frm.add_custom_button('get_doc', () => {
//     frappe.db.get_doc('Driver List')
//     .then(doc => {
//         console.log("This is frontend call in get_doc:",doc)
//     })
//  })
//  frappe.db.get_doc filters
// frm.add_custom_button('get_doc', () => {
//     frappe.db.get_doc('Driver List', null, { status: 'close' })
//     .then(doc => {
//      console.log(doc)
//    })
// })
// frappe.db.get_list
// frm.add_custom_button('get_list', () => {
//  frappe.db.get_list('Driver List', { fields: ['driver_email', 'driver_name', 'status'], filters: { status: 'open' }})
//  .then(doc => {
//      console.log(doc)
//  })
// })
// frappe.db.get_value single value
//   frm.add_custom_button('get_single_value', () => {
//       frappe.db.get_value('Driver List', 'LIC-005', 'status')
//       .then(doc => {
//          console.log(doc)
//       })
//   })
// frappe.db.get_value Multiple value
//  frm.add_custom_button('get_multi_value', () => {
//      frappe.db.get_value('Driver List', 'LIC-005', ['status', 'driver_email'])
//      .then(doc => {
//         console.log(doc.message.status, doc.message.driver_email)
//      })
//  })
// frappe.db.get_value filter
//    frm.add_custom_button('get_filter_value', () => {
//       frappe.db.get_value('Driver List', {status: 'close'}, 'driver_email')
//       .then(doc => {
//           console.log(doc.message.driver_email)
//       })
//    })
// frappe.db.get_single_value
//    frm.add_custom_button('get_single_value', () => {
//     frappe.db.get_single_value('Driver List', 'driver_email')
//     .then(doc => {
//       console.log(doc);
//     });
//    })
// frappe.db.set_value update a field's value
//    frm.add_custom_button('set_value', () => {
//      frappe.db.set_value('Driver List', 'LIC-001', 'status','Open')
//      .then(doc => {
//         console.log(doc.message)
//      })
//    })
// frappe.db.set_value update multiple fields
//   frm.add_custom_button('set_multiple_value', () => {
//     frappe.db.set_value('Driver List', 'LIC-001', {'status':'Open', 'salary': 50000 })
//     .then(doc => {
//         console.log(doc.message)
//     })
//   })
// frappe.db.insert new document
//    frm.add_custom_button('insert', () => {
//       frappe.db.insert({
//         doctype: 'Driver List', 
//         driver_name: 'Thoufeeq',
//         driver_email: 'thoufeeq@gmail.com',
//         license_name: 'LOC567774665',
//         phone_number: 6789567867,
//         joining_date: '2025-07-20',
//         status: 'Close',
//         salary: 30000
//     })
//       .then(doc => {
//         console.log(doc.message)
//       })
//    })
// frappe.db.count total number of Task records
    //  frm.add_custom_button('count_records', () => {
    //     frappe.db.count('Driver List')
    //     .then(count => {
    //         console.log(count)
    //     })
    //  })
// frappe.db.count filtering total status records
//    frm.add_custom_button('filter_count', () => {
//    frappe.db.count('Driver List', {filters: {status: 'Open'}
//    }).then(count => {
//       console.log("Open Drivers:", count);
//    });
//    })
// frappe.db.delete_doc delete the particular records
    // frm.add_custom_button('Delete_doc', () => {
    // frappe.db.delete_doc('Driver List', 'LIC-006')
    // .then(result => {
    //     console.log(result)
    // })
    // })
// frappe.db.exists check the existing records
    // frm.add_custom_button('Existing', () => {
    //    frappe.db.exists('Driver List', 'LIC-006')
    //    .then(exist => {
    //        console.log(exist)
    //    })
    // })
    },
});
