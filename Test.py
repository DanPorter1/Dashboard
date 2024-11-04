# streamlit run test.py
import streamlit as st
import pandas as pd

st.title("Dashboard")

with st.sidebar:
    st.write("Testing")
    inc_selectbox = st.sidebar.selectbox(
        "Select Incident type",
        ("All", "Pharmacy Manager", "HSCN", "EPS", "Other")
    )
    status_radio = st.radio(
        "Choose ticket status",
        ("Open", "On Hold", "Closed", "Resolved")
    )

df = pd.read_csv("SampleData.csv")

df.loc[df['Incident Summary'] == inc_selectbox]
