"""
        Using st.nagivation to create a menu
    this file app.py only contains the navigation
"""

import streamlit as st

#pages = st.navigation([""
#    st.Page("home.py", title="🏠 Home"),
#    st.Page("football.py", title="⚽ Football Data"),
#    st.Page("./basketball.py", title="🏀 Basketball Data"),
#    st.Page("./sales.py", title="💵 Sales"),
#    st.Page("./products.py", title="📋 Products")
#], position="top")

# group pages by a category
pages = {
    "Home": [st.Page("home.py", title="🏠 Home")],
    "Sports":[
        st.Page("football.py", title="⚽ Football Data"),
        st.Page("./basketball.py", title="🏀 Basketball Data")
    ],
    "Administrative":[
        st.Page("./sales.py", title="💵 Sales"),
        st.Page("./products.py", title="📋 Products")
    ]
}

pg = st.navigation(pages, position="top")

# run each page
pg.run() 