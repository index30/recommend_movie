import pandas as pd
from recommend import Recommend


data_path = "ml-100k/u.data"
item_path = "ml-100k/u.item"
user_path = "ml-100k/u.user"


def test_movie_genre():
    genre = ["unknown", "action", "adventure", "animation", "children's",
             "comedy", "crime", "documentary", "drama", "fantasy", "film-noir",
             "horror", "musical", "mystery", "romance", "sci-fi", "thriller",
             "war", "western"]
    mov_list = pd.read_csv('ml-100k/u.item', sep='|',
                           encoding='latin-1', header=None)
    mov = mov_list.iloc[0, :]
    gen = Recommend.movie_genre(mov)
    for g in gen:
        assert g in genre
