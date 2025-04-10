import streamlit as st
import pickle as pkl  # Use pkl instead of pickle
import pandas as pd

# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = [movies.iloc[i[0]].title for i in movies_list]
    return recommended_movies    

# Load movie dictionary
movies_dict = pkl.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Load similarity matrix
similarity = pkl.load(open('similarity.pkl', 'rb'))

# Streamlit UI
st.title('🎬 Movie Recommender System')

selected_movie_name = st.selectbox(
    "🔍 Search for a Movie:",
    movies['title'].values,
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)

    st.subheader("📌 Recommended Movies:")
    for movie in recommendations:
        st.write(f"✅ {movie}")
