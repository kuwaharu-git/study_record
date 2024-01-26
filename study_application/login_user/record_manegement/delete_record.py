import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from util import input_util, get_last_date
from util.db_util import check_error
from access_databasaes import access_study_records


@check_error
def main(user_id):
    print("--- 記録の削除 ---")
    print("※記録のIDは記録の表示から確認できます")
    record_id = input_util.input_int("削除する記録のIDを入力してください")
    if record_id == 'cancel':
        print('キャンセルしました')
        return
    rows = access_study_records.get_record_by_id(record_id)
    if rows is None:
        print(f"IDが{record_id}の記録はありませんでした")
        return
    if rows[0]['user_id'] != user_id:
        print(f"ID:{record_id}の記録はあなたの記録ではないため削除できません")
        return
    print(f"カテゴリー名:{rows[0]['category_name']}")
    print(f"勉強日付:{rows[0]['study_date']}")
    print(f"勉強時間:{rows[0]['study_time']}")
    if input_util.input_boolean("本当に削除してよろしいですか"):
        access_study_records.delete_record_by_id(record_id)
        print("削除が完了しました")
    else:
        print('キャンセルしました')
