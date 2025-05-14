####
# mysql
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine, URL, MetaData, Table
import mysql.connector
import toml

st.set_page_config(initial_sidebar_state="collapsed")

st.markdown("# Summary ❄️")

# Load Data
toml_data = toml.load("secret.toml")

USER = toml_data['mysql']['username']
PASSWORD = toml_data['mysql']['password']
HOST_NAME = toml_data['mysql']['host']
PORT = toml_data['mysql']['port']
DATABASE = toml_data['mysql']['database']

engine = create_engine(f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST_NAME}:{PORT}/{DATABASE}")
# same as engine = create_engine("mysql+mysqlconnector://root:admin@mysql:3306/dads5001db")


####
# mongodb
from pymongo import MongoClient
import duckdb

USER = toml_data['mongodb']['username']
PASSWORD = toml_data['mongodb']['password']
HOST_NAME = toml_data['mongodb']['host']
PORT = toml_data['mongodb']['port']
AUTHSOURCE = toml_data['mongodb']['authSource']
DATABASE = toml_data['mongodb']['database']

client = MongoClient(f"mongodb://{USER}:{PASSWORD}@{HOST_NAME}:{PORT}/?authSource={AUTHSOURCE}")
# same as client = MongoClient("mongodb://root:admin@mongodb:27017/?authSource=admin")


# main page func
def main_page():
    df1 = pd.read_sql(f'SELECT * FROM merge_table', con=engine)
    st.write(df1)

    db = client.dads5001db
    st.write(db.list_collection_names())

####
## page
summary_page = st.Page(main_page,title='Summary page', icon=":material/home:")
dashboard = st.Page("page2.py", title='Dashboard', icon=":material/database:")
read_me = st.Page("page3.py", title='Read me', icon=":material/note:")

## create menu tree
pg = st.navigation(
    {
        "Summary": [summary_page],
        "Data Table": [dashboard],
        "Contact us": [read_me],
    }
)
pg.run()