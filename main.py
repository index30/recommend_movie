#!/usr/local/Cellar/python3/3.5.1/bin/python3.5

# 仮定として、ユーザ登録されているレビュワーのみを対象
# ユーザIDを入力することで、そのユーザにオススメの映画をレコメンドする
from extract_data import Extract_data
from user_base import User_base
from item_base import Item_base
from recommend import Recommend
import numpy as np
import pandas as pd
from operator import itemgetter
import argparse


class Main:
    def main():
        parser = argparse.ArgumentParser()
        subparsers = parser.add_subparsers()
        rec_parser = subparsers.add_parser('rec')
        rec_parser.add_argument('-i', '--item', nargs=1)
        rec_parser.add_argument('-u', '--user', nargs=1)
        rec_parser.set_defaults(func=Recommend.recommend)
        args = parser.parse_args()
        if hasattr(args, 'func'):
            args.func(args)
        else:
            parser.print_help()


if __name__ == "__main__":
    Main.main()
