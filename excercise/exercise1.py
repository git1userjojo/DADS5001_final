import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import datetime as dt
import plotly.express as px

st.header("Exercise 1")

# select data
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
select_ls = [10, 100, 1000, 10000]
select_base = ['B02512', 'B02598', 'B02617', 'B02682', 'B02764']

@st.cache_data
def load_data(nrows, date, base):
    data = pd.read_csv(DATA_URL)#, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    data = data[(data['base'] == base) & (data[DATE_COLUMN].dt.date == date)]
    data = data[:nrows]
    data.reset_index(drop=True, inplace=True)
    return data

date = st.date_input("Select date", dt.date(2014, 9, 1))
num = st.selectbox("select number of rows", select_ls)
base = st.selectbox("select base", select_base)
data = load_data(num, date, base)

# show table
st.subheader('Raw data')
st.write(data)

# show map
st.subheader('3D Map data')
st.pydeck_chart(
    pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=data['lat'].loc[0],
            longitude=data['lon'].loc[0],
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=data,
                get_position="[lon, lat]",
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
            pdk.Layer(
                "ScatterplotLayer",
                data=data,
                get_position="[lon, lat]",
                get_color="[200, 30, 0, 160]",
                get_radius=200,
            ),
        ],
    )
)

# show histrogram graph
st.subheader('Histogram plot')
fig = px.histogram(data, x=DATE_COLUMN)
st.plotly_chart(fig)

# show count session
st.subheader('Session count')

if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Refresh!"):
    st.session_state.counter += 1
if st.button("Reset counter"):
    st.session_state.counter = 0

st.text(f"This page has run {st.session_state.counter} times.")
