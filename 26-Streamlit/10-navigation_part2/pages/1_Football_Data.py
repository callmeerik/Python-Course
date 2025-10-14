import streamlit as st
import pandas as pd
import plotly.express as px

def get_data():
    st.title("View Football Dataframe ")
    
    # read dataframe
    df = pd.read_csv("../data/results.csv")

    # show dataframe
    st.dataframe(df, height=250)

    st.header("Team Stadistics")

    # analysis
    team = st.selectbox("Select a team", df["home_team"].unique())
    home_games = df[df["home_team"] == team]["date"].count()
    away_games = df[df["away_team"] == team]["date"].count()
    st.write(f"Number of home games: {home_games}")
    st.write(f"Number of away games: {away_games}")

get_data()