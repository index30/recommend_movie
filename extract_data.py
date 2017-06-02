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


def make_mat(dic, mov):
    P = np.zeros((len(dic), 19))
    for d in dic:
        print(len(dic[d]))
        for i_d in dic[d]:
            P[int(d)-1, :] += np.array(list(mov_list.iloc[int(i_d[0])-1, 5:24]))
            # print(i_d[0])
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
        # print(mov_list.iloc[1, 4:24])
        # [print(x) for x in mov_list.iloc[1, 4:24]]
        # print(np.array(list(mov_list.iloc[1, 5:24])))
        # mov_dic = collect_data(i, 24)
        P = make_mat(user_dic, mov_list)
        print(P[0, :])
        print(len(user_dic['1']))
