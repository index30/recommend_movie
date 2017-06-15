# ユーザベースのレコメンド
import numpy as np


class UserBase:
    # 類似ユーザの検索
    # ユーザごとのベクトルを、ユークリッド距離を用いて類似しているユーザを出力
    def similar_user(P, u_id):
        u_vec = P[u_id-1, :]
        u_val = float('inf')
        for (i, p) in enumerate(P):
            if u_id-1 == i:
                continue
            tmp = np.linalg.norm(u_vec - p)
            if tmp < u_val:
                u_val = tmp
                sim_vec = p
                sim_id = i+1
        # u_vec...指定したユーザのベクトル
        # sim_id...類似したユーザと判断されたユーザのid
        # sim_vec...類似したユーザのベクトル
        return u_vec, sim_id, sim_vec
