import pickle
import streamlit as st
import requests


st.set_page_config(layout="wide")

st.markdown("""
    <style>
    .movie-title {
        height: 50px; 
        overflow: hidden;
        text-align: center;
        font-size: 16px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .stImage img {
        height: 350px !important;
        object-fit: cover;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names, recommended_movie_posters

st.header('Movie Recommender System')
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    
    cols = [col1, col2, col3, col4, col5]
    
    for i in range(5):
        with cols[i]:
            st.markdown(f'<div class="movie-title">{recommended_movie_names[i]}</div>', unsafe_allow_html=True)
            st.image(recommended_movie_posters[i])