import pandas as pd

movies = pd.read_csv("data/raw/movies.csv")
ratings = pd.read_csv("data/raw/ratings.csv")

movie_ratings = pd.merge(ratings, movies, on="movieId")

movie_matrix = movie_ratings.pivot_table(
    index="userId",
    columns="title",
    values="rating"
)

def recommend(movie_title):

    movie_ratings = movie_matrix[movie_title]

    similar = movie_matrix.corrwith(movie_ratings)

    corr_df = pd.DataFrame(similar, columns=["correlation"])

    corr_df.dropna(inplace=True)

    rating_count = movie_ratings.groupby("title")["rating"].count()

    corr_df["rating_count"] = rating_count

    recommendations = corr_df[corr_df["rating_count"] > 100] \
        .sort_values("correlation", ascending=False) \
        .head(10)

    return recommendations
