import os
import sys
from matplotlib import pyplot as plt
import japanize_matplotlib
import webbrowser
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from util import input_util
from util.db_util import check_error
from login_user.output import create_pi_graph, create_stack_border


@check_error
def main(user_id):
    year_month = input_util.input_year_month("グラフを作成する年、月を入力してください['%Y-%m']")
    if year_month == 'cancel':
        print("キャンセルしました")
        return
    result_1 = create_stack_border.main(user_id, year_month)
    if result_1 == 'not_data':
        print('記録がありませんでした')
        return
    result_2 = create_pi_graph.main(user_id, year_month)
    if result_2 == 'not_data':
        print('記録がありませんでした')
        return
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

