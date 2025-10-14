import streamlit as st
import pandas as pd

from st_aggrid import AgGrid, GridOptionsBuilder, StAggridTheme


# read dataframe with pandas
df = pd.read_csv("./data/results.csv")

custom_theme = (  
    StAggridTheme(base="quartz")
    .withParams(
        fontSize = 16,
        rowBorder = False,
        backgroundColor = "#8DA1EE",
        color = "#FFFF"
    )
)

def main():
    st.title("DataFrame with Streamlit")

    # using streamlit dataframe method
    st.subheader("Using st.dataframe() method")
    st.dataframe(df)

    # using pagination
    st.subheader("Using pagination")
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_pagination(paginationAutoPageSize=False, paginationPageSize=15)
    grid_options = gb.build()
    AgGrid(df, gridOptions= grid_options, theme=custom_theme)    
if __name__ == "__main__":
    main()