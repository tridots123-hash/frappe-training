frappe.pages['mypage-'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'None',
		single_column: true
	});
}

frappe.pages['mypage-'].on_page_load = function(wrapper) {
    let $wrapper = $(wrapper);
    $wrapper.html(`<div id="chart" style="padding: 20px;"></div>`);

    let data = {
        labels: [],
        datasets: [
            {
                name: "Fever",
                values: []
            },
            {
                name: "Cold",
                values: []
            }
        ]
    };

    let chart = new frappe.Chart("#chart", {
        title: "Disease Count Realtime",
        data: data,
        type: 'line',
        height: 300,
        colors: ['#ff6f69', '#247ba0']
    });

    frappe.realtime.on('disease_realtime_event', function(data_point) {
        const label = data_point.label;
        const values = data_point.points;

        chart.data.labels.push(label);
        chart.data.datasets[0].values.push(values[0]);  // Fever
        chart.data.datasets[1].values.push(values[1]);  // Cold

        // Keep only latest 10 entries
        if (chart.data.labels.length > 10) {
            chart.data.labels.shift();
            chart.data.datasets.forEach(ds => ds.values.shift());
        }

        chart.update();
    });
};   

