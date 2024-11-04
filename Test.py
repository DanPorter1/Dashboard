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
        ("All", "Open", "On Hold", "Closed", "Resolved")
    )

df = pd.read_csv("SampleData.csv")

if inc_selectbox == "All":
    st.write(df)
else:
    filtered_df = df.loc[df['Incident Summary'] == inc_selectbox]
    st.write(filtered_df)
if status_radio == "All":
    st.write(df)
else: 
    filtered_df = df.loc[df['State'] == status_radio]
    st.write(filtered_df)
