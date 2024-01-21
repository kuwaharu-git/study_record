import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from util import input_util
from access_databasaes import access_users, access_categories
from util.db_util import check_error

@check_error
def main(user_id):
    user_info = access_users.check_user_by_id(user_id)
    if user_info == None:
        print("[Error]: ログイン中のユーザーが削除されました")
        return
    print("--- カテゴリー追加 ---")
    category_name = input_util.input_any(f"カテゴリー名を入力してください")
    if access_categories.check_category(user_id, category_name):
        print(f"[Error]: {category_name}はすでに登録済みです")
        return 
    access_categories.create_category(user_id, category_name)
    print("カテゴリの追加が完了しました")

if __name__ == '__main__':
    main(2)
