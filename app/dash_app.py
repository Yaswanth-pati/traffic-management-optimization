from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Load your dataset
df = pd.read_csv('traffic-volume-survey.csv')

app = Dash(__name__, suppress_callback_exceptions=True)

def create_volume_histogram(data):
    fig = px.histogram(data, x='volume_24h', color='road_name',
                       title='Distribution of 24-Hour Traffic Volume',
                       labels={'volume_24h': '24-Hour Traffic Volume'},
                       barmode='group', template='plotly_white')
    fig.update_traces(opacity=0.75)
    fig.update_layout(
        title_font_size=22,
        title_font_family='Verdana',
        legend_title_text='Road',
        xaxis_title="24-Hour Volume",
        yaxis_title="Count",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(255,255,255,1)'
    )
    return fig



# Function to create a scatter plot of Volume vs. Speed
def create_volume_speed_scatter(data):
    fig = px.scatter(data, x='volume_24h', y='range', color='road_name',
                     title='Traffic Volume vs. Speed',
                     labels={'volume_24h': '24-Hour Volume', 'range': 'Speed (km/h)'},
                     template='plotly_white')
    fig.update_traces(marker=dict(size=10, opacity=0.8, line=dict(width=2, color='DarkSlateGrey')))
    fig.update_layout(
        title_font_size=22,
        legend_title_text='Road',
        xaxis_title="24-Hour Volume",
        yaxis_title="Speed (km/h)"
    )
    return fig

# Function to create a scatter plot of Volume vs. Speed
def create_volume_speed_year_scatter(data):
    fig = px.scatter(data, x='volume_24h', y='installed_year', color='road_name',
                     title='Traffic Volume vs. Speed',
                     labels={'volume_24h': '24-Hour Volume', 'range': 'Speed (km/h)'},
                     template='plotly_white')
    fig.update_traces(marker=dict(size=10, opacity=0.8, line=dict(width=2, color='DarkSlateGrey')))
    fig.update_layout(
        title_font_size=22,
        legend_title_text='Road',
        xaxis_title="24-Hour Volume",
        yaxis_title="Speed (km/h)"
    )
    return fig


# Function to create a bar chart of Peak Traffic Times
def create_peak_times_bar(data):
    fig = px.bar(data, x='road_name', y='peakvol', color='road_name',
                 title='Peak Traffic Volumes by Road',
                 labels={'peakvol': 'Peak Volume', 'road_name': 'Road Name'},
                 template='plotly_white')
    fig.update_layout(
        title_font_size=22,
        legend_title_text='Road',
        xaxis_title="Road Name",
        yaxis_title="Peak Volume",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(255,255,255,1)'
    )
    fig.update_traces(marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
    return fig


app.layout = html.Div([
    html.H1("Traffic Data Visualization", style={'textAlign': 'center', 'color': '#007BFF'}),
    html.Div([  # This div will contain the dropdowns and use flexbox to align them side by side
        dcc.Dropdown(
            id='road-dropdown',
            options=[{'label': road, 'value': road} for road in df['road_name'].unique()],
            value=[],
            multi=True,
            clearable=False,
            placeholder="Select a road",
            style={'padding': '3px', 'minWidth': '300px'}
        ),
        dcc.Dropdown(
            id='year-dropdown',
            options=[{'label': year, 'value': year} for year in sorted(df['installed_year'].unique())],
            value=[],
            multi=True,
            clearable=True,
            placeholder="Select installation year",
            style={'padding': '3px','minWidth': '300px'}
        ),
    ], style={'display': 'flex', 'justifyContent': 'space-between'}),  # Flex container styles
    dcc.Graph(id='traffic-volume-graph'),
    dcc.Graph(id='volume-speed-scatter-graph'),
    dcc.Graph(id='peak-times-bar-graph'),
], style={'padding': '20px', 'backgroundColor': '#FAFAFA'})


# Callback to update the traffic volume graph
@app.callback(
    Output('traffic-volume-graph', 'figure'),
    Input('road-dropdown', 'value')
)
def update_traffic_graph(selected_roads):
    try:
        if not selected_roads:
            return {}
        filtered_df = df[df['road_name'].isin(selected_roads)]
        return create_volume_histogram(filtered_df)
    except Exception as e:
        print("Error updating traffic graph:", e)
        return {}

# Callback to update the volume-speed scatter graph
@app.callback(
    Output('volume-speed-scatter-graph', 'figure'),
    Input('road-dropdown', 'value')
)
def update_volume_speed_scatter(selected_roads):
    try:
        if not selected_roads:
            return {}
        filtered_df = df[df['road_name'].isin(selected_roads)]
        return create_volume_speed_scatter(filtered_df)
    except Exception as e:
        print("Error updating volume-speed scatter:", e)
        return {}

# Callback to update the peak times bar graph
@app.callback(
    Output('peak-times-bar-graph', 'figure'),
    Input('road-dropdown', 'value')
)
def update_peak_times_bar(selected_roads):
    try:
        if not selected_roads:
            return {}
        filtered_df = df[df['road_name'].isin(selected_roads)]
        return create_peak_times_bar(filtered_df)
    except Exception as e:
        print("Error updating peak times bar graph:", e)
        return {}
    

# app.layout = html.Div([
#     html.H1("Traffic Data Visualization"),
#     dcc.Dropdown(
#         id='year-dropdown',
#         options=[{'label': year, 'value': year} for year in df['installed_year'].unique()],
#         value=None,
#         multi=True,
#         placeholder="Select Year",
#     ),
#     dcc.Graph(id='year-graph'),
#     dcc.Graph(id='volume-speed-year-scatter-graph'),
#     dcc.Graph(id='peak-times-bar-graph')
# ])

# @app.callback(
#     Output('year-graph', 'figure'),
#     Input('year-dropdown', 'value')
# )
# def update_graph(selected_years):
#     if not selected_years:
#         return {}
#     filtered_df = df[df['installed_year'].isin(selected_years)]
#     return create_volume_histogram(filtered_df)

# Callback to update the volume-speed scatter graph
# @app.callback(
#     Output('volume-speed-year-scatter-graph', 'figure'),
#     Input('road-dropdown', 'value')
# )
# def update_volume_speed_year_scatter(selected_years):
#     try:
#         if not selected_years:
#             return {}
#         filtered_df = df[df['installed_year'].isin(selected_years)]
#         return create_volume_speed_year_scatter(filtered_df)
#     except Exception as e:
#         print("Error updating volume-speed scatter:", e)
#         return {}




if __name__ == '__main__':
    app.run_server(debug=False)
