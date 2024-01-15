import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util.db_util import database_connect
from util import input_util
from access_databasaes.access_users import check_user_by_id

# user_idからカテゴリーが存在するか確認する関数
def check_category(cursor, user_id, category_name):
    sql = 'select * from categories where user_id = %s and category_name = %s'
    data = [user_id, category_name]
    cursor.execute(sql, data)
    rows = cursor.fetchall()
    if len(rows) != 0:
        return rows
    else:
        return False

# category_idからカテゴリー情報を取得
def get_category(cursor, category_id):
    sql = 'select * from categories where id = %s'
    data = [category_id]
    cursor.execute(sql, data)
    rows = cursor.fetchall()
    if len(rows) != 0:
        return rows
    else:
        return False

# user_diからすべてのカテゴリーを取得
def get_categories(cursor, user_id):
    sql = 'select * from categories where user_id = %s'
    data = [user_id]
    cursor.execute(sql, data)
    rows = cursor.fetchall()
    if len(rows) != 0:
        return rows
    else:
        return False

# カテゴリの追加
@database_connect
def create_category(cnx, cursor, user_id):
    user_info = check_user_by_id(cursor, user_id)   # ログイン中に他のユーザーによって削除される可能性を考慮
    if user_info:
        category_name = input_util.input_any(f"カテゴリー名を入力してください")
        category_info = check_category(cursor, user_id, category_name)
        if not category_info:
            sql = 'insert into categories (user_id, category_name) values (%s, %s)'
            data = [user_id, category_name]
            cursor.execute(sql, data)
            cnx.commit()
            print("カテゴリーの追加が完了しました")
        else:
            print(f"[Error]: {category_name}はすでに登録済みです")
    else:
        print(f"[Error]: {user_id}は登録されていません。一度ログアウトしてログインしなおしてください")    

# カテゴリの削除
@database_connect
def delete_category(cunx, cursor, user_id):
    category_id = input_util.input_int("削除するカテゴリーのIDを入力して下さい")
    category_info = get_category(cursor, category_id)
    if category_info:                                     
        if user_id == category_info[0]['user_id']:       
            if input_util.input_boolean(f"カテゴリー{category_info[0]['category_name']}を削除していいですか？"):
                sql = 'delete from categories where category_id = %s'
                data = [category_id]
                cursor.execute(sql, data)
                cunx.commit()
                print("カテゴリーの削除が完了しました")
            else:
                print("キャンセルしました")
        else:
            print(f"[Error]: カテゴリーのユーザーIDとあなたのIDが一致しないため削除できません")
    else:
        print(f"[Erroe]: ID: {category_id}のカテゴリーは存在しません。一度ログアウトしてログインしなおしてください")

if __name__ == '__main__':
    create_category(3)