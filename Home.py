import streamlit as st
import pandas as pd

def app():
    st.title("Women's Clothing E-Commerce Dataset Analysis")
    st.write("This is an interactive web application for analyzing the Women's Clothing E-Commerce dataset. The application provides the following features:")

    st.subheader("Features")
    st.write("1. **3D Plot Visualization**")
    st.write("Visualize the relationship between the Age, Rating, and Positive Feedback Count columns using a 3D scatter plot.")

    st.write("2. **Image Processing**")
    st.write("Upload an image and apply various image processing techniques, such as resizing, grayscale conversion, color mode conversion, cropping, and rotation.")

    st.write("3. **Text Similarity Analysis**")
    st.write("Perform text preprocessing on the 'Review Text' column, including tokenization, stopword removal, stemming, and punctuation removal. Analyze text similarity within different divisions ('General', 'General Petite', and 'Initmates') using cosine similarity.")

    st.subheader("Dataset")
    st.write("The application uses the Women's Clothing E-Commerce dataset, which contains customer reviews for women's clothing products. The dataset includes the following columns:")

    

    df = pd.read_csv("WomensClothingE-CommerceReviews.csv")
    st.write(df.head())

if __name__ == "__main__":
    app()