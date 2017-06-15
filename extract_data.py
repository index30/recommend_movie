import pandas as pd
import numpy as np


# データの整理(1つの行列に)
class ExtractData:
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
                # 評価したかどうかだけでなく、評価の点数も考慮してベクトル生成
                tmp = mov.iloc[int(i_d[0])-1, 5:24]
                tmp_val = list(map(str.isdigit, list(map(str, tmp))))
                if all(tmp_val) and tmp_val[0] is True:
                    P[int(d)-1, :] += np.array(list(mov.iloc[int(i_d[0])-1,
                                                             5:24]))*int(i_d[1])
        return P

    # 年代ごとに整理する関数(実装したが未使用)
    def divide_age(P, user):
        age = np.zeros((10, 19))
        for (i, p) in enumerate(P):
            u_info = user[str(i+1)][0]
            age_num = int(round(int(u_info[0])*(10**-1)))
            age[age_num-1, :] += p
        return age

    # 縦: ユーザID, 横: 映画のID
    # であるような行列を生成
    def user_title(user, mov):
        mat = np.zeros((len(user), len(mov)))
        for usr in user:
            for u in user[usr]:
                mat[int(usr)-1][int(u[0])-1] = 1
        return mat
