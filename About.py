from utils import *

st.title(APP_NAME)
st.header(ABOUT_HEADER)

st.markdown(
    """
    Focusing on Community Safety, this project analyzes crime and socio-economic data to understand incident risk for Toronto, Ontario neighbourhoods.  
    It also enables the user to predict and forecast incident risk looking at a particlar neighourhood.  
    Based on the predictions and forecast it would leverage Gemini AI to generate safety tips. 
    It is built using [streamlit](https://streamlit.io/cloud), [Gemini AI](https://ai.google.dev/gemini-api/docs) and TIDB Serverless (https://www.pingcap.com/).  
    The data is from [Toronto Police](https://data.torontopolice.on.ca/datasets/TorontoPS::major-crime-indicators-open-data/about) and [City of Toronto](https://data.urbandatacentre.ca/organization/city-of-toronto-open-data?q=wellbeing&sort=score+desc%2C+metadata_modified+desc&page=1).
    """
)