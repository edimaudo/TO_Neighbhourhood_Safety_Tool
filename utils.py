"""
Libraries
"""
import streamlit as st
import pandas as pd
import datetime
import os, os.path
import warnings
import random
import plotly.express as px
import plotly.graph_objects as go
import geopandas as gpd
import folium
import pickle
from pycaret.classification import *
import datetime
import time
import numpy as np
import statistics
import xgboost

"""
App Information
"""
APP_NAME = 'TO Neighbourhood Safety Tool'
ABOUT_HEADER = 'About'
OVERVIEW_HEADER = 'Safety & Socio-economic Overview'
NEIGHBORHOOD_HEADER = "Neighborhood Safety & Socio-economic Profile"
PREDICTON_HEADER = 'Neighborhood Safety Risk Prediction'
FORECAST_HEADER = 'Neighborhood Safety Risk Forecast'
APP_FILTERS = 'Filters'
NO_DATA_INFO = 'No data available to display based on the filters'

warnings.simplefilter(action='ignore', category=FutureWarning)
st.set_page_config(
    page_title=APP_NAME,
    layout="wide"
)


