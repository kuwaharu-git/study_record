import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util import input_util
from output import stacked_bar_graph
def output_select(user_id):
    while True:
        print("*** 記録出力 ***")
        print("1: 積み立て棒グラフ")
        print("2: 円グラフ")
        print("3: 終了")
        num = input_util.input_int("メニューを選択してください:")
        if num == 1:
            stacked_bar_graph.output_stacked_bar_graph(user_id)
        elif num == 2:
            pass
        elif num == 3:
            break
        else:
            print("1~3の数字を入力してください")

    