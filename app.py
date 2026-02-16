import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 AI Productivity Analysis System")

uploaded_file = st.file_uploader("Upload productivity CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df['Date'] = pd.to_datetime(df['Date'])

    df['Productivity_Score'] = (
        df['Tasks_Completed'] * 10
        - df['Errors'] * 5
        - (df['Task_Duration(min)'] / 10)
    )

    df['Status'] = ["Burnout Risk" if e > 2 else "Normal" for e in df['Errors']]

    st.subheader("Data Table")
    st.dataframe(df)

    st.subheader("Productivity Trend")

    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Productivity_Score'], marker='o')
    ax.set_xlabel("Date")
    ax.set_ylabel("Score")
    st.pyplot(fig)
