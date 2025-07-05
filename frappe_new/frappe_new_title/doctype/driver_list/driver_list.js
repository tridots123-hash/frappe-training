// Copyright (c) 2025, imran and contributors
// For license information, please see license.txt

frappe.ui.form.on("Driver List", {
	refresh(frm) {
       frm.add_custom_button('Get Route', () => {
           let route = frappe.get_route();
           let Driver_id = route[2];
           console.log(route)
           frappe.call({
               method: "frappe_new.frappe_new_title.doctype.driver_list.driver_list.get_diver_info",
               args: {
                   Driver_id: Driver_id
               },
               callback: function(res) {
                     msgprint("Driver Info: " + JSON.stringify(res.message));
               }
           })
       })
// # ------------------------------------------------------------------------------------------
    //    frm.add_custom_button('Set Route', () => {
    //     //    frappe.set_route('List', 'Class Records', 'List'); 
    //     //    frappe.set_route(['Form', 'Driver List', 'List'])
    //     //    frappe.set_route('List/Driver List/List')
    //     //    frappe.set_route('List', 'Driver List', 'List', { status: 'open' })
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
    //                 let formatted_date = data.joining_date ? frappe.format(data.joining_date, {fieldtype: "Date"}) : "N/A";
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
    //     let result = add_numbers(a, b);
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
//     frappe.db.get_doc('Driver List', frm.doc.name)
//     .then(doc => {
//         console.log("This is frontend call in get_doc:",doc)
//     })
//  })
//  frappe.db.get_doc filters
// frm.add_custom_button('get_doc', () => {
//     frappe.db.get_doc('Driver List',  frm.doc.name, { status: 'close' })
//     .then(doc => {
//      console.log(doc)
//    })
// })
// frappe.db.get_list
// frm.add_custom_button('get_list', () => {
//  frappe.db.get_list('Driver List', { fields: ['*'], filters: { status: 'close' }})
//  .then(doc => {
//      console.log(doc)
//  })
// })
// frappe.db.get_value single value
//   frm.add_custom_button('get_single_value', () => {
//       frappe.db.get_value('Driver List', 'LIC-001', 'status')
//       .then(doc => {
//          console.log(doc)
//       })
//   })
// frappe.db.get_value Multiple value
//  frm.add_custom_button('get_multi_value', () => {
//      frappe.db.get_value('Driver List', 'LIC-001', ['status', 'driver_email'])
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
//     frappe.db.get_single_value('Driver List','driver_email')
//     .then(doc => {
//       console.log(doc);
//     });
//    })
// frappe.db.set_value update a field's value
//    frm.add_custom_button('set_value', () => {
//      frappe.db.set_value('Driver List', 'LIC-003', 'status','Open')
//      .then(doc => {
//         console.log(doc.message)
//      })
//    })
// frappe.db.set_value update multiple fields
//   frm.add_custom_button('set_multiple_value', () => {
//     frappe.db.set_value('Driver List', 'LIC-001', {'status':'Close', 'salary': 80000 })
//     frm.reload_doc()
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
// ------------------------------------------------------------------------------------------
// Javascript Dialog API
// Full control, Multiple customizations, Suitable for complex forms, Manual show/hide	
// frappe.ui.Dialog 
// frm.add_custom_button('Dialog API', () => {
//    let d = new frappe.ui.Dialog({
//      title: 'Driver Details',
//      fields: [
//          {
//              label: 'First Name',
//              fieldname: 'first_name',
//              fieldtype: 'Data'
//          },
//          {
//              label: 'Last Name',
//              fieldname: 'last_name',
//              fieldtype: 'Data'
//          },
//          {
//              label: 'Age',
//              fieldname: 'age',
//              fieldtype: 'Int'
//          }
//      ],
//      size: 'small',
//      primary_action_label: 'Submit',
//      primary_action(values) {
//          console.log("this is value:",values);
//          d.hide();
//      }
//    });
//    d.show();
//  })
// ------------------------------------------------------------------------------------------
// frappe.ui.Dialog liked doctype
// frm.add_custom_button('Open Dialog', () => {
//         let dialog = new frappe.ui.Dialog({
//             title: 'Enter Your Details',
//             fields: [
//                 { label: 'Doctype Name', fieldname: 'mobile', fieldtype: 'Data' },
//                 { label: 'Department', fieldname: 'department', fieldtype: 'Link', options: 'Class Records' }
//             ],
//             primary_action_label: 'Save',
//             primary_action(values) {
//                 console.log('User Input:', values);
//                 frappe.msgprint('Saved: ' + values.mobile);
//                 dialog.hide();
//             }
//         });
//         dialog.show();
//     });
// ------------------------------------------------------------------------------------------
//    msgprint
    // frm.add_custom_button('msgprint', () => {
        // frappe.msgprint(__('Document updated successfully'));

        //   frappe.msgprint({
        //   title: __('Important message'),
        //   indicator: 'yellow',
        //   message: __('Document updated successfully')
        
        //   frappe.msgprint({
        //   title: 'Confirm',
        //   message: 'Are you sure you want to proceed?',
        //   primary_action_label: 'Yes', 
        //   primary_action: {
        // //      action() {
        //            console.log('this action message')
        //             }
        //       }
        //   }
        //   });
// });
// msgprint server and client call
// frm.add_custom_button('server action', () => {
//     frappe.msgprint({
//         title: 'Warning!',
//         message: 'Active the server side call',
//         primary_action: {
//             label: 'Delete',
//             server_action: 'frappe_new.frappe_new_title.doctype.driver_list.driver_list.server_action',
//             args: {
//                 doc_name: 'LIC-007'
//             },
//             callback: function(r) {
//                 if(r.message) {
//                     console.log(r.message)
//                 }
//             }
//         }
//     });
// })
// frm.add_custom_button('client action', () => {
//      frappe.msgprint({
//         title: 'Warning!',
//         message: 'Active the client side call',
//         primary_action: {
//             label: 'action',
//             client_action: 'frappe.frappe_new.provider.alert',
//             args: {
//                 name: 'alert this'
//             }
//         }
//      })
// })
// ------------------------------------------------------------------------------------------
// frappe.prompt() is a shortcut method to show a quick popup with some input fields — without creating full frappe.ui.Dialog manually.
	// Quick input, Simple use case, Suitable for 1–2 fields only, Auto show, auto hide
    // frm.add_custom_button('prompt', () => {
    // frappe.prompt('Last Name', ({value}) => console.log(value))
    // frappe.prompt('Last Name', console.log, 'Enter last Name', 'Submit');
    // frappe.prompt({
    //     label: 'Birth Date',
    //     fieldname: 'date',
    //     fieldtype: 'Date'
    // }, (values) => {
    //     console.log(values.date)
    // })
// ------------------------------------------------------------------------------------------
    // frappe.prompt([
    //      {
    //         label: 'Enter your name',
    //         fieldname: 'name',
    //         fieldtype: 'Data',
    //         reqd: 1
    //      }
    // ],(values) => {
    //         console.log(values.name);
    //         frappe.msgprint('Hello ' + values.name)}, 
    //         'User Info', // title
    //         'Submit'    // button text
    // );
// ------------------------------------------------------------------------------------------
    // frappe.prompt([
    //     {
    //         label: 'Status',
    //         fieldname: 'status',
    //         fieldtype: 'Select',
    //         options: 'Open\nIn Progress\nClosed',
    //         reqd: 1
    //     }],
    //      (values) => {
    //          frappe.db.set_value('Driver List', frm.doc.name, 'status', values.status)
    //              .then(() => {
    //                  frappe.msgprint('Status updated to ' + values.status);
    //                  frm.reload_doc();
    //              });
    //      },
    //      'Update Status',
    //      'Set'
    //      );
    // })
// ------------------------------------------------------------------------------------------
	// Ask for confirmation (Yes/No), Simple popup, Regular confirmation, ❌ Only one message
    // frm.add_custom_button('Confirm', () => {
    //     frappe.confirm('Are you sure you want to proceed?',
    //     () => {
    //       console.log('You onclick the Yes Button')
    //     }, () => {
    //       console.log('You onclick the No Button')
    //    })
    // })
// ------------------------------------------------------------------------------------------
//    Warn the user with a strong message, Visually stronger (red warning look), Risky or critical actions, Can show both title and sub description
    // frm.add_custom_button('Warn', () => {
    //     frappe.warn('This action is irreversible!',
    //           'Do you really want to delete this?',
    //            () => {
    //            console.log('Proceeding with deletion');
    //     },() => {
    //     console.log('Action cancelled');
    // }
    // );
    // })
// ------------------------------------------------------------------------------------------
    // frm.add_custom_button('show_alert', () => {
        // frappe.show_alert('Hi, you have a new message', 5) 
        // 5 This is for How long the alert box stays visible (in seconds)
        // setInterval(()=>{
        //     frappe.show_alert('Hi, you have a new message', 5) 
        // },60000)
        // 60000 sec = 1 minutes
        // frappe.show_alert({
        //     message:__('Hi, you have a new message'),
        //     indicator:'green'
        // }, 5)
    // })
// ------------------------------------------------------------------------------------------
//    frm.add_custom_button('show_progress', () => {
//        frappe.show_progress('Loading..', 70, 100, 'Please wait');
//    })
// ------------------------------------------------------------------------------------------
// This only creates the document in memory, but it won’t navigate (route) to the form.
// frm.add_custom_button('new_doc', () => {
//     frappe.prompt([
//         { label: 'Driver Name', fieldname: 'driver_name', fieldtype: 'Data', reqd: 1 },
//         { label: 'License No', fieldname: 'license_name', fieldtype: 'Data' }
//     ], 
//     (values) => {
//         let doc = frappe.model.get_new_doc('Driver List');
//         doc.driver_name = values.driver_name;
//         doc.license_name = values.license_name;
//         frappe.set_route('Form', 'Driver List', doc.name);
//     }, 
//     'Create New Driver', 'Create'
//     );
// })
// ------------------------------------------------------------------------------------------
//  frm.add_custom_button('Select Employees', () => {
//         new frappe.ui.form.MultiSelectDialog({
//             doctype: "Employee",
//             target: frm,
//             setters: {
//                 department: frm.doc.name  // Filter employees of this dept
//             },
//             add_filters_group: 1,
//             action(selections) {
//                 console.log("Selected Employees:", selections);
//                 frappe.msgprint("You selected " + selections.length + " employee(s)");
//                 // Do something with selected employee names (selections is an array of names)
//             },
//             primary_action_label: "Add Employees"
//         });
//      });
    },
});



