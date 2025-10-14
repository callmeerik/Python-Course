import streamlit as st

st.header("Basic Form ")

st.subheader("Register")

# create form
with st.form("register"):
    name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Register", type="primary")
    if submit:
        st.success("User registered in our database")