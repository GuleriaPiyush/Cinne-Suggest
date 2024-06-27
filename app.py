#Final Project File d

import pickle

import streamlit as st
import pandas as pd


def Recommand(movie):
    movie_index = Movies[Movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie_names = []
    for i in movies_list:
        recommended_movie_names.append(Movies.iloc[i[0]].title)
    return recommended_movie_names


st.title("Cinne Suggest: The Movie Recommder System")

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
Movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

selected_movie_name = st.selectbox(
    'Enter a movie name you liked or type of movie you like So we can recommand you better ;)',
Movies['title'].values)

if st.button('Recommend '):
    recomandations = Recommand(selected_movie_name)
    for i in recomandations:
        st.write(i)
