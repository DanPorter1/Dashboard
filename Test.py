# streamlit run test.py
import streamlit as st
import pandas as pd

st.title("Dashboard")

with st.sidebar:
    st.write("Testing")
    add_selectbox = st.sidebar.selectbox(
        "Select Incident type",
        ("All", "Pharmacy Manager", "HSCN", "EPS", "Other")
    )
    add_radio = st.radio(
        "Choose ticket status",
        ("Open", "On Hold", "Closed", "Resolved")
    )

df = pd.read_csv("SampleData.csv")
st.dataframe(df)
if 'selectbox_changed' not in st.session_state:
    st.session_state.selectbox_changed = False

if add_selectbox != st.session_state.selected_incident_type:
    st.session_state.selected_incident_type = add_selectbox
    st.session_state.selectbox_changed = True

if st.session_state.selectbox_changed:
    filtered_df = df[df['Incident Summary'].str.contains(add_selectbox)]
    st.dataframe(filtered_df)
