import os
# from matplotlib.pyplot import plt
import sys

import pandas as pd
import plotly.express as px
import streamlit as st
import streamlit.components.v1 as components

def overview_app():
    st.title("View all cleaned data")
    st.write(
        "Customer Data's Overview")
    number = st.number_input("Enter the number of rows and press enter: ", min_value=None, max_value=None, value=0,
                             step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)

    df = pd.read_csv('../data/cleaned_data.csv', nrows=number)
    st.write(df)

    st.header("Top 10 handsets used by customers")
    top_df = pd.read_csv('../data/top_10_handset.csv')

    fig = px.bar(top_df, x='Handset_type', y='count', height=500)
    st.plotly_chart(fig)

    st.header("Top 3 applications used by customers")
    top_df = pd.read_csv('../data/user_eng.csv')

    fig = px.bar(top_df, x='cluster', y='total_data', height=500)
    st.plotly_chart(fig)
overview_app()