import os
import sys
import datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from util import input_util
from access_databasaes import access_study_records, access_users, access_categories, access_studying_users
from util.db_util import check_error


@check_error
def main(user_id):
    if access_users.check_user_by_id == None:
        print(f"[Error]: {user_id}は登録されていません。一度ログアウトしてログインしなおしてください") 
        return
    study_info = access_studying_users.check_studying_user(user_id)
    if study_info is None:
        print(f"[Error]: 現在ID{user_id}は勉強中ではありません")
        return 
    category_id = study_info[0]['category_id']
    category_name = access_categories.get_category(category_id)
    if category_name:
        category_name = category_name[0]['category_name']
    else:
        # 学習中にカテゴリが消されてた場合はその他に書き換え
        category_id = 1
        category_name = 'その他'
    study_date = study_info[0]['start_time'].date()
    # datetime.timedeltaから合計秒数を求めそこから時間と分を取得
    difference = int((datetime.datetime.now() - study_info[0]['start_time']).total_seconds())
    MinutesGet, SecondsGet = divmod(difference, 60)   # 分, 秒
    HoursGet, MinutesGet = divmod(MinutesGet, 60)   # 時間, 分
    study_time = f"{HoursGet}:{MinutesGet}:00"   # 秒は切り捨て
    if HoursGet >= 24:
        print("24時間を超える記録は作成できません。勉強中の記録も削除します")
        access_studying_users.delete_studying_user(user_id)
        return
    print(f"カテゴリリー名: {category_name}")
    print(f"勉強年月日: {study_date}")
    print(f"勉強時間: {HoursGet}時間{MinutesGet}分")
    if input_util.input_boolean("記録しますか?"):
        access_study_records.create_record(user_id, category_name, study_date, study_time)
        access_studying_users.delete_studying_user(user_id)
        print("勉強の記録が完了しました")
    else:
        print("キャンセルしました")
        if input_util.input_boolean("引き続き同じ勉強をしますか?しない場合現在の勉強中の記録を削除します"):
            print("引き続き勉強を頑張ってください")
        else:
            access_studying_users.delete_studying_user(user_id)
            print("勉強中の記録を削除しました")


if __name__ == '__main__':
    user_id = input_util.input_int('user_idの入力')
    main(user_id)