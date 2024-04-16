import streamlit as st
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import seaborn as sns
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt
import nltk
nltk.download('all')
nltk.download('stopwords')
nltk.download('punkt')

def app():
    st.subheader("Text Similarity Analysis")

    df = pd.read_csv("WomensClothingE-CommerceReviews.csv")

    # Text preprocessing
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    def preprocess_text(text):
        text = re.sub(r'[^a-zA-Z\s]', '', str(text).lower())
        tokens = word_tokenize(text)
        tokens = [word for word in tokens if word not in stop_words]
        tokens = [lemmatizer.lemmatize(word) for word in tokens]
        return ' '.join(tokens)

    df['Review Text'] = df['Review Text'].apply(preprocess_text)

    # Similarity analysis
    divisions = df['Division Name'].unique()

    division = st.selectbox("Select a division", divisions)

    selected_reviews = df[df['Division Name'] == division]['Review Text'].iloc[:10]  # Selecting only the first 10 reviews

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(selected_reviews)

    similarities = cosine_similarity(vectors)

    # Plot similarity heatmap
    st.write("Similarity Matrix:")
    fig, ax = plt.subplots()
    sns.heatmap(similarities, annot=True, cmap='coolwarm', xticklabels=False, yticklabels=False, ax=ax)
    st.pyplot(fig)

    # Display similar reviews
    st.write("Similar Reviews:")
    for i in range(len(similarities)):
        similar_indices = similarities[i].argsort()[:-6:-1]
        similar_reviews = [(selected_reviews.iloc[j], similarities[i][j]) for j in similar_indices if i != j]
        if similar_reviews:
            st.write(f"Review {i}: {selected_reviews.iloc[i]}")
            st.write("Similar reviews:")
            for review, similarity in similar_reviews:
                st.write(f"  {review} (Similarity: {similarity:.2f}")

if __name__ == "__main__":
    app()
