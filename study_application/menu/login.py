import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from access_databasaes import access_categories, access_study_records, access_studying_users, access_users
from util import input_util
from menu import category_manegement

def select_menu(user_id):
    while True:
        print("*** ユーザーメニュー")
        if access_studying_users.check_studying_user_db(user_id):
            print("1: 勉強の終了(現在勉強中です)")
            type = 1
        else:
            print("1: 勉強の開始")
            type = 2
        print("2: カテゴリ管理")
        print("3: 記録の出力")
        print("4: 所属の変更")
        print("5: ログアウト")
        num = input_util.input_int("メニューを選択してください:")
        if num == 1 and type == 1:
            access_study_records.create_study_record(user_id)
        elif num == 1 and type == 2:
            access_studying_users.insert_studying_user(user_id)
        elif num == 2:
            category_manegement.category_select_menu(user_id)
        elif num == 3:
            pass
        elif num == 4:
            access_users.update_user_affiliaton(user_id)
        elif num == 5:
            print("ログアウトしました")
            break
        else:
            print("1~5の数字を入力してください")
            
