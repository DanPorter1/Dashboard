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


st.write(filtered_df)
filtered_df = df[df['Incident Summary'] == inc_selectbox] if inc_selectbox != "All" else df
filtered_df = filtered_df[filtered_df['State'] == status_radio] if status_radio != "All" else filtered_df
st.write(filtered_df)
