import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from util import input_util, get_last_date
from util.db_util import check_error
from access_databasaes import access_study_records


@check_error
def main(user_id):
    year_month = input_util.input_year_month("記録を表示する年、月を入力してください['%Y-%m']")
    if year_month == 'cancel':
        print("キャンセルしました")
        return
    last_date = get_last_date.last_date(year_month.year, year_month.month)
    rows = access_study_records.get_records(user_id, year_month.date(), year_month.date().replace(day=last_date))
    if rows is None:
        print("記録がありませんでした")
        return
    for row in rows:
        print(f"ID:{row['id']:<3} カテゴリ名:{row['category_name']:<10} 日付:{row['study_date']} 時間{row['study_time']}")