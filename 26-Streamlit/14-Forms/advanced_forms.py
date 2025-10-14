import streamlit as st


st.header("Declarative Forms")

form2 = st.form("form2")
form2.write("Job Selection")
position = form2.selectbox("Select a position", ["Data Analyst", "Data Scientist",
                                                 "Data Engineer", "Web Developer",
                                                 "Project Manager", "Architect"])
btn_submit = form2.form_submit_button("Send")
if btn_submit:
    st.info(f"You choose {position}")