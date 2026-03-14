# Movie Recommendation System

This project builds a movie recommendation system using collaborative filtering.

The system analyzes user ratings and recommends similar movies based on correlation between user preferences.

## Dataset

MovieLens dataset was used.

Files:

data/raw/movies.csv
data/raw/ratings.csv

## Method

The recommendation system uses:

* User-movie rating matrix
* Pearson correlation
* Popularity filtering

Steps:

1. Merge movies and ratings datasets
2. Create a user-movie pivot table
3. Calculate correlation between movies
4. Filter movies with enough ratings
5. Return top similar movies

## Example

Input:

Toy Story (1995)

Output recommendations:

* The Incredibles
* Finding Nemo
* Aladdin
* Monsters Inc
* Mrs. Doubtfire

## Project Structure

```
movie-recommendation-system-khatantamir
│
├── app/                # Application layer (future Streamlit web app)
├── data/               # Dataset files
│   └── raw/
│       ├── movies.csv
│       └── ratings.csv
│
├── models/             # Saved models (if used later)
│
├── notebooks/          # Jupyter notebooks for exploration
│   └── 01_data_exploration.ipynb
│
├── src/                # Source code
│   └── recommender.py
│
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## How to Run

Install dependencies:

pip install -r requirements.txt

Run the recommendation function:

from src.recommender import recommend
recommend("Toy Story (1995)")

The system will return the top 10 most similar movies based on user rating patterns.
