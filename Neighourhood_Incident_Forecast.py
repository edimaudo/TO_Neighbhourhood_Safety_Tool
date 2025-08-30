from utils import *
from data import *

st.title(APP_NAME)
st.header(FORECAST_HEADER)

st.write("Use the filters to forecast future incidents and get insights into how to keep yourself safe")

with st.sidebar:
        neighourhood_options = st.selectbox('Neighbourhood',NEIGHBORHOOD)
        mci_options = st.selectbox('Crime Type',MCI_CATEGORY)
        forecast_range = st.slider("Forecast Range", 1, 36, 12)

# Setup data
neighorhood_df = df_filtered[(df_filtered['MCI_CATEGORY'] == (mci_options)) & (df_filtered['Neighborhood'] == neighourhood_options)]
model_data = neighorhood_df[['OCC_YEAR','OCC_MONTH','Neighborhood','MCI_CATEGORY']]

crime_monthly = model_data.groupby(
    ['OCC_YEAR','OCC_MONTH','Neighborhood','MCI_CATEGORY']
).size().reset_index(name="Total")

crime_monthly["DATE"] = pd.to_datetime(
    crime_monthly["OCC_YEAR"].astype(str) + "-" + crime_monthly["OCC_MONTH"].astype(str) + "-01"
)