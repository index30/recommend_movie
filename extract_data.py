# 与えられたデータをユーザごとにグループ分け
import pandas as pd
import numpy as np


# データを集める
# ex. {'ユーザ名': [[item1], [item2], ...]}
def collect_data(f, rec_num):
    lines = f.readlines()
    dic = {}
    for l in lines:
        item = (l.strip()).split()
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


if __name__ == '__main__':
    data_path = "ml-100k/u.data"
    item_path = "ml-100k/u.item"

    with open(data_path, 'r') as d:
        # ユーザの配列
        user_dic = collect_data(d, 4)
        # 映画のリスト
        mov_list = pd.read_csv('ml-100k/u.item', sep='|',
                               encoding='latin-1', header=None)
        P = make_mat(user_dic, mov_list)
        print(P[0, :])
