# streamlit run test.py
import streamlit as st
import pandas as pd
import altair as alt

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


grouped_df = filtered_df.groupby('State').size().reset_index(name='Count')
filtered_df['Open Date Short'] = filtered_df['Open Date'].str[:11]
grouped_open_date = filtered_df.groupby('Open Date Short')['Open Date'].nunique().reset_index(name='Count')
grouped_total = filtered_df.groupby(['State', 'Open Date Short']).size().reset_index(name='Count')

chart1 = alt.Chart(grouped_df).mark_bar().encode(
    x='State',
    y='Count'
)

chart2 = alt.Chart(grouped_open_date).mark_bar().encode(
    x='Open Date Short',
    y='Count'
)

chart3 = alt.Chart(grouped_total).mark_bar().encode(
  x='Open Date Short',
  y='Count',
  color='State',
  column='State'
)

st.altair_chart(chart3, use_container_width=True)
