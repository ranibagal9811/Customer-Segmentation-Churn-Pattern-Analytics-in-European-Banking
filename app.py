import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

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
# Sidebar Filters
# -------------------------
st.sidebar.title("Filters")

geo_filter = st.sidebar.multiselect(
    "Geography", df['Geography'].unique(),
    default=df['Geography'].unique()
)

age_filter = st.sidebar.multiselect(
    "Age Group", df['AgeGroup'].unique(),
    default=df['AgeGroup'].unique()
)

tenure_filter = st.sidebar.multiselect(
    "Tenure Group", df['TenureGroup'].unique(),
    default=df['TenureGroup'].unique()
)

filtered_df = df[
    (df['Geography'].isin(geo_filter)) &
    (df['AgeGroup'].isin(age_filter)) &
    (df['TenureGroup'].isin(tenure_filter))
]

# -------------------------
# TITLE
# -------------------------
st.title("Customer Churn Analytics Dashboard")

# -------------------------
# KPIs
# -------------------------
st.subheader("Overall Churn Summary")

churn_rate = filtered_df['Exited'].mean()
total = len(filtered_df)
churned = filtered_df['Exited'].sum()

col1, col2, col3 = st.columns(3)
col1.metric("Total Customers", total)
col2.metric("Churned", churned)
col3.metric("Churn Rate", f"{churn_rate:.2%}")

# -------------------------
# Geography Churn
# -------------------------
st.subheader("Geography-wise Churn")

geo = filtered_df.groupby('Geography')['Exited'].mean().reset_index()

fig, ax = plt.subplots()
sns.barplot(data=geo, x='Geography', y='Exited', ax=ax)
st.pyplot(fig)

# -------------------------
# Age vs Tenure Heatmap
# -------------------------
st.subheader("Age & Tenure Churn")

pivot = pd.pivot_table(filtered_df,
                       values='Exited',
                       index='AgeGroup',
                       columns='TenureGroup')

fig2, ax2 = plt.subplots()
sns.heatmap(pivot, annot=True, ax=ax2)
st.pyplot(fig2)

# -------------------------
# High Value Customers
# -------------------------
st.subheader("High-Value Customer Analysis")

hv = filtered_df[filtered_df['BalanceSegment'] == 'High']

hv_rate = hv['Exited'].mean()
hv_count = len(hv)

c1, c2 = st.columns(2)
c1.metric("High Value Customers", hv_count)
c2.metric("High Value Churn Rate", f"{hv_rate:.2%}")

fig3, ax3 = plt.subplots()
sns.boxplot(x='Exited', y='Balance', data=hv, ax=ax3)
st.pyplot(fig3)

# -------------------------
# Top Risk Segments
# -------------------------
st.subheader("Top Risk Segments")

risk = filtered_df.groupby(['Geography','AgeGroup'])['Exited'].mean().reset_index()
top = risk.sort_values(by='Exited', ascending=False).head(5)

st.dataframe(top)

# -------------------------
# Drill Down
# -------------------------
st.subheader("Data Explorer")
st.dataframe(filtered_df)
