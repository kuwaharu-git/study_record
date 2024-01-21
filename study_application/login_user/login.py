import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from access_databasaes import access_studying_users, access_users
from util import input_util
from login_user.category_manegement import category_manegement_menu
from login_user.output import create_html
from login_user.study_record import start_study, finish_study
from login_user import update_affiliaton
from util.db_util import check_error
@check_error
def select_menu():
    user_name = input_util.input_any("ユーザー名を入力してください: ")
    user_info = access_users.check_user_by_user_name(user_name)
    if not user_info == None:
        user_id = user_info[0]["id"]
    else:
        print(f"{user_name}は登録されていません")
    while True:
        print("*** ユーザーメニュー")
        if access_studying_users.check_studying_user(user_id):
            print("1: 勉強の終了(現在勉強中です)")
            menu_type = 1
        else:
            print("1: 勉強の開始")
            menu_type = 2
        print("2: カテゴリ管理")
        print("3: 記録の出力")
        print("4: 所属の変更")
        print("5: ログアウト")
        num = input_util.input_int("メニューを選択してください:")
        if num == 1 and menu_type == 1:
            finish_study.main(user_id)
        elif num == 1 and menu_type == 2:
            start_study.main(user_id)
        elif num == 2:
            category_manegement_menu.category_select_menu(user_id)
        elif num == 3:
            create_html.main(user_id)
        elif num == 4:
            update_affiliaton.main(user_id)
        elif num == 5:
            print("ログアウトしました")
            break
        else:
            print("1~5の数字を入力してください")

if __name__ == '__main__':
    select_menu()