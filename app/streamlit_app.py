import streamlit as st
import pandas as pd
import plotly.express as px

# Load your data
data = pd.read_csv('traffic-volume-survey.csv')

# Display DataFrame columns for debugging
st.write("DataFrame columns:", data.columns)

#select the road names
#selected_roads = st.multiselect('Select road names:', data['road_name'].unique())






