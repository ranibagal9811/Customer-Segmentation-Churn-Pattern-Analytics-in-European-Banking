# 📊 Customer Segmentation & Churn Pattern Analytics in European Banking

## 📌 Overview
Customer churn is one of the most critical challenges in retail banking. This project analyzes churn behavior using segmentation-driven analytics to identify high-risk customers and support data-driven retention strategies.

The project combines **exploratory data analysis, customer segmentation, and an interactive Streamlit dashboard** to provide actionable insights.

---

## 🎯 Objectives

### 🔹 Primary Objectives
- Measure overall churn rate
- Identify churn distribution across customer segments
- Compare churn behavior across European regions

### 🔹 Secondary Objectives
- Analyze churn among high-value customers
- Evaluate engagement and tenure patterns
- Support strategic and marketing decisions

---

## 📊 Dataset Description

| Feature | Description |
|--------|------------|
| CustomerId | Unique customer identifier |
| Geography | France, Germany, Spain |
| Gender | Male / Female |
| Age | Customer age |
| CreditScore | Creditworthiness score |
| Tenure | Years with bank |
| Balance | Account balance |
| NumOfProducts | Number of bank products |
| HasCrCard | Credit card ownership |
| IsActiveMember | Activity status |
| EstimatedSalary | Annual salary |
| Exited | Churn indicator (Target) |

---

## 🧠 Key Analysis Performed

### 🔹 Customer Segmentation
- Age Groups: `<30`, `30–45`, `46–60`, `60+`
- Credit Score Bands: Low, Medium, High
- Tenure Groups: New, Mid-term, Long-term
- Balance Segments: Zero, Low, High
- Geographic Segmentation

---

### 🔹 Churn Analysis
- Overall churn rate (~20%)
- Segment-wise churn comparison
- Geography–Age interaction analysis
- Churn contribution by segment size
- Churned vs retained customer comparison

---

### 🔹 Comparative Demographic Analysis
- Gender-based churn differences
- Geography vs Age interaction heatmaps
- Financial stability vs churn patterns

---

### 🔹 High-Value Customer Analysis
- Identification of high-balance churners
- Salary vs balance comparison
- Revenue loss estimation from churn

---

## 📈 Key Insights

- Churn rate is approximately **20%**
- **Germany** shows the highest churn rates
- Customers aged **46–60** are most likely to churn
- **Inactive customers** have significantly higher churn
- High-balance customers contribute major revenue loss
- Financial stability alone does not prevent churn

---

## 💻 Streamlit Dashboard Features

- 📊 KPI Metrics (Churn Rate, Customers, Revenue Impact)
- 🌍 Geography-wise churn visualization
- 🔥 Age & tenure heatmaps
- 💰 High-value customer churn analysis
- 🎯 Top risk segment identification
- 🔍 Interactive filters and drill-down views
- 📄 Summary & business recommendations

---

## 🚀 Tech Stack

- Python (Pandas, NumPy)
- Visualization (Seaborn, Matplotlib)
- Machine Learning (optional: Scikit-learn, XGBoost)
- Streamlit (Dashboard)

---


---

## 📌 Conclusion

This project demonstrates how segmentation-driven analytics can uncover deep insights into customer churn behavior. By identifying high-risk segments and quantifying financial impact, the analysis supports targeted and effective retention strategies.

---

## 🎯 Business Recommendations

- Focus retention efforts in high-risk regions (Germany)
- Target customers aged 46–60
- Improve engagement of inactive users
- Provide personalized services to high-value customers
- Implement predictive models for early churn detection

---

## 👩‍💻 Author
Rani Bagal
