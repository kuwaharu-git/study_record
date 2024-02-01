import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from util import input_util, get_last_date
from util.db_util import check_error
from access_databasaes import access_study_records, access_categories


@check_error
def main(user_id):
    print("--- 勉強記録の追加 ---")
    print("--- カテゴリ一覧 ---")
    rows = access_categories.get_categories(user_id)
    print("1  :その他")
    category_list = [1]
    while True:
        if rows:
            for row in rows:
                print(f"{row['id']:<3}:{row['category_name']}")
                category_list.append(row['id'])
        category_id = input_util.input_int("記録する勉強のカテゴリーのカテゴリーIDを入力してください:")
        if category_id == 'cancel':
            print("キャンセルしました")
            return
        if category_id in category_list:
            category_name = access_categories.get_category(category_id)[0]['category_name']
            break
        else:
            print("表示されているあなたのカテゴリーのカテゴリーIDを入力してください")    
    study_date = input_util.input_date("勉強した日付を入力してください[%Y-%m-%d]:")
    if study_date == 'cancel':
        print("キャンセルしました")
        return
    while True:
        study_time_hour = input_util.input_int("勉強時間を入力してください[hour]")
        if study_time_hour == 'cancel':
            print("キャンセルしました")
            return
        # 24以上の数字を入れるとdayに入ってしまうため制限
        if study_time_hour >= 24:
            print("24未満の数字を入力してください")
        elif study_time_hour < 24:
            break
    while True:
        study_time_minute = input_util.input_int("勉強時間を入力してください[minute]")
        if study_time_minute == 'cancel':
            print("キャンセルしました")
            return
        if study_time_minute >= 60:
            print("60未満の数字を入力してください")
        elif study_time_minute < 60:
            break
    access_study_records.create_record(user_id, category_name, study_date, f'{study_time_hour}:{study_time_minute}')
    print("記録の追加が完了しました")