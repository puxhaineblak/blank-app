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
st.title("Dark Gray Background with Black Borders")
st.write("This is a Streamlit app with a custom dark theme!")
