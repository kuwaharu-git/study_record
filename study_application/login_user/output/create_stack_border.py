import os
import sys
from matplotlib import pyplot as plt
import japanize_matplotlib
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from util import get_last_date
from access_databasaes import access_study_records


# 積み上げ縦棒グラフを作成する関数
def main(user_id, year_month):
    last_date = get_last_date.last_date(year_month.year, year_month.month)
    rows = access_study_records.get_records(user_id, year_month.date(), year_month.date().replace(day=last_date))
    if rows is None:
        return 'not_data'
    category_name_list = access_study_records.get_category_name_list(user_id, year_month.date(), year_month.date().replace(day=last_date))
    x_date = [str(i) for i in range(1, last_date + 1)]
    bar_records = dict()   # カテゴリーIDごとに日付ごとの勉強時間のリストを持つディクショナリ
    for category in category_name_list:
        bar_records[category['category_name']] = [0] * last_date
    for row in rows:
        time = row['study_time']   # timedelta型
        minute = time.seconds // 60
        category_name = row['category_name']
        date = row['study_date'].day
        bar_records[category_name][date - 1] += minute
    plt.bar(x_date, bar_records[category_name_list[0]['category_name']], label = category_name_list[0]['category_name'])
    for i in range(1, len(category_name_list)):
        plt.bar(x_date, bar_records[category_name_list[i]['category_name']], bottom=bar_records[category_name_list[i - 1]['category_name']], label = category_name_list[i]['category_name'])
    plt.xticks([i for i in range(0, last_date + 2, 2)])
    plt.xlabel("日")
    plt.ylabel("分")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, fontsize=18)
    plt.savefig(f"{os.path.dirname(__file__)}/{user_id}_stacked_bar_graph.png", bbox_inches='tight')
    plt.clf()
