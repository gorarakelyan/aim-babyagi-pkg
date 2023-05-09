ui.text("Welcome to BabyAGI observation space <3")

BoardLink("babyagi.dashboards.individual_dashboard")
BoardLink("babyagi.dashboards.side_by_side_comparison")

ui.text("Pages:")
BoardLink("babyagi.pages.exec_detailed")

ui.text("All executions (this is an embedded util board):")

BoardEmbed("babyagi.utils.metrics")
