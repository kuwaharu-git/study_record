import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util.db_util import database_connect


# user_idからカテゴリーが存在するか確認する関数
@database_connect
def check_category(cnx, cursor, user_id, category_name):
    sql = 'select * from categories where user_id = %s and category_name = %s'
    data = [user_id, category_name]
    cursor.execute(sql, data)
    rows = cursor.fetchall()
    if len(rows) != 0:
        return rows
    else:
        return False


# category_idからカテゴリー情報を取得
@database_connect
def get_category(cnx, cursor, category_id):
    sql = 'select * from categories where id = %s'
    data = [category_id]
    cursor.execute(sql, data)
    rows = cursor.fetchall()
    if len(rows) != 0:
        return rows
    else:
        return None


# user_idからすべてのカテゴリーを取得
@database_connect
def get_categories(cnx, cursor, user_id):
    sql = 'select * from categories where user_id = %s order by id'
    data = [user_id]
    cursor.execute(sql, data)
    rows = cursor.fetchall()
    if len(rows) != 0:
        return rows
    else:
        return None


# カテゴリを追加する関数
@database_connect
def create_category(cnx, cursor, user_id, category_name):
    sql = 'insert into categories (user_id, category_name) values (%s, %s)'
    data = [user_id, category_name]
    cursor.execute(sql, data)
    cnx.commit()
    return True


# カテゴリを削除する関数
@database_connect
def delete_category(cnx, cursor, category_id):
    sql = 'delete from categories where id = %s'
    data = [category_id]
    cursor.execute(sql, data)
    cnx.commit()
    return True


# user_idからカテゴリをすべて削除をする関数
@database_connect
def delete_categoires_user(cnx, cursor, user_id):
    sql = 'delete from categories where user_id = %s'
    data = [user_id]
    cursor.execute(sql, data)
    cnx.commit()