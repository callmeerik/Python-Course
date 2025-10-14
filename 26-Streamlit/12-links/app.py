"""
        Links
    This file contains the code for links in Streamlit
    using the st.link_page(), you can use this for navigate
    to anothe page in a multipage app, or to navigate to an external
    page. Also we'll see the st.link_button()

    Remember, if you want use st.page_link() to navigate to pages in a multipage app
    you need use the pages folder, and if you want you can hide the 
    sidebar with native options
"""

import streamlit as st



st.page_link("./pages/1_home.py", label="Home", icon="🏠")

# link to external page
st.page_link("https://onefootball.com/es/inicio", label="💻 One Football")

# button external link
st.link_button("Go To One Football", "https://onefootball.com/es/inicio")