import streamlit as st


st.header("Salary Calculator")

with st.form("form_calculator", clear_on_submit=True):
    # create columns layout
    col1, col2, col3 = st.columns(3)

    with col1:
        hourly_salary = st.number_input("Hourly Salary ($)", min_value=0.0 )
    with col2:
        weekly_worked_hours = st.number_input("Weekkly Hours Worked", min_value=0.0)
    with col3:
        st.write("")
        calculate = st.form_submit_button("Calculate Salary", type="primary")

    if calculate:
        # calcute salary
        daily = (weekly_worked_hours / 5) * hourly_salary
        weekly = daily * 5
        monthly = weekly * 4
        annual = weekly * 52

        st.subheader("💲 Salary Breakdown")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 📅**Daily Salary**")
            st.write(f"${daily}")
            st.markdown("#### 📅**Weekly Salary**")
            st.write(f"${weekly}")
        with col2:
            st.markdown("#### 📅**Monthly Salary**")
            st.write(f"${monthly}")
            st.markdown("#### 📅**Annual Salary**")
            st.write(f"${annual}")