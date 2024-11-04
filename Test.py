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


grouped_df = filtered_df.groupby(['Open Date Short', 'State']).size().reset_index(name='Count')

# Create chart with red color
chart = alt.Chart(grouped_df).mark_bar(color='red').encode(
    x='Open Date Short',
    y='Count',
    color='State',
    tooltip=['State', 'Open Date Short', 'Count']
).interactive()

st.altair_chart(chart, use_container_width=True)
