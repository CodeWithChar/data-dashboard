import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
st.title("📊 Simple Data Dashboard")
st.write("Upload your CSV file to analyze the data.")

uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("📌 Raw Data")
    st.dataframe(df.head())

    # Basic Statistics
    st.subheader("📈 Data Summary")
    st.write(df.describe())

    # Visualization
    st.subheader("📊 Sales vs. Profit")

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.lineplot(x=df["Date"], y=df["Sales"], label="Sales", marker="o")
    sns.lineplot(x=df["Date"], y=df["Profit"], label="Profit", marker="o")
    
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    
    st.pyplot(fig)
