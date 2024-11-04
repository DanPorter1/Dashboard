# streamlit run d:/Py/Work/ai/dashboard/dashboad.py
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np


st.title("INC - Dashboard")

filtered_df = pd.read_csv("anondata.csv")

filtered_df['Open Date'] = pd.to_datetime(filtered_df['Open Date'])

months = filtered_df['Open Date'].dt.strftime('%Y-%m').unique()

st.sidebar.title("Filters")
inc_type = st.sidebar.selectbox("Incident Type", ["All", "EPS", "Hardware", "HSCN"])
num_months = st.sidebar.slider("Number of months to show", 1, len(months), 3)
start_month = st.sidebar.selectbox("Starting month", months)
months_list = months.tolist()
filtered_months = months_list[months_list.index(start_month):months_list.index(start_month) + num_months]

max_value = 0
for i in range(0, len(filtered_months), 3):
    cols = st.columns(4)
    for j, month in enumerate(filtered_months[i:i+3]):
        month_df = filtered_df[filtered_df['Open Date'].dt.strftime('%Y-%m') == month]
        incident_summary_counts = month_df['Incident Summary'].value_counts()
        sorted_counts = dict(sorted(incident_summary_counts.items(), key=lambda x: x[1], reverse=True))

        top_5 = dict(list(sorted_counts.items())[:5])
        other = sum(list(sorted_counts.values())[5:])

        current_max = max([top_5[v] for v in top_5] + [other])
        if current_max > max_value:
            max_value = current_max

        fig = px.bar(x=[f"{v} - {k}" for k, v in top_5.items()] + ["Other"],
                     y=[top_5[v] for v in top_5] + [other],
                     title=f"Period {month}",
                     text=[top_5[v] for v in top_5] + [other])
        fig.update_layout(title=f"Period {month}")
        fig.update_layout(yaxis=dict(range=[0, max_value * 1.1]))
        cols[j].plotly_chart(fig, use_container_width=True)

  # Calculate the percentage for each top 5 incident summary
        total_count = sum(top_5.values())
        percentages = {k: (v / total_count) * 100 for k, v in top_5.items()}

        # Display the percentages
        for summary, percentage in percentages.items():
            cols[j].write(f"{summary}: {percentage:.2f}%")

        # Display the percentage change
        if month == start_month:
            percentage_change = 0
        else:
            start_month_value = filtered_df[filtered_df['Open Date'].dt.strftime('%Y-%m') == start_month]['Incident Summary'].value_counts().sum()
            current_month_value = month_df['Incident Summary'].value_counts().sum()
            percentage_change = ((current_month_value - start_month_value) / start_month_value) * 100

        cols[j].write(f"Percentage change from {start_month}: {percentage_change:.2f}%")
       #  202 129 140 

start_month_df = filtered_df[filtered_df['Open Date'].dt.strftime('%Y-%m') == start_month]
end_month_df = filtered_df[filtered_df['Open Date'].dt.strftime('%Y-%m') == filtered_months[-1]]
start_month_count = start_month_df['Incident Summary'].value_counts().sum()
end_month_count = end_month_df['Incident Summary'].value_counts().sum()
total_percentage_change = ((end_month_count - start_month_count) / start_month_count) * 100
st.sidebar.write(f"**Total Percentage Change from {start_month} to {filtered_months[-1]}: {total_percentage_change:.2f}%**")
st.sidebar.write(f"**Total Incidents in {start_month}: {start_month_count}**")
st.sidebar.write(f"**Total Incidents in {filtered_months[-1]}: {end_month_count}**")