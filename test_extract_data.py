from extract_data import Extract_data
import pandas as pd


def test_collect_data():
    with open("ml-100k/u.data", 'r') as f:
        number = 4
        cut = "\t"
        c_data = Extract_data.collect_data(f, number, cut)
        assert (number-1) == len(c_data['1'][0])


def test_make_mat():
    pass


def test_devide_age():
    pass


def test_user_title():
    pass
