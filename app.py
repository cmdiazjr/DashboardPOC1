import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go

from modules.latency import check_latency
from modules.system_metrics import get_system_metrics
from modules.security_feed import get_event_feed
from modules.device_health import get_device_health

app = dash.Dash(__name__)
app.title = "Dashboard POC 1"

# Layout
app.layout = html.Div(style={"font-family": "Arial", "margin": "20px"}, children=[
    html.H1("Real-Time IT Operations Dashboard", style={"text-align": "center"}),

    # Auto refresh every 5 seconds
    dcc.Interval(id="interval-component", interval=5*1000, n_intervals=0),

    html.Div([
        # Latency chart
        html.Div([
            html.H3("Network Latency (ms)"),
            dcc.Graph(id="latency-graph")
        ], style={"width": "48%", "display": "inline-block", "vertical-align": "top"}),

        # System Metrics
        html.Div([
            html.H3("System Metrics"),
            html.Div(id="system-metrics")
        ], style={"width": "48%", "display": "inline-block", "vertical-align": "top", "padding-left": "20px"})
    ]),

    html.Hr(),

    html.Div([
        # Security Feed
        html.Div([
            html.H3("Security Events (Latest 5)"),
            html.Div(id="security-feed")
        ], style={"width": "48%", "display": "inline-block", "vertical-align": "top"}),

        # Device Health Panel
        html.Div([
            html.H3("Device Health Status"),
            html.Div(id="device-health")
        ], style={"width": "48%", "display": "inline-block", "vertical-align": "top", "padding-left": "20px"})
    ])
])

# CALLBACKS ----------------------------------------------------------------

@app.callback(
    Output("latency-graph", "figure"),
    Input("interval-component", "n_intervals")
)
def update_latency_graph(n):
    data = check_latency()

    return {
        "data": [
            go.Bar(
                x=list(data.keys()),
                y=[v["latency"] if v["latency"] is not None else 0 for v in data.values()],
                marker=dict(
                    color=[
                        "#2ECC71" if v["status"] == "UP" else
                        "#F1C40F" if v["status"] == "DEGRADED" else
                        "#E74C3C"
                        for v in data.values()
                    ]
                )
            )
        ],
        "layout": go.Layout(
            yaxis={"title": "Latency (ms)"},
            margin={"l": 40, "r": 20, "t": 20, "b": 40},
            height=300
        )
    }


@app.callback(
    Output("system-metrics", "children"),
    Input("interval-component", "n_intervals")
)
def update_system_metrics(n):
    m = get_system_metrics()

    return html.Div([
        html.P(f"CPU Usage: {m['cpu_percent']}%"),
        html.P(f"Memory: {m['memory_used']} GB / {m['memory_total']} GB"),
        html.P(f"Disk: {m['disk_used']} GB / {m['disk_total']} GB")
    ])


@app.callback(
    Output("security-feed", "children"),
    Input("interval-component", "n_intervals")
)
def update_security(n):
    events = get_event_feed()

    return html.Ul([
        html.Li(f"{event['timestamp']} | {event['event_type']} | {event['source_ip']}")
        for event in events
    ])


@app.callback(
    Output("device-health", "children"),
    Input("interval-component", "n_intervals")
)
def update_health(n):
    health = get_device_health()

    def color(status):
        return {
            "UP": "#2ECC71",
            "DEGRADED": "#F1C40F",
            "DOWN": "#E74C3C"
        }.get(status, "white")

    return html.Ul([
        html.Li(f"{device}: {status}", style={"color": color(status), "font-weight": "bold"})
        for device, status in health.items()
    ])


# RUN APP -------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8050)

