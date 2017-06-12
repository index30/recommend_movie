import pandas as pd
import numpy as np


# データの整理(1つの行列に)
class Extract_data:
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
                P[int(d)-1, :] += np.array(list(mov.iloc[int(i_d[0])-1,
                                                              5:24]))*int(i_d[1])
        return P

    # 年代ごとに整理する関数
    def divide_age(P, user):
        age = np.zeros((10, 19))
        for (i, p) in enumerate(P):
            u_info = user[str(i+1)][0]
            age_num = int(round(int(u_info[0])*(10**-1)))
            age[age_num-1, :] += p
        return age


    # 縦: ユーザID, 横: 映画のID
    def user_title(user, mov):
        mat = np.zeros((len(user), len(mov)))
        for usr in user:
            for u in user[usr]:
                mat[int(usr)-1][int(u[0])-1] = 1
        return mat

if __name__ == '__main__':
    data_path = "ml-100k/u.data"
    item_path = "ml-100k/u.item"
    user_path = "ml-100k/u.user"

    with open(data_path, 'r') as d, open(user_path, 'r') as u:
        # データの配列{'ユーザID':[アイテムID, 評価, タイムスタンプ]}
        data_dic = Extract_data.collect_data(d, 4, "\t")
        print(data_dic)
        print(len(data_dic))
        # 映画のリスト
        mov_list = pd.read_csv('ml-100k/u.item', sep='|',
                               encoding='latin-1', header=None)
        print(len(mov_list))
        # ユーザの情報の配列
        # user_dic = Extract_data.collect_data(u, 5, "|")
        # P = Extract_data.make_mat(data_dic, mov_list)

        # 年代ごとに整理
        # A = Extract_data.divide_age(P, user_dic)

        # ユーザが評価している映画を1, していないものを0とする行列の生成
        # mat = Extract_data.user_title(data_dic, mov_list)
        # print(mat)
