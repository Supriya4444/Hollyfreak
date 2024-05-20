import time

import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    dist = llr[movie_index]
    movie_list = sorted(list(enumerate(dist)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []

    for i in movie_list:
        movie_id = i[0]
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

llr = pickle.load(open('llr.pkl', 'rb'))


st.title(":red[Movies Recommendation System]")
option = st.selectbox(
    'Select any movie from the provided list to get recommendations : ',
    movies['title'].values)


st.header(' ', divider='rainbow')
st.caption(':green[Tap "Recommend" button to get results !!]')


st.button("Reset", type="primary")
if st.button("Recommend"):
    recommendations = recommend(option)
    for i in recommendations:
        st.write(i)
else:
    st.write("Please select movie name!")
st.caption(':blue[_Hope this is helpful_]:sunglasses:')


st.image('C:\\Users\\Supriya\\OneDrive\\Pictures\\Camera Roll\\jnina.jpg',width=700)
