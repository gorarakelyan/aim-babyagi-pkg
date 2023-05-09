row1, row2 = ui.rows(2)

row1.text("Select the run:")
run_hash = row1.text_input('f1a3eff6664b4d0694305e0a')

metrics, texts = row2.tabs(['Metrics', 'Texts'])

with metrics:
    metrics_data = Metric.filter(f'run.hash == "{run_hash}"')
    metrics.line_chart(metrics_data, x='steps', y='values', 
        color=["metric.name"], stroke_style=["metric.context"])
with texts:
    texts_data = Texts.filter(f'run.hash == "{run_hash}"')
    texts_list = texts.texts(texts_data, color=['record.step'])
    texts_list.group('row', ['texts.name'])
    texts_list.group('column', ['texts.context'])
