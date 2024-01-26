import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from util import input_util, get_last_date
from util.db_util import check_error
from access_databasaes import access_study_records
from login_user.record_manegement import create_record, delete_record, show_record


@check_error
def main(user_id):
    while True:
        print("--- 勉強記録管理メニュー ---")
        print("1: 記録の表示")
        print("2: 記録の作成")
        print("3: 記録の削除")
        print("4: 終了")
        num = input_util.input_int("メニューを選択してください")
        if num == 1:
            show_record.main(user_id)
        elif num == 2:
            create_record.main(user_id)
        elif num == 3:
            delete_record.main(user_id)
        elif num == 4 or 'cancel':
            return
        else:
            print("1~4の数字を入力してください")
