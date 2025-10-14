import streamlit as st

pg = st.navigation([
    st.Page("home.py", title="Home"),
    st.Page("basic_form.py", title="Basic Form"),
    st.Page("advanced_forms.py", title="Advaced Forms"),
    st.Page("calculator.py", title="Salary Calculator")
])


if __name__ == '__main__':
    pg.run()