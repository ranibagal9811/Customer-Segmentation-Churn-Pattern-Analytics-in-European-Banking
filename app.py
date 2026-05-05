import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# -------------------------
# Load Data
# -------------------------
@st.cache_data
def load_data():
    return pd.read_csv("European_Bank.csv")

df = load_data()

# -------------------------
# Feature Engineering
# -------------------------
df['AgeGroup'] = pd.cut(df['Age'],
                       bins=[0,30,45,60,100],
                       labels=['<30','30-45','46-60','60+'])

df['TenureGroup'] = pd.cut(df['Tenure'],
                          bins=[-1,3,7,10],
                          labels=['New','Mid-term','Long-term'])

df['BalanceSegment'] = pd.cut(df['Balance'],
                             bins=[-1,0,100000,250000],
                             labels=['Zero','Low','High'])

# -------------------------
# Sidebar Navigation
# -------------------------
st.sidebar.title("Navigation")

page = st.sidebar.radio("Go to", [
    "Dashboard",
    "Segmentation Insights",
    "Comparative Analysis",
    "High-Value Customers",
    "Visualizations",
    "Result Summary",
    "Business Recommendations"
])

# -------------------------
# Filters (Global)
# -------------------------
geo = st.sidebar.multiselect("Geography", df['Geography'].unique(), df['Geography'].unique())
age = st.sidebar.multiselect("Age Group", df['AgeGroup'].unique(), df['AgeGroup'].unique())

filtered_df = df[
    (df['Geography'].isin(geo)) &
    (df['AgeGroup'].isin(age))
]

# =========================
# PAGE 1: Dashboard
# =========================
if page == "Dashboard":
    st.title("Customer Churn Dashboard")

    churn_rate = filtered_df['Exited'].mean()
    total = len(filtered_df)
    churned = filtered_df['Exited'].sum()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Customers", total)
    col2.metric("Churned Customers", churned)
    col3.metric("Churn Rate", f"{churn_rate:.2%}")

    st.subheader("Churn by Geography")
    geo_churn = filtered_df.groupby('Geography')['Exited'].mean().reset_index()
    fig, ax = plt.subplots()
    sns.barplot(data=geo_churn, x='Geography', y='Exited', ax=ax)
    st.pyplot(fig)

# =========================
# PAGE 2: Segmentation Insights
# =========================
elif page == "Segmentation Insights":
    st.title("Segmentation Insights")

    st.subheader("Age Group Churn")
    fig, ax = plt.subplots()
    sns.barplot(x='AgeGroup', y='Exited', data=filtered_df, ax=ax)
    st.pyplot(fig)

    st.info("Churn increases significantly in the 46–60 age group.")

    st.subheader("Balance Segment Churn")
    fig2, ax2 = plt.subplots()
    sns.barplot(x='BalanceSegment', y='Exited', data=filtered_df, ax=ax2)
    st.pyplot(fig2)

# =========================
# PAGE 3: Comparative Analysis
# =========================
elif page == "Comparative Analysis":
    st.title("Comparative Demographic Analysis")

    st.subheader("Gender vs Churn")
    fig, ax = plt.subplots()
    sns.barplot(x='Gender', y='Exited', data=filtered_df, ax=ax)
    st.pyplot(fig)

    st.subheader("Geography vs Age Heatmap")
    pivot = pd.pivot_table(filtered_df,
                           values='Exited',
                           index='Geography',
                           columns='AgeGroup')

    fig2, ax2 = plt.subplots()
    sns.heatmap(pivot, annot=True, ax=ax2)
    st.pyplot(fig2)

    st.warning("Germany + Age 46–60 shows highest churn risk.")

# =========================
# PAGE 4: High-Value Customers
# =========================
elif page == "High-Value Customers":
    st.title("High-Value Customer Analysis")

    hv = filtered_df[filtered_df['BalanceSegment'] == 'High']

    hv_rate = hv['Exited'].mean()
    hv_count = len(hv)
    revenue_loss = hv[hv['Exited'] == 1]['Balance'].sum()

    col1, col2, col3 = st.columns(3)
    col1.metric("High Value Customers", hv_count)
    col2.metric("Churn Rate", f"{hv_rate:.2%}")
    col3.metric("Revenue Loss", f"{revenue_loss:,.0f}")

    fig, ax = plt.subplots()
    sns.boxplot(x='Exited', y='Balance', data=hv, ax=ax)
    st.pyplot(fig)

    st.error("High-value customers contribute significantly to revenue loss.")

# =========================
# PAGE 5: Visualizations
# =========================
elif page == "Visualizations":
    st.title("Advanced Visualizations")

    st.subheader("Churn Distribution")
    fig, ax = plt.subplots()
    filtered_df['Exited'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
    st.pyplot(fig)

    st.subheader("Products vs Churn")
    fig2, ax2 = plt.subplots()
    sns.countplot(x='NumOfProducts', hue='Exited', data=filtered_df, ax=ax2)
    st.pyplot(fig2)

    st.subheader("Age Distribution")
    fig3, ax3 = plt.subplots()
    filtered_df['Age'].hist(ax=ax3)
    st.pyplot(fig3)

# =========================
# PAGE 6: Result Summary
# =========================
elif page == "Result Summary":
    st.title("Key Findings")

    st.write("""
    - Overall churn rate is approximately 20%
    - Germany has the highest churn rates
    - Customers aged 46–60 are most likely to churn
    - Inactive members show higher churn
    - High-balance customers contribute significantly to revenue loss
    """)

# =========================
# PAGE 7: Business Recommendations
# =========================
elif page == "Business Recommendations":
    st.title("Recommendations")

    st.write("""
    1. Focus retention strategies in Germany
    2. Target customers aged 46–60
    3. Improve engagement for inactive users
    4. Provide personalized services to high-value customers
    5. Implement predictive churn models for early intervention
    """)
