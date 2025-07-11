frappe.pages['chart-realtime-update'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Sales Count',
		single_column: true
	});

	wrapper.innerHTML += `<div id="chart" style="margin-top: 20px; height: 300px;"></div>`;

	const data = {
		labels: [],
		datasets: [{
			name: "Sales",
			values: []
		}]
	};

	const chart = new frappe.ui.RealtimeChart("#chart", "disease_realtime_event", 10, {
		title: "Sales Count",
		data: data,
		type: 'bar',
		height: 300,
		colors: ["#ff6f69"]
	});

	chart.start_updating();

	frappe.realtime.on('event_name', (data) => {
    console.log(data)
    })
};


	// frappe.call({
	// 	method: "frappe_new.frappe_new_title.doctype.sales_count.sales_count.get_chart_data",
	// 	callback: function(r) {
	// 		if (r.message) {
	// 			 window.chart = new frappe.ui.RealtimeChart("#chart", "test_event", 2, {
	// 				title: "Sales By Item",
	// 				data: r.message,
	// 				type: 'bar',
	// 				height: 250,
	// 				color: ['#7cd6fd']
	// 			})
	// 			window.chart.start_updating();
	// 		}
	// 	}
	// })



