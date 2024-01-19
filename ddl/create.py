import datetime
from datetime import timedelta, datetime
from random import randint
user_id = 2
category_ids = [9, 6, 7, 5, 4, 2, 1]
for _ in range(40):
    category_id = category_ids[randint(0, len(category_ids) - 1)]
    study_date = datetime(2024, 1, 1) + timedelta(days=randint(1, 30))
    study_time = timedelta(hours=randint(0, 4), minutes=randint(0, 59))

    # SQL文を出力
    sql = f"INSERT INTO study_records (user_id, category_id, study_date, study_time) VALUES ({user_id}, {category_id}, '{study_date}', '{study_time}');"
    print(sql)