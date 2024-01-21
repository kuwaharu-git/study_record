import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util import input_util
from user_manegement import create_user, delete_user
from util.db_util import check_error

@check_error
def select_menu():
    while True:
        print("*** ユーザー管理 *** ")
        print("1: ユーザー登録")
        print("2: ユーザー削除")
        num = input_util.input_int("メニューを選択してください:")
        if num == 1:
            create_user.main()
            break
        elif num == 2:
            delete_user.main()
            break
        else:
            print("1~2の数字を入力してください")

if __name__ == '__main__':
    select_menu()