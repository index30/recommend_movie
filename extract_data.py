# データの整理(1つの行列に)
import pandas as pd
import numpy as np


# データを辞書型に集める
# ex. {'ユーザ名': [[item1], [item2], ...]}
# 入力: f_path...ファイルのパス
#       cut...配列をカットする箇所
#       delim...区切り文字指定
# 出力: dic...辞書型に集められたデータ
def collect_data(f_path, cut, delim):
    with open(f_path) as data:
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
# 入力: dic...ユーザとユーザが評価した映画の情報が紐づいた辞書型の配列
#       m_list...映画の情報が格納された配列
# 出力: ユーザ(縦軸)と映画のジャンル(横軸)を示した行列
def genre_eval(dic, mov_list):
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
def genre_distribution(dic, mov_list):
    mat = np.zeros((len(dic), len(mov_list)))
    for usr in dic:
        for u in dic[usr]:
            mat[int(usr)-1][int(u[0])-1] = 1
    return mat
