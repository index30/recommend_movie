import pandas as pd
from main import Main
from extract_data import Extract_data
from user_base import User_base
from item_base import Item_base

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
    gen = Main.movie_genre(mov)
    for g in gen:
        assert g in genre
