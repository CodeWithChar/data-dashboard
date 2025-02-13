import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("📊 Interactive Data Visualization")

# Upload CSV
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview", df.head())

    # Select Column for Visualization
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    selected_col = st.selectbox("Choose a numeric column", numeric_cols)

    # Choose Plot Type
    plot_type = st.radio("Select a plot type:", ["Histogram", "Boxplot", "Scatterplot"])

    fig, ax = plt.subplots()
    
    if plot_type == "Histogram":
        sns.histplot(df[selected_col], bins=30, kde=True, ax=ax)
        ax.set_title(f"Histogram of {selected_col}")
    
    elif plot_type == "Boxplot":
        sns.boxplot(y=df[selected_col], ax=ax)
        ax.set_title(f"Boxplot of {selected_col}")
    
    elif plot_type == "Scatterplot":
        second_col = st.selectbox("Choose another numeric column for scatterplot", numeric_cols)
        sns.scatterplot(x=df[selected_col], y=df[second_col], ax=ax)
        ax.set_title(f"Scatterplot of {selected_col} vs {second_col}")

    st.pyplot(fig)
