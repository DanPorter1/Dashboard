 # streamlit run test.py
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

st.title("Dashboard")
#==============================================================#
def barchart():
    df['Unique Date'] = df['Open Date'].str[:11]
    # Group by 'Unique Date' and 'State' to get total incidents for each state on each unique date
    grouped_df = filtered_df.groupby(['Unique Date', 'State']).size().unstack(fill_value=0).reset_index()
    
    # Melt the dataframe to have states as a single column
    melted_df = pd.melt(grouped_df, id_vars=['Unique Date'], var_name='State', value_name='Total Incidents')
    
    # Plot grouped bar chart with adjusted bargap to make bars touch
    fig = px.bar(melted_df, x='Unique Date', y='Total Incidents', color='State', barmode='group', labels={'value': 'Total Incidents', 'Unique Date': 'Date'}).update_traces(marker=dict(line=dict(width=0)))
    
    return st.plotly_chart(fig)
#==============================================================#

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
chart = False
if inc_selectbox == "All":
    if status_radio != "All":
        chart = True
        filtered_df = df[df['State'] == status_radio]
    else: 
        filtered_df = df
        if chart == False:
            st.write(filtered_df)
            barchart()
else:
    chart = True
    filtered_df = df[(df['Incident Summary'] == inc_selectbox) & (df['State'] == status_radio)]
    
    if status_radio != "All":
        chart = True
        filtered_df = filtered_df[filtered_df['State'] == status_radio]
st.write(filtered_df)
