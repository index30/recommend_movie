import pandas as pd
import numpy as np


# データの整理(1つの行列に)
class ExtractData:
    def __init__(self, path):
        self.data = path
        self.item = "ml-100k/u.item"

    # データを辞書型に集める
    # ex. {'ユーザ名': [[item1], [item2], ...]}
    def collect_data(self, cut, delim):
        with open(self.data) as data, open(self.item) as item:
            lines = data.readlines()
            dic = {}
            for line in lines:
                l = line.strip().split(delim)
                if l[0] in dic:
                    dic[l[0]].append(l[1:cut])
                else:
                    dic[l[0]] = [l[1:cut]]
        return dic

    # 各ユーザのジャンルごとの評価総数行列
    # ジャンルごとの評価値を考慮した場合のメソッド
    def genre_eval(self, cut, delim):
        mov_list = pd.read_csv(self.item, sep='|',
                               encoding='latin-1', header=None)
        dic = self.collect_data(cut, delim)
        P = np.zeros((len(dic), 19))
        # d:ユーザID
        for d in dic:
            # i_d = [アイテムID, 評価, タイムスタンプ]
            for i_d in dic[d]:
                # 映画の情報をベクトル化
                # 評価したかどうかだけでなく、評価の点数も考慮してベクトル生成
                tmp = mov_list.iloc[int(i_d[0])-1, 5:]
                tmp_val = list(map(str.isdigit, list(map(str, tmp))))
                if all(tmp_val) and tmp_val[0] is True:
                    col_genre = list(mov_list.iloc[int(i_d[0])-1, 5:])
                    P[int(d)-1, :] += np.array(col_genre)*int(i_d[1])
        return P

    # 縦: ユーザID, 横: 映画のID
    # であるような行列を生成
    # ジャンルごとの評価値は考慮しておらず、計算が高速
    def genre_distribution(self, cut, delim):
        mov_list = pd.read_csv(self.item, sep='|',
                               encoding='latin-1', header=None)
        dic = self.collect_data(cut, delim)
        mat = np.zeros((len(dic), len(mov_list)))
        for usr in dic:
            for u in dic[usr]:
                mat[int(usr)-1][int(u[0])-1] = 1
        return mat
