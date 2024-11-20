import streamlit as st
import pandas as pd
import numpy as np
from Bio import SeqIO
import matplotlib.pyplot as plt
import plotly.express as px
import py3Dmol 
from io import StringIO
st.markdown("""
    <style>
        body {
            background-color: #2e2e2e;  /* Dark gray background */
            color: white;               /* White text color */
        }
        .block-container {
            border: 2px solid black;   /* Black borders around the content */
            padding: 20px;              /* Padding for content spacing */
        }
        .css-1v3fvcr {
            background-color: #333333 !important; /* Darker background for Streamlit elements */
        }
        .stButton>button {
            background-color: #4CAF50;  /* Example: Green button */
            color: white;               /* White text color for the button */
        }
    </style>
""", unsafe_allow_html=True)
st.title("Dark Gray Background with Black Borders")  # App title
st.write("This is a Streamlit app with a custom dark theme!")  # Main description text
st.button("Click Me")
