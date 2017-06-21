# extract_data.pyのテストコード
import extract_data
import pandas as pd
import numpy as np


def test_collect_data():
    number = 4
    cut = "\t"
    c_data = extract_data.collect_data("ml-100k/u.data", number, cut)
    assert (number-1) == len(c_data['1'][0])


def test_genre_eval():
    pass


def test_genre_distribution():
    pass
