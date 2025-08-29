from utils import *

pg = st.navigation([
    st.Page("About.py"),
    st.Page("Overview.py"),
    st.Page("Neighborhood_Safety_Risk_Exploration.py"),
    st.Page("Neighborhood_Safety_Risk_Predictor.py"),
])
pg.run()