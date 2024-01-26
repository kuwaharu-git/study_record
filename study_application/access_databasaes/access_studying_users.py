import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util.db_util import database_connect


# 勉強中テーブルからuser_idで情報の取得
@database_connect
def check_studying_user(cnx, cursor, user_id):
    sql = 'select * from studying_users where user_id = %s'
    data = [user_id]
    cursor.execute(sql, data)
    rows = cursor.fetchall()
    if len(rows) != 0:
        return rows
    else:
        return None


# 勉強中テーブルから全userの情報の取得
@database_connect
def get_all_info(cnx, cursor):
    sql = 'select * from studying_users'
    cursor.execute(sql)
    rows = cursor.fetchall()
    if len(rows) != 0:
        return rows
    else:
        return None


# 勉強中のユーザーの追加
@database_connect
def insert_studying_user(cnx, cursor, user_id, category_id, now):
    sql = 'insert into studying_users (user_id, category_id, start_time) values (%s, %s, %s)'
    data = [user_id, category_id, now]
    cursor.execute(sql, data)
    cnx.commit()


# 勉強中userの削除
@database_connect
def delete_studying_user(cnx, cursor, user_id):
    sql = 'delete from studying_users where user_id = %s'
    data = [user_id]
    cursor.execute(sql, data)
    cnx.commit()


# 勉強中のユーザーの情報の取得
@database_connect
def get_studying_user_info(cnx, cursor, user_id):
    study_info = check_studying_user(user_id)
    if study_info:
        return study_info
    else:
        return None


if __name__ == '__main__':
    insert_studying_user(2)