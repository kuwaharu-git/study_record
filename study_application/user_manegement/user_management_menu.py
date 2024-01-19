import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from access_databasaes import access_categories, access_study_records, access_studying_users, access_users
from util import input_util

def select_menu():
    while True:
        print("*** ユーザー管理 *** ")
        print("1: ユーザー登録")
        print("2: ユーザー削除")
        num = input_util.input_int("メニューを選択してください:")
        if num == 1:
            access_users.create_user()
            break
        elif num == 2:
            access_users.delete_user()
            break
        else:
            print("1~2の数字を入力してください")
