import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from access_databasaes import access_categories, access_study_records, access_studying_users, access_users
from util import input_util
from menu import login, user_management

def category_select_menu(user_id):
    while True:
        print("*** カテゴリ管理 ***")
        print("1: カテゴリの追加")
        print("2: カテゴリの削除")
        print("3: 終了(ユーザーメニューに戻る)")
        num = input_util.input_int("メニューを選択してください:")
        if num == 1:
            access_categories.create_category(user_id)
        elif num == 2:
            access_categories.delete_category(user_id)
        elif num == 3:
            break
        else:
            print("1~3の数字を入力してください")
