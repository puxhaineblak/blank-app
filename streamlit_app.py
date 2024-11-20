import streamlit as st
import pandas as pd
import numpy as np
from Bio import SeqIO
import matplotlib.pyplot as plt
import plotly.express as px
import py3Dmol 
from io import StringIO
git clone https://github.com/your-username/streamlit-dark-theme-app.git
cd streamlit-dark-theme-app
touch app.py
st.markdown("""
    <style>
        body {
            background-color: #2e2e2e;  /* Dark gray background */
            color: white;               /* White text color */
        }
        .block-container {
            border: 2px solid black;   /* Black borders */
            padding: 20px;              /* Add some padding for better spacing */
        }
        .css-1v3fvcr {
            background-color: #333333 !important; /* Darker background for elements */
        }
        .stButton>button {
            background-color: #4CAF50;  /* Example: Green button */
            color: white;
        }
    </style>
""", unsafe_allow_html=True)
st.title("Dark Gray Background with Black Borders")  # Title of the app
st.write("This is a Streamlit app with a custom dark theme!")
venv\Scripts\activate
pip freeze > requirements.txt
git add app.py requirements.txt
git commit -m "Added Streamlit app with dark theme and custom styling"
git push origin main
streamlit run app.py
