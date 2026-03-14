import streamlit as st
import pandas as pd

movies = pd.read_csv("data/raw/movies.csv")
ratings = pd.read_csv("data/raw/ratings.csv")

ratings_with_titles = pd.merge(ratings, movies, on="movieId")

movie_matrix = ratings_with_titles.pivot_table(
    index="userId",
    columns="title",
    values="rating"
)

def recommend(movie_title):
    target_ratings = movie_matrix[movie_title]

    similar = movie_matrix.corrwith(target_ratings)

    corr_df = pd.DataFrame(similar, columns=["correlation"])
    corr_df.dropna(inplace=True)

    rating_count = ratings_with_titles.groupby("title")["rating"].count()
    corr_df["rating_count"] = rating_count

    recommendations = corr_df[corr_df["rating_count"] > 100] \
        .sort_values("correlation", ascending=False) \
        .head(10)

    return recommendations

st.title("Movie Recommendation System")

movie_name = st.text_input("Enter a movie title:")

if st.button("Get Recommendations"):
    if movie_name in movie_matrix.columns:
        results = recommend(movie_name)
        st.write(results)
    else:
        st.write("Movie not found. Please try another title.")
