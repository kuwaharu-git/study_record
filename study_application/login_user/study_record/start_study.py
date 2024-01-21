import os
import sys
import datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from util import input_util
from access_databasaes import access_users, access_categories, access_studying_users
from util.db_util import check_error
@check_error
def main(user_id):
    if access_users.check_user_by_id(user_id) == None:
        print(f"[Error]: {user_id}は登録されていません。一度ログアウトしてログインしなおしてください") 
        return
    if access_studying_users.check_studying_user(user_id):
        print(f"[Error]: すでに勉強中なため開始できません。")
        return 
    now = datetime.datetime.now()
    print("1  :その他")
    category_list = [1]
    rows = access_categories.get_categories(user_id)
    while True:
        if rows:
            for row in rows:
                print(f"{row['id']:<3}:{row['category_name']}")
                category_list.append(row['id'])
        category_id = input_util.input_int("勉強するカテゴリーのカテゴリーIDを入力してください")
        if category_id in category_list:
            access_studying_users.insert_studying_user(user_id, category_id, now)
            print("勉強の開始記録が完了しました。勉強が終わった後忘れずに終了の記録をつけてください")
            break
        else:
            print("表示されているあなたのカテゴリーのカテゴリーIDを入力してください")
    
if __name__ == '__main__':
    user_id = input_util.input_int('user_idの入力')
    main(user_id)