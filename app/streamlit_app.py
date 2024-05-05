import streamlit as st
import pandas as pd
import joblib


# Background
def add_bg_from_local():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(""); 
            background-size: cover;
            background-position: center center;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


add_bg_from_local()

# App Header
st.title(" Traffic Prediction App")
st.write("Enter the parameters and predict the traffic level")

# Loading the  Trained Model
lr_model = joblib.load("optimized_model.pkl")
logistic_model = joblib.load("log_model.pkl")
decision_model = joblib.load("dec_model.pkl")


# Function to enter the input and predict
def user_input():
    col1, col2, col3 = st.columns(3)
    with col1:
        pc85th_kmh = st.number_input("85th Percentile Speed", min_value=0)
        volume_12h = st.number_input("12 Hour Volume", min_value=0)
    with col2:
        volume_24h = st.number_input("24 Hour Volume", min_value=0)
        comm_vhcl = st.number_input("Commercial Vehicle Volume", min_value=0.0)
    with col3:
        peakvol = st.number_input("Peak Volume", min_value=0.0)

    return pd.DataFrame(
        {
            "pc85th_kmh": [pc85th_kmh],
            "volume_12h": [volume_12h],
            "volume_24h": [volume_24h],
            "comm_vhcl": [comm_vhcl],
            "peakvol": [peakvol],
        }
    )


def categorize_traffic_level_updated(speed_range):
    if speed_range == "Between 30km/h and 40km/h" or speed_range == "Less than 30km/h":
        return "low"
    elif speed_range == "Between 40km/h and 50km/h":
        return "moderate"
    elif speed_range == "Between 50km/h and 60km/h":
        return "high"
    elif speed_range == "More than 60km/h":
        return "extremely high"
    else:
        return "undefined"


# User Input
input_df = user_input()

# Button to Display Result
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Random Forest"):
        prediction = lr_model.predict(input_df)
        predicted_traffic_level = categorize_traffic_level_updated(prediction[0])
        st.write(f"Predicted Traffic Range: {prediction[0]}")
        st.write(f"Predicted Traffic Level: {predicted_traffic_level}")

with col2:
    if st.button("Logistic Model"):
        prediction = logistic_model.predict(input_df)
        predicted_traffic_level = categorize_traffic_level_updated(prediction[0])
        st.write(f"Predicted Traffic Range: {prediction[0]}")
        st.write(f"Predicted Traffic Level: {predicted_traffic_level}")

with col3:
    if st.button("Decision Tree"):
        prediction = decision_model.predict(input_df)
        predicted_traffic_level = categorize_traffic_level_updated(prediction[0])
        st.write(f"Predicted Traffic Range: {prediction[0]}")
        st.write(f"Predicted Traffic Level: {predicted_traffic_level}")
