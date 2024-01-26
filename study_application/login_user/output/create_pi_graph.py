import os
import sys
from matplotlib import pyplot as plt
import japanize_matplotlib
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from util import get_last_date
from access_databasaes import access_study_records

# 円グラフを作成する関数
def main(user_id, year_month):
    last_date = get_last_date.last_date(year_month.year, year_month.month)
    rows = access_study_records.get_records(user_id, year_month.date(), year_month.date().replace(day=last_date))
    if rows is None:
        return 'not_data'
    pie_records = dict()   # カテゴリーIDごとに日付ごとの勉強時間のリストを持つディクショナリ
    category_name_list = access_study_records.get_category_name_list(user_id, year_month.date(), year_month.date().replace(day=last_date))
    for category in category_name_list:
        pie_records[category['category_name']] = 0
    for row in rows:
        time = row['study_time']   # timedelta型
        minute = time.seconds // 60
        category_name = row['category_name']
        pie_records[category_name] += minute
    x = list(pie_records.keys())
    y = list(pie_records.values())
    for i in range(len(x)):
        hour = 0
        minute = 0
        hour += y[i] // 60
        minute += y[i] % 60
        x[i] = f"{x[i]}: {hour}時間{minute}分"

    plt.pie(y, labels=x, autopct="%1.1f%%", counterclock=False, startangle=90)
    plt.legend(bbox_to_anchor=(1.4, 0.8), loc='upper left', borderaxespad=0, fontsize=18)
    plt.savefig(f"{os.path.dirname(__file__)}/{user_id}_pie_chart.png", bbox_inches='tight')
    plt.clf()