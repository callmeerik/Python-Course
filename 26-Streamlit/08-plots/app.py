import streamlit as st
import plotly.express as px
import pandas as pd

# config data page
st.set_page_config(
    page_title="Plots",
    page_icon= "📊"
)

def main():
    st.title("📊 Plots In Streamlit")

    # load dataframe
    df = pd.read_csv("./data/employee_survey.csv")
    st.dataframe(df, height=300)

    # pecentage representation of departments in the survey
    fig = px.pie(
        data_frame=df,
        values="PhysicalActivityHours",
        names="Dept",
        title="Physiscal Activity Hours per Department"
    )
    st.plotly_chart(fig)

    # bar plot
    x = st.selectbox("Choose a column", df.columns)
    y = st.selectbox("Choose a numeical column", df.columns)
    if x == y:
         st.write("⚠ Select different columnas")
    else:
        fig2 = px.bar(df, x=x, y=x, title=f"Avg {y} by {x}", 
                  color_discrete_sequence=["#05CA3D"] )
        st.plotly_chart(fig2)

if __name__ == "__main__":
    main()