# 仮定として、ユーザ登録されているレビュワーのみを対象
# ユーザIDを入力することで、そのユーザにオススメの映画をレコメンドする
from extract_data import Extract_data
import numpy as np
import pandas as pd


# 類似ユーザの検索
# ユーザごとのベクトルを、ユークリッド距離を用いて類似してるか計算
def similar_user(P, u_id):
    u_vec = P[u_id-1, :]
    val = float('inf')
    for (i, p) in enumerate(P):
        if u_id-1 == i:
            continue
        print(i)
        tmp = np.linalg.norm(u_vec - p)
        if tmp < val:
            val = tmp
            vec = p
    return u_vec, val, vec


if __name__ == "__main__":
    data_path = "ml-100k/u.data"
    item_path = "ml-100k/u.item"
    user_path = "ml-100k/u.user"

    with open(data_path, 'r') as d, open(user_path, 'r') as u:
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

        # 類似するユーザの検索
        u_vec, val, vec = similar_user(P, 1)
        print(u_vec)
        print(val)
        print(vec)
