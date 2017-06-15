import numpy as np

ITEMAX = 1682


# アイテムベースでのレコメンド
# 評価に寄らず、アイテムの共起に着目
class ItemBase:
    # 同一人物が購入した商品の組み合わせ
    def item_mat(dic):
        M = np.zeros((ITEMAX, ITEMAX))
        for d in dic:
            item = dic[d]
            for (i, j) in enumerate(item):
                m = [int(t[0]) for (s, t) in enumerate(item) if i != s]
                for ele in m:
                    M[int(j[0])-1, ele-1] += 1
        # 正規化
        for k in range(ITEMAX):
            sum_c = sum(M[:, k])
            M[:, k] = M[:, k]/sum_c
        return M

    # ある映画のタイトルと共に評価されている映画の選出
    def for_rec_table(mat, mov_num):
        target = mat[:, mov_num]
        sort_val = np.sort(target)[::-1]
        index = np.argsort(target)[::-1]
        mov_pair = (sort_val[0], index[0])
        return mov_pair
