import os
import sys
from matplotlib import pyplot as plt
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util import input_util, get_last_date
from util.db_util import database_connect
from access_databasaes import access_users, access_study_records, access_categories
import japanize_matplotlib
@database_connect
def output_stacked_bar_graph(cnx, cursor, user_id):
    year_month =  input_util.input_year_month("グラフを作成する年、月を入力してください['%Y-%m']")
    last_date = get_last_date.last_date(year_month.year, year_month.month)
    x_date = [str(i) for i in range(1, last_date + 1)]
    rows = access_study_records.get_records(cursor, user_id, year_month.date(), year_month.date().replace(day=last_date))
    if rows:
        records = dict() # カテゴリーIDごとに日付ごとの勉強時間のリストを持つディクショナリ
        category_id_list = access_study_records.get_category_id_list(cursor, user_id, year_month.date(), year_month.date().replace(day=last_date))
        for category in category_id_list:
            records[str(category['category_id'])] = [0] * last_date
        for row in rows:
            time = row['study_time']   # timedelta型
            minute = time.seconds // 60
            category_id = str(row['category_id'])
            date = row['study_date'].day
            records[category_id][date - 1] += minute
        category_name = access_categories.get_category(cursor, category_id_list[0]['category_id'])
        if category_name:
            category_name = category_name[0]['category_name']
        else:
            category_name = f"不明_{category_id_list[0]['category_id']}"
        plt.bar(x_date, records[str(category_id_list[0]['category_id'])], label = category_name)
        for i in range(1, len(category_id_list)):
            category_name = access_categories.get_category(cursor, category_id_list[i]['category_id'])
            if category_name:
                category_name = category_name[0]['category_name']
            else:
                category_name = f"不明_{category_id_list[i]['category_id']}"
            plt.bar(x_date, records[str(category_id_list[i]['category_id'])], bottom=records[str(category_id_list[i - 1]['category_id'])], label = category_name)
        plt.xticks([i for i in range(0, last_date + 2, 2)])
        plt.legend()            
        plt.savefig(f"{os.path.dirname(__file__)}/{user_id}_stacked_bar_graph.png")
        with open(f"{os.path.dirname(os.path.abspath(__file__))}\{user_id}_stacked_bar_graph.html", mode='w', encoding= 'utf-8', newline='\n') as f:
            f.write('<html>\n')
            f.write('<head>\n')
            f.write('<title>勉強記録</title>\n')
            f.write('</head>\n')
            f.write('<body>\n')
            f.write(f'<h1>{year_month.strftime("%Y年%m月")}の勉強記録\n')
            f.write('</body>\n')
            f.write(f'<img src="{os.path.dirname(__file__)}/{user_id}_stacked_bar_graph.png">\n')
            f.write('</body>\n')
            f.write('</html>\n')
    else:
        print("記録がありませんでした")

if __name__ == '__main__':
    output_stacked_bar_graph(2)
