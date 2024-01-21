import os
import sys
from matplotlib import pyplot as plt
import japanize_matplotlib
import webbrowser
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from util import input_util, get_last_date
from util.db_util import check_error
from access_databasaes import access_study_records


@check_error
def main(user_id):
    year_month =  input_util.input_year_month("グラフを作成する年、月を入力してください['%Y-%m']")
    last_date = get_last_date.last_date(year_month.year, year_month.month)
    rows = access_study_records.get_records(user_id, year_month.date(), year_month.date().replace(day=last_date))
    if rows == None:
        print("記録がありませんでした")
        return
    category_name_list = access_study_records.get_category_name_list(user_id, year_month.date(), year_month.date().replace(day=last_date))

    # 積み上げ棒グラフの作成
    x_date = [str(i) for i in range(1, last_date + 1)]
    bar_records = dict() # カテゴリーIDごとに日付ごとの勉強時間のリストを持つディクショナリ
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
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, fontsize=18)
    plt.savefig(f"{os.path.dirname(__file__)}/{user_id}_stacked_bar_graph.png", bbox_inches='tight')
    plt.clf()
    # 円グラフの作成
    pie_records = dict() # カテゴリーIDごとに日付ごとの勉強時間のリストを持つディクショナリ
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

    with open(f"{os.path.dirname(os.path.abspath(__file__))}\{user_id}_stacked_bar_graph.html", mode='w', encoding= 'utf-8', newline='\n') as f:
        f.write('<html>\n')
        f.write('<head>\n')
        f.write('<title>勉強記録</title>\n')
        f.write('</head>\n')
        f.write('<body>\n')
        f.write(f'<h1>{year_month.strftime("%Y年%m月")}の勉強記録</h1>\n')
        f.write('</body>\n')
        f.write(f'<img src="{os.path.dirname(__file__)}/{user_id}_stacked_bar_graph.png">\n')
        f.write(f'<img src="{os.path.dirname(__file__)}/{user_id}_pie_chart.png">\n')
        f.write('</body>\n')
        f.write('</html>\n')
    webbrowser.open(f"{os.path.dirname(os.path.abspath(__file__))}\{user_id}_stacked_bar_graph.html", 2, autoraise=True)

if __name__ == '__main__':
    main(2)
