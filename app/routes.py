from flask import render_template, request, jsonify
from app import app
import folium
import pandas as pd
import json

#traffic_volume_survey.json
road_data = pd.read_json('traffic_volume_survey.json')

@app.route('/')
def index():
    return render_template('home.html')

# @app.route('/route')
# def show_route():
#     start_lat = request.args.get('start_lat')
#     start_lon = request.args.get('start_lon')
#     end_lat = request.args.get('end_lat')
#     end_lon = request.args.get('end_lon')
#     # Logic to calculate route and display map
#     return render_template('maps.html', start_lat=start_lat, start_lon=start_lon, end_lat=end_lat, end_lon=end_lon)

@app.route('/predict',methods=['POST'])
def predict():
    try:
        # Extract road names from the form
        start_road_name = request.form['start']
        end_road_name = request.form['end']

        # Find the corresponding latitude and longitude for the road names
        start = road_data[road_data['road_name'] == start_road_name].iloc[0]
        end = road_data[road_data['road_name'] == end_road_name].iloc[0]

        # Create a folium map centered at the midpoint of the start and end points
        map_center = [(start['latitude'] + end['latitude']) / 2, (start['longitude'] + end['longitude']) / 2]
        folium_map = folium.Map(location=map_center)

        # Adding markers for the start and end points
        folium.Marker(
            [start['latitude'], start['longitude']],
            popup=f"Start: {start_road_name}",
            icon=folium.Icon(color='green', icon='play')
        ).add_to(folium_map)

        folium.Marker(
            [end['latitude'], end['longitude']],
            popup=f"End: {end_road_name}",
            icon=folium.Icon(color='red', icon='stop')
        ).add_to(folium_map)

        # Save map to html file within 'templates' directory
        map_file = 'map.html'
        folium_map.save(f'app/static/{map_file}')

        # Render the map in an iframe within the 'maps.html' template
        return render_template('maps.html', map_file=map_file)
        # return jsonify({'map_url': map_url})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/visuals',methods=['GET'])
def visuals():
    # Logic
    return render_template('visuals.html')

@app.route('/maps')
def maps():
    return render_template('maps.html')
