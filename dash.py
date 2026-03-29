import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("bank.csv")
st.set_page_config(page_title="Real Time Science Dashboard", page_icon='✅', layout="wide")

st.title("Real Time Data Analysis")
# Filtre sur le type job
job_filter = st.selectbox("Select a job", pd.unique(df["job"]))
# Creer un endroit pour le filtre
df = df[df["job"] == job_filter]

# INDICATEURS
avg_age = np.mean(df.age)
count_married = int(df[(df["marital"]== 'married')]['marital'].count())
balance = np.mean(df["balance"])

kpi1, kpi2, kpi3 = st.columns(3)

kpi1.metric(label="Age", value=round(avg_age), delta=round(avg_age))
kpi2.metric(label="Married Count", value=int(count_married), delta=round(count_married))
kpi3.metric(label="Balance $", value=f"${round(balance,2)}", delta=round(balance/count_married)*100)

# Graphiques
col1, col2 = st.columns(2)
with col1:
    st.markdown("### FIRST CHART")
    fig1 = plt.figure()
    sns.barplot(data=df, y='age', x='marital', palette= 'mako')
    st.pyplot(fig1)
with col2:
    st.markdown("### SECOND CHART")
    fig2 = plt.figure()
    sns.histplot(data=df, x='age')
    st.pyplot(fig2)

st.markdown("### DETAILED DATA VIEW")
st.dataframe(df)
