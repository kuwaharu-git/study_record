import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from access_databasaes import access_categories, access_study_records, access_studying_users, access_users
from util import input_util

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
        pass
    elif num == 2:
        pass 
    elif num == 3:
        access_studying_users.get_all_info()
    elif num == 4:
        break
    else:
        print("1~4で入力してください")
        continue