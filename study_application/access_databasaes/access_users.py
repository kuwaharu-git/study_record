import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util.db_util import database_connect


# ユーザーがusersに存在するかの確認(idから)
@database_connect
def check_user_by_id(cnx, cursor, id):
    sql = 'select * from users where id = %s'
    data = [id]
    cursor.execute(sql, data)
    rows = cursor.fetchall()
    if len(rows) != 0:
        return rows
    else:
        return None
    

# ユーザーがusersに存在するかの確認(user_nameから)
@database_connect
def check_user_by_user_name(cnx, cursor, name):
    sql = 'select * from users where user_name = %s'
    data = [name]
    cursor.execute(sql, data)
    rows = cursor.fetchall()
    if len(rows) != 0:
        return rows
    else:
        return None


# ユーザー登録
@database_connect
def create_user(cnx, cursor, user_name, affiliaton):
    sql = 'insert into users (user_name, affiliaton) values (%s, %s)'
    data = [user_name, affiliaton]
    cursor.execute(sql, data)
    cnx.commit()


# ユーザー削除
@database_connect
def delete_user(cnx, cursor, user_name):
    sql = 'delete from users where user_name = %s'
    data = [user_name]
    cursor.execute(sql, data)
    cnx.commit()


# 所属のアップデート
@database_connect
def update_user_affiliaton(cnx, cursor, user_id, affiliaton):
    sql = 'update users set affiliaton = %s where id = %s'
    data = [affiliaton, user_id]
    cursor.execute(sql, data)
    cnx.commit()


if __name__ == "__main__":
    create_user()
