import streamlit as st



# navigation
pg = st.navigation([
    st.Page("home.py", title="Home", icon="🏠"),
    st.Page("./article_generator.py", title="Article Generator", icon="📗"),
    st.Page("./code_generator.py", title="Code Generator", icon="💻"),
    st.Page("./dataset_generator.py", title="Dataset Generator", icon="📊")
])

pg.run()