import datetime
from datetime import timedelta, datetime
from random import randint
user_id = 2
category_names = ["Python", "web", "MySQL", "English", "Java", "IoT"]
for _ in range(40):
    category_name = category_names[randint(0, len(category_names) - 1)]
    study_date = datetime(2024, 1, 1) + timedelta(days=randint(1, 30))
    study_time = timedelta(hours=randint(0, 4), minutes=randint(0, 59))

    # SQL文を出力
    sql = f"INSERT INTO study_records (user_id, category_name, study_date, study_time) VALUES ({user_id}, '{category_name}', '{study_date}', '{study_time}');"
    print(sql)

# 2  :Python
# 4  :web
# 6  :MySQL
# 7  :English
# 8  :Java
# 9  :IoT