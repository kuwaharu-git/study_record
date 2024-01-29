import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util.db_util import database_connect


# 勉強記録の件数を取得
@database_connect
def get_records_count(cnx, cursor, user_id):
    sql = 'select count(*) as count from study_records where user_id = %s'
    data = [user_id]
    cursor.execute(sql, data)
    rows = cursor.fetchall()
    if len(rows) != 0:
        count = rows[0]['count']
        return count
    else:
        return 0


# 勉強記録の追加
@database_connect
def create_record(cnx, cursor, user_id, category_name, study_date, study_time):
    sql = 'insert into study_records (user_id, category_name, study_date, study_time) values (%s, %s, %s, %s)'
    data = [user_id, category_name, study_date, study_time]
    cursor.execute(sql, data)
    cnx.commit()


# 勉強記録の削除(by_id)
@database_connect
def delete_record_by_id(cnx, cursor, record_id):
    sql = 'delete from study_records where id = %s'
    data = [record_id]
    cursor.execute(sql, data)
    cnx.commit()


# 勉強記録の削除(user削除)
@database_connect
def delete_records_user(cnx, cursor, user_id):
    sql = 'delete from study_records where user_id = %s'
    data = [user_id]
    cursor.execute(sql, data)
    cnx.commit()


# 勉強記録の取得(年月で絞り込み)
@database_connect
def get_records(cnx, cursor, user_id, first_date, last_date):
    sql = 'select * from study_records where user_id = %s and study_date between %s and %s order by study_date, id'
    data = [user_id, first_date, last_date]
    cursor.execute(sql, data)
    records_rows = cursor.fetchall()
    if len(records_rows) != 0:
        return records_rows
    else:
        return None


# category_nameのリストを取得(年月で絞り込み)
@database_connect   
def get_category_name_list(cnx, cursor, user_id, first_date, last_date):
    sql = 'select distinct(category_name) as category_name from study_records where user_id = %s and study_date between %s and %s'
    data = [user_id, first_date, last_date]
    cursor.execute(sql, data)
    rows = cursor.fetchall()
    return rows


@database_connect
def get_record_by_id(cnx, cursor, record_id):
    sql = 'select * from study_records where id = %s'
    data = [record_id]
    cursor.execute(sql, data)
    rows = cursor.fetchall()
    if len(rows) != 0:
        return rows
    else:
        return None