import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from access_databasaes import access_categories, access_study_records, access_studying_users, access_users
from util import input_util
from menu import login, user_management

print("=== 勉強記録アプリ ===")
print()
while True:
    print("*** TOPメニュー ***")
    print("1: ログイン")
    print("2: ユーザー管理(新規ユーザーはこちらから登録)")
    print("3: 勉強中のユーザーを確認する")
    print("4: 終了")
    print()
    num = input_util.input_int("メニューを選択してください:")
    if num == 1:
        user_name = input_util.input_any("ユーザー名を入力してください: ")
        user_info = access_users.check_user_by_user_name_db(user_name)
        if user_info:
            user_id = user_info[0]["id"]
            login.select_menu(user_id)
        else:
            print(f"{user_name}は登録されていません")
            continue
    elif num == 2:
        user_management.select_menu()
    elif num == 3:
        access_studying_users.get_all_info()
    elif num == 4:
        break
    else:
        print("1~4で入力してください")
        continue