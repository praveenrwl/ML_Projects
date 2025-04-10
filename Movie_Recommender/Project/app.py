import streamlit as st
import pickle as pkl
import pandas as pd
import requests

def fetch_poster(movie_id):
    requests.get('')


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        movie_id = i[0]
        # Fetch Poster from API
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies    


movies_dict = pkl.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pkl.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movies_names= st.selectbox(
    "Search Your Movies Here",
    movies['title'].values,
)



if st.button("Recommend"):
    recommendations = recommend(selected_movies_names)

    for i in recommendations:
        st.write(i)


