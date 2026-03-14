# Movie Recommendation System

## Overview

This project builds a **movie recommendation system** that suggests similar movies based on user preferences.

The goal of the project is to demonstrate how recommendation systems work using **content-based filtering** with movie metadata.

The system analyzes movie features such as genres and descriptions to recommend movies that are similar to the one a user selects.

---

## Dataset

This project uses the **MovieLens dataset**, which contains movie information and user ratings.

Main files used:

- `movies.csv` — movie titles and genres
- `ratings.csv` — user ratings for movies

The dataset is commonly used for building recommendation systems and collaborative filtering models.

---

## Recommendation Method

The recommendation engine uses **Content-Based Filtering**.

Steps used in the recommendation pipeline:

1. Load movie dataset
2. Preprocess movie metadata
3. Convert text features into numerical vectors
4. Compute similarity between movies using **cosine similarity**
5. Recommend the most similar movies to the selected movie

---

## Project Structure

```
movie-recommendation-system-khatantamir
│
├── app
│   └── main.py
│
├── data
│   └── raw
│       ├── movies.csv
│       └── ratings.csv
│
├── models
│
├── notebooks
│   └── exploration.ipynb
│
├── src
│   └── recommender.py
│
├── requirements.txt
└── README.md
```

---

## Technologies Used

- Python
- pandas
- scikit-learn
- numpy
- Jupyter Notebook

---

## Running the Project

Install dependencies:

```
pip install -r requirements.txt
```

Run the recommendation script:

```
from src.recommender import recommend
recommend("Toy Story (1995)")
```

---

## Example Output

Example recommendation results:

```
Input Movie:
Toy Story (1995)

Recommended Movies:
Toy Story 2 (1999)
A Bug's Life (1998)
Monsters, Inc. (2001)
Finding Nemo (2003)
Up (2009)
```

---

## Future Improvements

Possible improvements for this project:

- Add collaborative filtering
- Build a hybrid recommendation system
- Deploy the model as an API
- Create a simple web interface for users

---

## Author

**Khatantamir Otgonbyamba**
