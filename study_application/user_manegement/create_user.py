import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from access_databasaes import access_users
from util import input_util
from util.db_util import check_error


@check_error
def main():
    user_name = input_util.input_any("登録するユーザー名を入力してください:")
    if user_name == 'cancel':
        print("キャンセルしました")
        return
    user_info = access_users.check_user_by_user_name(user_name)
    if user_info is not None:
        print(f"[Error]: {user_name}はすでに登録されているため登録できません")
        return 
    affiliaton = input_util.input_any_null("所属を入力してください。所属を設定しない場合は何も入力せずにEnterを押してください:")
    if affiliaton == 'cancel':
        print("キャンセルしました")
        return
    access_users.create_user(user_name, affiliaton)
    print("ユーザーの登録が完了しました")


if __name__ == '__main__':
    main()