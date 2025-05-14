import streamlit as st


def page3():
    st.markdown("# Dashboard ❄️")
    st.write("Here's our first attempt at using data to create a table:")


summary_page = st.Page("page1.py",title='Summary page', icon=":material/home:")
dashboard = st.Page("page2.py", title='Dashboard', icon=":material/database:")
read_me = st.Page(page3, title='Read me', icon=":material/note:")

pg = st.navigation(
    {
        "Summary": [summary_page],
        "Data Table": [dashboard],
        "Contact us": [read_me],
    }
)

pg.run()