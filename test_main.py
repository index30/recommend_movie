import pandas as pd
from main import Main
from extract_data import Extract_data

data_path = "ml-100k/u.data"
item_path = "ml-100k/u.item"
user_path = "ml-100k/u.user"


def test_similar_user():
    with open(user_path, 'r') as u:
        mov_list = pd.read_csv('ml-100k/u.item', sep='|',
                               encoding='latin-1', header=None)
        user_dic = Extract_data.collect_data(u, 5, "|")
        M = Extract_data.user_title(user_dic, mov_list)
        M[0, :] = M[0, :]*0
        M[5, :] = M[5, :]*0
        u_vec, sim_id, vec = Main.similar_user(M, 1)
        assert sim_id == 5

