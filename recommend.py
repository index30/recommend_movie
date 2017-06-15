from extract_data import Extract_data
from user_base import User_base
from item_base import Item_base
import numpy as np
import pandas as pd
from operator import itemgetter


class Recommend:
    def recommend(args):
        data_path = "ml-100k/u.data"
        item_path = "ml-100k/u.item"
        user_path = "ml-100k/u.user"
        with open(data_path, 'r') as d, open(item_path, 'r') as i, open(user_path, 'r') as u:
            d_dic = Extract_data.collect_data(d, 4, "\t")
            m_list = pd.read_csv('ml-100k/u.item', sep='|',
                                 encoding='latin-1', header=None)
            u_dic = Extract_data.collect_data(u, 5, "|")
            if args.item:
                print("[Item-base recommend]")
                mat = Item_base.item_mat(d_dic)
                Recommend.item_recommend(d_dic, int(args.item[0]), mat, m_list)
            elif args.user:
                print("[User-base recommend]")
                M = Extract_data.user_title(u_dic, m_list)
                u_vec, sim_id, vec = User_base.similar_user(M, int(args.user[0]))
                Recommend.user_recommend(int(args.user[0]), sim_id, d_dic, m_list)

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
    def user_recommend(i_id, u_id, dic, mov):
        i_dic = dic[str(i_id)]
        u_dic = dic[str(u_id)]
        i_mov = [x[0] for x in i_dic]
        count = 0
        for u in u_dic:
            if count > 9:
                continue
            arr = np.array(list(mov.iloc[int(u[0])-1,:]))
            if not u[0] in i_mov and int(u[1]) > 3:
                print(arr[1] + " ... genre is", end='')
                [print(" <" + g + ">", end='') for g in Recommend.movie_genre(arr)]
                print("")
                count += 1

    # 最も選ばれる確率の高い映画の推薦
    def item_recommend(dic, u_id, mat, mov):
        u_dic = dic[str(u_id)]
        rec_list = [Item_base.for_rec_table(mat, int(item[0])) for item in u_dic]
        sort_list = sorted(rec_list, key=itemgetter(0))[::-1]
        mov_num = sort_list[0][1]
        arr = mov.iloc[mov_num, :]
        print(arr[1] + "... genre is", end='')
        [print(" <" + g + ">", end='') for g in Recommend.movie_genre(arr)]
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
        # P = Extract_data.make_mat(data_dic, mov_list)

        # 年代ごとに整理
        #A = Extract_data.divide_age(P, user_dic)

        # ユーザのもつ映画評価
        M = Extract_data.user_title(user_dic, mov_list)

        # 類似するユーザの検索
        # ジャンルの蓄積情報のみを用いた場合
        # u_vec, sim_id, vec = similar_user(P, input_id)
        # ユーザのもつ映画評価を元に検索する場合
        u_vec, sim_id, vec = User_base.similar_user(M, input_id)
        # 映画推薦の出力部分
        print("User-base recommend ...")
        Recommend.user_recommend(input_id, sim_id, data_dic, mov_list)
        print("")
        print("Item-base recommend...")
        mat = Item_base.item_mat(data_dic)
        Recommend.item_recommend(data_dic, input_id, mat, mov_list)
