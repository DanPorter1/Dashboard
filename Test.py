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
    if status_radio != "All":
        filtered_df = df[df['State'] == status_radio]
    else: 
        filtered_df = df
else:
    filtered_df = df[(df['Incident Summary'] == inc_selectbox) & (df['State'] == status_radio)]
    
    if status_radio != "All":
        filtered_df = filtered_df[filtered_df['State'] == status_radio]

st.write(filtered_df)

grouped_df = filtered_df.groupby('State').size().reset_index(name='count')
st.bar_chart(grouped_df, x='State', y='count')

grouped_open_date = filtered_df.groupby('Open Date')['Open Date'].nunique().reset_index(name='unique_count')
st.bar_chart(grouped_open_date, x='Open Date', y='unique_count')
