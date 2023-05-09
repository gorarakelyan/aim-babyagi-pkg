row1, row2, row2 = ui.rows(3)

row2_col1, row2_col2 = row2.columns(2)

run1 = "0a958b87be9e47cbbaba3386"
run2 = "83ae83b6df48480a8d004786"

html_p = row1.text(f'Comparing runs: {run1}, {run2}')

row2_col1.run_messages(run1)
row2_col2.run_messages(run2)

metrics = Metric.filter(f'run.hash in ["{run1}", "{run2}"]')
line_chart = row3.line_chart(metrics, x='steps', y='values',
                color=["metric.name"],
                stroke_style=["metric.context"])
line_chart.group('row', ['metric.name'])
line_chart.group('column', ['run.hash'])
