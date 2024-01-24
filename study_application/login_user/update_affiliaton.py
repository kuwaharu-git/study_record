import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util import input_util
from util.db_util import check_error
from access_databasaes import access_users

@check_error
def main(user_id):
    user_info = access_users.check_user_by_id(user_id)
    if user_info == None:
        print(f"[Error]: {user_id}は登録されていません")
        return 
    print(f"現在の所属: {user_info[0]['affiliaton']}")
    affiliaton = input_util.input_any_null(f"所属を入力してください。所属を無しにする場合は何も入力せずにEnterを押してください:")
    if affiliaton == 'cancel':
        print("キャンセルしました")
        return
    access_users.update_user_affiliaton(user_id, affiliaton)
    print("ユーザーの所属の更新が完了しました")
