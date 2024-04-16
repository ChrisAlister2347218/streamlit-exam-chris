import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    st.subheader("Data Visualization")
    df = pd.read_csv("WomensClothingE-CommerceReviews.csv")
    st.write(df.head())

    # 3D Scatter Plot
    st.subheader("3D Scatter Plot")
    x_col = st.selectbox("Select X-axis column", ["Age", "Rating", "Positive Feedback Count"], key="x_col_3d")
    y_col = st.selectbox("Select Y-axis column", ["Age", "Rating", "Positive Feedback Count"], key="y_col_3d")
    z_col = st.selectbox("Select Z-axis column", ["Age", "Rating", "Positive Feedback Count"], key="z_col_3d")
    color_col = st.selectbox("Select color column", df.columns, key="color_col_3d")

    fig = px.scatter_3d(df, x=x_col, y=y_col, z=z_col, color=color_col)
    st.plotly_chart(fig)

    # Bar Plot
    st.subheader("Bar Plot")
    x_col_bar = st.selectbox("Select X-axis column", ["Age", "Rating", "Positive Feedback Count"], key="x_col_bar")
    y_col_bar = st.selectbox("Select Y-axis column", ["Age", "Rating", "Positive Feedback Count"], key="y_col_bar")
    color_col_bar = st.selectbox("Select color column", ["Age", "Rating", "Positive Feedback Count"], key="color_col_bar")

    fig_bar = px.bar(df, x=x_col_bar, y=y_col_bar, color=color_col_bar)
    st.plotly_chart(fig_bar)

    # Histogram
    st.subheader("Histogram")
    hist_col = st.selectbox("Select column for histogram", ["Age", "Rating", "Positive Feedback Count"], key="hist_col")
    color_col_hist = st.selectbox("Select color column", df.columns, key="color_col_hist")

    fig_hist = px.histogram(df, x=hist_col, color=color_col_hist)
    st.plotly_chart(fig_hist)

if __name__ == "__main__":
    app()