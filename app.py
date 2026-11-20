# Library Setup
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# Import function from db_service.py
from services.db_service import get_rush_hours_data

# Initialize Dash Application
app = Dash(__name__)
server = app.server # Required for deployment

# Fetching a data via db_service
df = get_rush_hours_data()

# Create Plotly Visualization
"""
TODO: Create a chart that show volume of each channel in each hour
"""
fig = px.bar(
    df,
    x="hour_of_day",
    y="total_order",
    color="channel",
    barmode="group",
    title="Total Orders by Clock Hour and Sales Channel (21 Sep - 1 Nov 2026)",
    labels={
        "hour_of_day": "Clock Hour of Day",
        "total_order": "Total Orders (All Recorded Days)",
        "channel": "Sales Channel"
    }
)

# App Layout
app.layout = html.Div([
    html.H1("Bubble Tea Store Analytics"),
    html.P("21 Sep – 1 Nov 2026"),
    dcc.Graph(id="rush-hour-chart", figure=fig)
])

if __name__ == "__main__":
    app.run(debug = True)