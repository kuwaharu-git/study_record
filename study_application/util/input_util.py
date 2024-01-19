import datetime


# キーボードの入力内容を整数で返す
def input_int(prompt):
    while True:
        str = input(prompt)   # キーボードからIDを入力
        if not str.isdigit():                      # 入力された値が整数かどうか判定
            print("エラー！！整数で入力してください")
            continue
        break
    return int(str)

# キーボードの入力内容を少数で返す
def input_float(prompt):
    while True:
        str = input(prompt)   # キーボードからIDを入力
        if not str.isdigit():                      # 入力された値が整数かどうか判定
            print("エラー！！数字で入力してください")
            continue
        break
    return float(str)




# キーボードの入力内容が日付型であることの確認
def input_date(prompt):
    while True:
        str = input(prompt)
        try:
            datetime.datetime.strptime(str, '%Y-%m-%d')
        except ValueError:
            print("エラー!!日付で入力してください")
            continue
        break
    return str

def input_year_month(prompt):
    while True:
        str = input(prompt)
        try:
            year_month = datetime.datetime.strptime(str, '%Y-%m')
        except ValueError:
            print("エラー!!日付で入力してください")
            continue
        break
    return year_month

# キーボドの入力内容が何もないかの確認
def input_any(prompt):
    while True:
        str = input(prompt)
        if str == "":
            print("何か入力してください")
            continue
        else:
            break
    return str.strip()

# not nullではないため何もない場合はNoneを返す
def input_any_null(prompt):
    while True:
        str = input(prompt)
        if str == "":
            return None
        else:
            break
    return str.strip()


def input_boolean(prompt):
    while True:
        str = input(f'{prompt} y/n')
        if str.lower() == 'y':
            return True
        elif str.lower() == 'n':
            return False
        else:
            print("yかnを入力してください")
            continue
