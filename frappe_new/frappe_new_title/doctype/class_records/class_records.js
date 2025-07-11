// Copyright (c) 2025, imran and contributors
// For license information, please see license.txt

frappe.ui.form.on("Class Records", {
	refresh(frm) {
      frm.add_custom_button('Scan QR', () => {
       new frappe.ui.Scanner({
          dialog: true, 
          multiple: false, 
          on_scan(data) {
             const scanned_value = data.decodedText;

             frm.set_value("qr_scanner", scanned_value)

             let is_external = scanned_value;

             let link_html = `<a href="${scanned_value}" ${is_external ? 'target="_blank"' : ''} style="color: blue; text-decoration: underline;">Go to Scanned Link</a>`;
             
             frappe.msgprint({
                title: "Scanned Code",
                indicator: "green",
                message: `Scanned Value: <b>${scanned_value}</b><br><br>${link_html}`
             });

          }
        });
      })
	},
});
