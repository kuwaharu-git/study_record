import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from util import input_util
from access_databasaes import access_users, access_categories, access_studying_users
from util.db_util import check_error

@check_error
def main(user_id):
    user_info = access_users.check_user_by_id(user_id)
    if user_info == None:
        print("[Error]: ログイン中のユーザーが削除されました")
        return
    rows = access_categories.get_categories(user_id)
    if rows == None:
        print("カテゴリを登録していません")
        return
    print("--- カテゴリー削除 ---") 
    for row in rows:
            print(f"{row['id']}: {row['category_name']}")
    category_id = input_util.input_int("削除するカテゴリーのIDを入力して下さい")
    category_info = access_categories.get_category(category_id)
    if category_info == None:
         print(f"[Erroe]: ID: {category_id}のカテゴリーは存在しません")
         return 
    if user_id != category_info[0]['user_id']:
         print(f"[Error]: カテゴリーのユーザーIDとあなたのIDが一致しないため削除できません")
         return
    studying_user_info =  access_studying_users.check_studying_user(user_id)
    if studying_user_info:
         if studying_user_info[0]['category_id'] == category_id:
              print("現在学習中のカテゴリなため削除できません")
              return 
    if input_util.input_boolean(f"カテゴリー{category_info[0]['category_name']}を削除していいですか？"):
        access_categories.delete_category(category_id)
        print("カテゴリーの削除が完了しました")
    else:
        print("キャンセルしました")   

if __name__ == '__main__':
    main(2)  