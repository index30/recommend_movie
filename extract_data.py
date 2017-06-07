# 与えられたデータをユーザごとにグループ分け
import pandas as pd
import numpy as np


# データを集める
# ex. {'ユーザ名': [[item1], [item2], ...]}
def collect_data(f, rec_num, cut):
    lines = f.readlines()
    dic = {}
    for l in lines:
        item = (l.strip()).split(cut)
        if item[0] in dic:
            dic[item[0]] += [item[1:rec_num]]
        else:
            dic[item[0]] = [item[1:rec_num]]
    return dic


# 各ユーザのジャンルごとの評価総数行列
def make_mat(dic, mov):
    P = np.zeros((len(dic), 19))
    # d:ユーザID
    for d in dic:
        # i_d = [アイテムID, 評価, タイムスタンプ]
        for i_d in dic[d]:
            # 映画の情報をベクトル化
            P[int(d)-1, :] += np.array(list(mov_list.iloc[int(i_d[0])-1, 5:24]))*int(i_d[1])
    return P


# 年代ごとに整理する関数
def divide_age(P, user):
    age = np.zeros((10, 19))
    for (i, p) in enumerate(P):
        u_info = user[str(i+1)][0]
        age_num = int(round(int(u_info[0])*(10**-1)))
        age[age_num-1, :] += p
    return age


# 類似ユーザの検索
# ユーザごとのベクトルをユークリッド距離にて類似してるかを判断
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
    return u_vec, val, vec

if __name__ == '__main__':
    data_path = "ml-100k/u.data"
    item_path = "ml-100k/u.item"
    user_path = "ml-100k/u.user"

    with open(data_path, 'r') as d, open(user_path, 'r') as u:
        # データの配列
        data_dic = collect_data(d, 4, "\t")
        # 映画のリスト
        mov_list = pd.read_csv('ml-100k/u.item', sep='|',
                               encoding='latin-1', header=None)
        # ユーザの情報の配列
        user_dic = collect_data(u, 5, "|")
        P = make_mat(data_dic, mov_list)

        # 年代ごとに整理
        A = divide_age(P, user_dic)
        # print(A)
        # print(P[0, :])

        # 類似するユーザの検索
        u_vec, val, vec = similar_user(P, 1)
        print(u_vec)
        print(val)
        print(vec)
