import streamlit as st
import plotly.express as px
import pandas as pd
from add_update import add_update_tab
from analytics_by_category import analytics_category_tab
from analytics_by_months import analytics_months_tab

# Customizing Theme
st.set_page_config(page_title="Expenditure Tracking System-Personal", layout="wide")

# App Title with Styling
st.markdown("<h1 style='text-align: center; color: #E63946;'>💰 Expenditure Tracking System-Personal</h1>", unsafe_allow_html=True)

# Create Tabs
tab1, tab2, tab3, tab4 = st.tabs(["Add/Update", "Analytics By Category", "Analytics By Months", "Graphical Analysis"])

# Add/Update Tab
with tab1:
    add_update_tab()

# Category Analysis Tab
with tab2:
    analytics_category_tab()

# Monthly Analysis Tab
with tab3:
    analytics_months_tab()

# Graphical Analysis Tab
with tab4:
    st.subheader("📊 Expense Trends & Insights")

    # Sample Data (Replace this with actual database query)
    data = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
        "Food": [200, 250, 300, 280, 260],
        "Transport": [150, 180, 200, 190, 170],
        "Office Supplies": [100, 120, 130, 140, 150],
        "Misc": [50, 60, 70, 65, 80]
    })

    # Stacked Area Chart for Expense Trend
    fig = px.area(data, x="Month", y=["Food", "Transport", "Office Supplies", "Misc"],
                  title="📈 Monthly Expense Trend",
                  labels={"value": "Amount ($)", "variable": "Category"},
                  color_discrete_sequence=px.colors.qualitative.Set1)

    st.plotly_chart(fig, use_container_width=True)

    # Pie Chart for Expense Breakdown (Sample Data)
    pie_data = pd.DataFrame({
        "Category": ["Food", "Transport", "Office Supplies", "Misc"],
        "Amount": [sum(data["Food"]), sum(data["Transport"]), sum(data["Office Supplies"]), sum(data["Misc"])]
    })

    fig2 = px.pie(pie_data, values="Amount", names="Category",
                  title="💡 Expense Breakdown by Category",
                  color_discrete_sequence=px.colors.sequential.RdBu)

    st.plotly_chart(fig2, use_container_width=True)

# Sidebar for Filters
st.sidebar.header("🔍 Filters")
selected_category = st.sidebar.selectbox("Select Category", ["All", "Food", "Transport", "Office Supplies", "Misc"])
date_range = st.sidebar.date_input("Select Date Range", [])

# Success or Warning Messages
st.sidebar.markdown("---")
st.sidebar.success("📌 Keep track of your expenses to optimize spending!")
st.sidebar.warning("⚠️ High expenses detected for some categories!")
