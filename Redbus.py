# importing libraries
# import pandas as pd
# import mysql.connector
import streamlit as st
# from streamlit_option_menu import option_menu
# import plotly.express as px
# import time
import base64

# Function to convert image to base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Path to your image
background_image_path = r'/Users/saro/Desktop/redbus_selenium/imgs/pexels-gabriel-peter-219375-696644.png'

# Convert the image to base64
base64_image = get_base64_of_bin_file(background_image_path)

# CSS to inject
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/jpg;base64,{base64_image}");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
</style>
"""

# Inject CSS with markdown
st.markdown(page_bg_img, unsafe_allow_html=True)

st.header("Redbus Selenium Project")