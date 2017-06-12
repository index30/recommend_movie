#!/usr/local/Cellar/python3/3.5.1/bin/python3.5

# 仮定として、ユーザ登録されているレビュワーのみを対象
# ユーザIDを入力することで、そのユーザにオススメの映画をレコメンドする
from extract_data import Extract_data
import numpy as np
import pandas as pd


class Main:
    # 類似ユーザの検索
    # ユーザごとのベクトルを、ユークリッド距離を用いて類似してるか計算
    def similar_user(P, u_id):
        u_vec = P[u_id-1, :]
        val = float('inf')
        for (i, p) in enumerate(P):
            if u_id-1 == i:
                continue
            tmp = np.linalg.norm(u_vec - p)
            if tmp < val:
                val = tmp
                vec = p
                sim_id = i
        return u_vec, sim_id, vec


    # 映画のジャンルを出力
    def movie_genre(mov_list):
        genre = ["unknown", "action", "adventure", "animation", "children's",
                 "comedy", "crime", "documentary", "drama", "fantasy", "film-noir",
                 "horror", "musical", "mystery", "romance", "sci-fi", "thriller",
                 "war", "western"]
        mov = list(map(int, mov_list[5:24]))
        m_genre = [g for (g,m) in zip(genre, mov) if m == 1]
        return m_genre


    # 類似ユーザを元に映画推薦
    def recommand(i_id, u_id, dic, mov):
        i_dic = dic[str(i_id)]
        u_dic = dic[str(u_id)]
        i_mov = [x[0] for x in i_dic]
        for u in u_dic:
            arr = np.array(list(mov.iloc[int(u[0])-1,:]))
            if not u[0] in i_mov and int(u[1]) > 3:
                print(arr[1] + " ... genre is", end='')
                [print(" <" + g + ">", end='') for g in Main.movie_genre(arr)]
                print("")


if __name__ == "__main__":
    data_path = "ml-100k/u.data"
    item_path = "ml-100k/u.item"
    user_path = "ml-100k/u.user"

    input_id = int(input("please input your ID: "))

    with open(data_path, 'r') as d, open(item_path, 'r') as i, open(user_path, 'r') as u:
        # データの配列
        data_dic = Extract_data.collect_data(d, 4, "\t")
        # 映画のリスト
        mov_list = pd.read_csv('ml-100k/u.item', sep='|',
                               encoding='latin-1', header=None)
        # ユーザの情報の配列
        user_dic = Extract_data.collect_data(u, 5, "|")
        P = Extract_data.make_mat(data_dic, mov_list)

        # 年代ごとに整理
        A = Extract_data.divide_age(P, user_dic)

        # ユーザのもつ映画評価
        M = Extract_data.user_title(user_dic, mov_list)

        # 類似するユーザの検索
        # ジャンルの蓄積情報のみを用いた場合
        # u_vec, sim_id, vec = similar_user(P, input_id)
        # ユーザのもつ映画評価を元に検索する場合
        u_vec, sim_id, vec = Main.similar_user(M, input_id)
        # 映画推薦の出力部分
        print("We recommend ...")
        Main.recommand(input_id, sim_id, data_dic, mov_list)
