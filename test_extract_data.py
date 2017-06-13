from extract_data import Extract_data
import pandas as pd
import numpy as np


def test_collect_data():
    with open("ml-100k/u.data", 'r') as f:
        number = 4
        cut = "\t"
        c_data = Extract_data.collect_data(f, number, cut)
        assert (number-1) == len(c_data['1'][0])


def test_make_mat():
    with open("ml-100k/u.data", 'r') as f:
        number = 4
        cut = "\t"
        c_data = Extract_data.collect_data(f, number, cut)
        mov_id = []
        mov_list = pd.read_csv('ml-100k/u.item', sep='|',
                               encoding='latin-1', header=None)
        mov_list.iloc[0, 5] = 'test'
        mat = Extract_data.make_mat(c_data, mov_list)
        assert all(isinstance(x, np.float64) for x in list(mat[0]))


def test_devide_age():
    pass


def test_user_title():
    with open("ml-100k/u.data", 'r') as f:
        number = 4
        cut = "\t"
        c_data = Extract_data.collect_data(f, number, cut)
        mov_id = []
        mov_list = pd.read_csv('ml-100k/u.item', sep='|',
                               encoding='latin-1', header=None)
        P = Extract_data.user_title(c_data, mov_list)
        for u in c_data['1']:
            mov_id += [int(u[0])-1]
        p_list = [P[0, x] for x in mov_id]
        assert all(p == 1 for p in p_list)
