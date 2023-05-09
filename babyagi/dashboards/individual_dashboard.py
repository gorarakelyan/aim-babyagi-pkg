row1, row2, row3 = ui.rows(3)

row2_col1, row2_col2 = row2.columns(2)
row3_col1, row3_col2 = row3.columns(2)

run_hash = row1.text_input('f1a3eff6664b4d0694305e0a')

if run_hash != '':
    row2_col1.run_logs(run_hash)
    row2_col2.run_messages(run_hash)

    metrics = Metric.filter(f'run.hash == "{run_hash}"')
    texts = Texts.filter(f'run.hash == "{run_hash}"')

    row3_col1.line_chart(metrics, x='steps', y='values', 
        color=["metric.name"], stroke_style=["metric.context"])

    text_viz = row3_col2.texts(texts, color=['record.step'])
    text_viz.group('row', ['texts.name'])
    text_viz.group('column', ['texts.context'])
