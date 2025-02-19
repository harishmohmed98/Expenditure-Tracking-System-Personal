import streamlit as st
from datetime import datetime
import requests
import pandas as pd
import plotly.express as px

API_URL = "http://localhost:8000"


def fetch_analytics(start_date, end_date, filter_by):
    payload = {
        "start_date": start_date.strftime("%Y-%m-%d"),
        "end_date": end_date.strftime("%Y-%m-%d"),
        "filter_by": filter_by
    }
    response = requests.post(f"{API_URL}/analytics/", json=payload)
    return response.json()


def analytics_graphical_tab():
    st.title("Graphical Expense Analysis")

    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2024, 8, 1))
    with col2:
        end_date = st.date_input("End Date", datetime(2024, 8, 5))

    filter_by = st.selectbox("Filter Data By", ["Category", "Month", "Custom Date Range"])
    chart_type = st.selectbox("Select Chart Type", [
        "Bar Chart", "Line Chart", "Scatter Plot", "Pie Chart", "Area Chart", "Column Chart", "Histogram"
    ])

    if st.button("Generate Analysis"):
        response = fetch_analytics(start_date, end_date, filter_by)

        if response:
            df = pd.DataFrame({
                "Category": list(response.keys()),
                "Total": [response[category]["total"] for category in response],
                "Percentage": [response[category]["percentage"] for category in response]
            })
            df_sorted = df.sort_values(by="Percentage", ascending=False)

            st.subheader(f"{chart_type} for {filter_by}")

            if chart_type == "Bar Chart":
                fig = px.bar(df_sorted, x="Category", y="Total", title="Bar Chart Analysis")
            elif chart_type == "Line Chart":
                fig = px.line(df_sorted, x="Category", y="Total", title="Line Chart Analysis")
            elif chart_type == "Scatter Plot":
                fig = px.scatter(df_sorted, x="Category", y="Total", title="Scatter Plot Analysis")
            elif chart_type == "Pie Chart":
                fig = px.pie(df_sorted, names="Category", values="Total", title="Pie Chart Analysis")
            elif chart_type == "Area Chart":
                fig = px.area(df_sorted, x="Category", y="Total", title="Area Chart Analysis")
            elif chart_type == "Column Chart":
                fig = px.bar(df_sorted, x="Category", y="Total", title="Column Chart Analysis")
            elif chart_type == "Histogram":
                fig = px.histogram(df_sorted, x="Category", y="Total", title="Histogram Analysis")

            st.plotly_chart(fig)
            df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)
            df_sorted["Percentage"] = df_sorted["Percentage"].map("{:.2f}".format)
            st.table(df_sorted)
        else:
            st.warning("No data available for the selected date range and filter.")
