import os
import sys
from matplotlib import pyplot as plt
import japanize_matplotlib
import webbrowser
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from util import input_util, get_last_date
from util.db_util import check_error
from login_user.output import create_pi_graph, create_stack_border
from access_databasaes import access_study_records


@check_error
def main(user_id):
    year_month = input_util.input_year_month("グラフを作成する年、月を入力してください['%Y-%m']")
    if year_month == 'cancel':
        print("キャンセルしました")
        return
    # 積み上げ棒グラフの作成
    result_1 = create_stack_border.main(user_id, year_month)
    if result_1 == 'not_data':
        print('記録がありませんでした')
        return
    # 円グラフの作成
    result_2 = create_pi_graph.main(user_id, year_month)
    if result_2 == 'not_data':
        print('記録がありませんでした')
        return
    last_date = get_last_date.last_date(year_month.year, year_month.month)
    rows = access_study_records.get_records(user_id, year_month.date(), year_month.date().replace(day=last_date))
    # HTMLの作成
    with open(f"{os.path.dirname(os.path.abspath(__file__))}\{user_id}_output.html", mode='w', encoding= 'utf-8', newline='\n') as f:
        f.write('<html>\n')
        f.write('<head>\n')
        f.write('<title>勉強記録</title>\n')
        f.write('<link rel="stylesheet" href="style.css">')
        f.write('</head>\n')
        f.write('<body>\n')
        f.write(f'<h1>{year_month.strftime("%Y年%m月")}の勉強記録</h1>\n')
        f.write('</body>\n')
        f.write(f'<img src="{os.path.dirname(__file__)}/{user_id}_stacked_bar_graph.png">\n')
        f.write(f'<img src="{os.path.dirname(__file__)}/{user_id}_pie_chart.png">\n')
        # tableの作成
        f.write('<table border=1>\n')
        f.write('<tr>\n')
        f.write('<th>ID</th><th>カテゴリー</th><th>勉強日付</th><th>勉強時間</th>\n')
        f.write('</tr>\n')
        for row in rows:
            f.write('<tr>\n')
            f.write(f'<td>{row["id"]}</td><td>{row["category_name"]}</td><td>{row["study_date"]}</td><td>{row["study_time"]}</td>\n')
            f.write('</tr>\n')
        f.write('</table>\n')
        f.write('</body>\n')
        f.write('</html>\n')
    webbrowser.open(f"{os.path.dirname(os.path.abspath(__file__))}\{user_id}_output.html", 2, autoraise=True)


if __name__ == '__main__':
    main(2)

