import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from access_databasaes import access_categories, access_study_records, access_studying_users, access_users
from util import input_util

def main():
    name = input_util.input_any("削除するユーザー名を入力してください:")
    user_info = access_users.check_user_by_user_name(name)
    if user_info == None:
        print(f"[Error]: {name}は登録されていません")
        return
    user_id = user_info[0]['id']
    count = access_study_records.get_records_count(user_id)
    print(f"勉強記録の件数{count}")
    if input_util.input_boolean(f"ユーザー: {name}を削除していいですか?勉強記録も削除されます"):
        # ユーザーに関するすべての情報を削除
        access_studying_users.delete_studying_user(user_id)
        access_study_records.delete_records_user(user_id)
        access_categories.delete_categoires_user(user_id)
        access_users.delete_user(name)
        print("ユーザーの削除が完了しました")
    else:
        print("キャンセルしました")

if __name__ == '__main__':
    main()