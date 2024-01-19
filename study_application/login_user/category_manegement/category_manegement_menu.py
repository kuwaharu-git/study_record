import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from access_databasaes import access_categories, access_study_records, access_studying_users, access_users
from util import input_util
from login_user.category_manegement import create_category, delete_category
from util.db_util import check_error

@check_error
def category_select_menu(user_id):
    while True:
        print("*** カテゴリ管理 ***")
        print("--- カテゴリ一覧 ---")
        rows = access_categories.get_categories(user_id)
        for row in rows:
                print(f"{row['id']:<3}:{row['category_name']}")
        print("--- メニュー ---")
        print("1: カテゴリの追加")
        print("2: カテゴリの削除")
        print("3: 終了(ユーザーメニューに戻る)")
        num = input_util.input_int("メニューを選択してください:")
        if num == 1:
             create_category.main(user_id)
        elif num == 2:
            delete_category.main(user_id)
        elif num == 3:
            break
        else:
            print("1~3の数字を入力してください")

if __name__ == '__main__':
     category_select_menu(2)