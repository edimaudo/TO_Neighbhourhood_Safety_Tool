from utils import *

pg = st.navigation([
    st.Page("About.py"),
    st.Page("Overview.py"),
    st.Page("Neighborhood_Incident_Exploration.py"),
    st.Page("Neighborhood_Incident_Predictor.py"),
    st.Page("Neighborhood_Incident_Forecast.py"),
])
pg.run()