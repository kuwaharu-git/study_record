import datetime

# 月の最後の日にちを求める関数
def last_date(year, month):
    d = datetime.datetime(year, month, 1)
    after_one_month = d.replace(month=month + 1)
    last = after_one_month - datetime.timedelta(days=1)
    return last.day