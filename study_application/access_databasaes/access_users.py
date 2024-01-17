import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util.db_util import database_connect
from util import input_util
from access_databasaes import access_study_records, access_categories, access_studying_users

# ユーザーがusersに存在するかの確認(idから)
def check_user_by_id(cursor, id):
    sql = 'select * from users where id = %s'
    data = [id]
    cursor.execute(sql, data)
    rows = cursor.fetchall()
    if len(rows) != 0:
        return rows   # ユーザーが存在したらrowsを返す
    else:
        return False  # ユーザーが存在しなかったらFalseを返す
    
# ユーザーがusersに存在するかの確認(user_nameから)
def check_user_by_user_name(cursor, name):
    sql = 'select * from users where user_name = %s'
    data = [name]
    cursor.execute(sql, data)
    rows = cursor.fetchall()
    if len(rows) != 0:
        return rows   # ユーザーが存在したらrowsを返す
    else:
        return False  # ユーザーが存在しなかったらFalseを返す
    
@database_connect    
def check_user_by_user_name_db(cnx, cursor, name):
    sql = 'select * from users where user_name = %s'
    data = [name]
    cursor.execute(sql, data)
    rows = cursor.fetchall()
    if len(rows) != 0:
        return rows   # ユーザーが存在したらrowsを返す
    else:
        return False  # ユーザーが存在しなかったらFalseを返す
    
# ユーザーの登録
@database_connect
def create_user(cnx, cursor):
    name = input_util.input_any("登録するユーザー名を入力してください:")
    user_info = check_user_by_user_name(cursor, name)
    if not user_info:
        affiliaton = input_util.input_any_null(f"所属を入力してください。所属を設定しない場合は何も入力せずにEnterを押してください:")
        sql = 'insert into users (user_name, affiliaton) values (%s, %s)'
        data = [name, affiliaton]
        cursor.execute(sql, data)
        cnx.commit()
        print("ユーザーの登録が完了しました")
    else:
        print(f"[Error]: {name}はすでに登録されているため登録できません")

# ユーザーの削除
@database_connect
def delete_user(cnx, cursor):
    name = input_util.input_any("削除するユーザー名を入力してください:")
    user_info = check_user_by_user_name(cursor, name)
    if user_info:
        user_id = user_info[0]['id']
        count = access_study_records.get_records_count(cursor, user_id)
        print(f"勉強記録の件数{count}")
        if input_util.input_boolean(f"ユーザー: {name}を削除していいですか?勉強記録も削除されます"):
            access_studying_users.delete_studying_user(cnx, cursor,user_id)
            access_study_records.delete_records_user(cnx, cursor,user_id)
            access_categories.delete_categoires_user(cnx, cursor,user_id)
            sql = 'delete from users where user_name = %s'
            data = [name]
            cursor.execute(sql, data)
            cnx.commit()
            print("ユーザーの削除が完了しました")
        else:
            print("キャンセルしました")
    else:
        print(f"[Error]: {name}は登録されていません")

# ユーザーの所属の更新
@database_connect
def update_user_affiliaton(cnx, cursor, user_id):
    user_info = check_user_by_id(cursor, user_id)
    if user_info:
        affiliaton = input_util.input_any_null(f"所属を入力してください。所属を無しにする場合は何も入力せずにEnterを押してください:")
        sql = 'update users set affiliaton = %s where user_name = %s'
        data = [affiliaton, user_id]
        cursor.execute(sql, data)
        cnx.commit()
        print("ユーザーの所属の更新が完了しました")
    else:
        print(f"[Error]: {user_id}は登録されていません")

        

if __name__ == "__main__":
    create_user()
