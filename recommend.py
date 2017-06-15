from extract_data import ExtractData
from user_base import UserBase
from item_base import ItemBase
import numpy as np
import pandas as pd
from operator import itemgetter


class Recommend:
    def recommend(args):
        data = ExtractData("ml-100k/u.data")
        user = ExtractData("ml-100k/u.user")
        d_dic = data.collect_data(4, "\t")
        m_list = pd.read_csv('ml-100k/u.item', sep='|',
                             encoding='latin-1', header=None)
        if args.item:
            print("[Item-base recommend]")
            mat = ItemBase.item_mat(d_dic)
            Recommend.item_recommend(d_dic, int(args.item[0]), mat, m_list)
        elif args.user:
            print("[User-base recommend]")
            # 高速で簡素な検索をする場合
            # M = user.genre_distribution(5, "|")
            # 評価値を考えた検索をする場合
            M = data.genre_eval(4, "\t")
            u_vec, sim_id, vec = UserBase.similar_user(M, int(args.user[0]))
            Recommend.user_recommend(int(args.user[0]), sim_id, d_dic, m_list)

    # 映画のジャンルを出力
    def movie_genre(mov_list):
        genre = ["unknown", "action", "adventure", "animation", "children's",
                 "comedy", "crime", "documentary", "drama", "fantasy", "film-noir",
                 "horror", "musical", "mystery", "romance", "sci-fi", "thriller",
                 "war", "western"]
        mov = list(map(int, mov_list[5:]))
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
            arr = np.array(list(mov.iloc[int(u[0])-1, :]))
            if not u[0] in i_mov and int(u[1]) > 3:
                print(arr[1] + " ... genre is", end='')
                [print(" <" + g + ">", end='') for g in Recommend.movie_genre(arr)]
                print("")
                count += 1

    # 最も選ばれる確率の高い映画の推薦
    def item_recommend(dic, u_id, mat, mov):
        u_dic = dic[str(u_id)]
        rec_list = [ItemBase.for_rec_table(mat, int(item[0])) for item in u_dic]
        sort_list = sorted(rec_list, key=itemgetter(0))[::-1]
        mov_num = sort_list[0][1]
        arr = mov.iloc[mov_num, :]
        print(arr[1] + "... genre is", end='')
        [print(" <" + g + ">", end='') for g in Recommend.movie_genre(arr)]
        print("")
