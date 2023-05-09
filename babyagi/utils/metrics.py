metrics = Metric.filter('True')
chart = ui.line_chart(metrics, x='steps', y='values', 
	stroke_style=["metric.context"],
	color=['metric.name'],
	)
chart.group('column', ['run.hash'])