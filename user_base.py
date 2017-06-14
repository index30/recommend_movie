import numpy as np


class User_base:
    # 類似ユーザの検索
    # ユーザごとのベクトルを、ユークリッド距離を用いて類似してるか計算
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
                sim_id = i
        return u_vec, sim_id, vec
