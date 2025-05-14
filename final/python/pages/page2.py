import streamlit as st


def page2():
    st.markdown("# Summary ❄️")
    st.write("Here's our first attempt at using data to create a table:")


summary_page = st.Page("page1.py",title='Summary page', icon=":material/home:")
dashboard = st.Page(page2, title='Dashboard', icon=":material/database:")
read_me = st.Page("page3.py", title='Read me', icon=":material/note:")

pg = st.navigation(
    {
        "Summary": [summary_page],
        "Data Table": [dashboard],
        "Contact us": [read_me],
    }
)

pg.run()