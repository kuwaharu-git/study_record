import datetime
# inputの際に使うモジュール
# cancelと入力されたらcancelを返す


# キーボードの入力内容を整数で返す
def input_int(prompt):
    while True:
        str = input(prompt)   # キーボードからIDを入力
        if str == 'cancel':
            return 'cancel'
        if not str.isdigit():                      # 入力された値が整数かどうか判定
            print("エラー！！整数で入力してください")
            continue
        break
    return int(str)


# キーボードの入力内容を少数で返す
def input_float(prompt):
    while True:
        str = input(prompt)   # キーボードからIDを入力
        if str == 'cancel':
            return 'cancel'
        if not str.isdigit():                      # 入力された値が整数かどうか判定
            print("エラー！！数字で入力してください")
            continue
        break
    return float(str)


# キーボードの入力内容が日付型であることの確認
def input_date(prompt):
    while True:
        str = input(prompt)
        if str == 'cancel':
            return 'cancel'
        try:
            datetime.datetime.strptime(str, '%Y-%m-%d')
        except ValueError:
            print("[Error]: 指定されたフォーマットで入力してください")
            continue
        break
    return str


# キーボードの入力内容が年、月か確認
def input_year_month(prompt):
    while True:
        str = input(prompt)
        if str == 'cancel':
            return 'cancel'
        try:
            year_month = datetime.datetime.strptime(str, '%Y-%m')
        except ValueError:
            print("[Error]: 指定されたフォーマットで入力してください")
            continue
        break
    return year_month


# キーボードの入力内容が時、分であることを確認
def input_hour_minute(prompt):
    while True:
        str = input(prompt)
        if str == 'cancel':
            return 'cancel'
        try:
            hour_minute = datetime.datetime.strptime(str, '%I:%M')
        except ValueError:
            print("[Error]: 指定されたフォーマットで入力してください")
            continue
        break
    return hour_minute


# キーボドの入力内容が何もないかの確認
def input_any(prompt):
    while True:
        str = input(prompt)
        if str == 'cancel':
            return 'cancel'
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
        if str == 'cancel':
            return 'cancel'
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
