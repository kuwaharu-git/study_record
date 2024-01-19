import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util.db_util import database_connect
from util import input_util
from access_databasaes import access_users, access_studying_users

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

# カテゴリの削除
# @database_connect
# def delete_category(cunx, cursor, user_id):
#     rows = get_categories(cursor, user_id)
#     if rows:
#         for row in rows:
#             print(f"{row['id']}: {row['category_name']}")
#         print("※削除したカテゴリーですでに記録をしている場合、その記録のカテゴリーは不明になります")
#         category_id = input_util.input_int("削除するカテゴリーのIDを入力して下さい")
#         category_info = get_category(cursor, category_id)
#         studying_user_info =  access_studying_users.check_studying_user(cursor, user_id)
#         if studying_user_info:
#             studying_cateogy_id = studying_user_info[0]['category_id']
#         else:
#             studying_cateogy_id = False
#         if category_info:                                     
#             if user_id == category_info[0]['user_id']:      
#                 if category_id != studying_cateogy_id:
#                     if input_util.input_boolean(f"カテゴリー{category_info[0]['category_name']}を削除していいですか？"):
#                         sql = 'delete from categories where id = %s'
#                         data = [category_id]
#                         cursor.execute(sql, data)
#                         cunx.commit()
#                         print("カテゴリーの削除が完了しました")
#                     else:
#                         print("キャンセルしました")
#                 else:
#                     print("現在学習中のカテゴリなため削除できません")
#             else:
#                 print(f"[Error]: カテゴリーのユーザーIDとあなたのIDが一致しないため削除できません")
#         else:
#             print(f"[Erroe]: ID: {category_id}のカテゴリーは存在しません")
#     else:
#         print("カテゴリを登録していません")
#     return True



# カテゴリの追加
# @database_connect
# def create_category(cnx, cursor, user_id):
#     user_info = access_users.check_user_by_id(cursor, user_id)   # ログイン中に他のユーザーによって削除される可能性を考慮
#     if user_info:
#         category_name = input_util.input_any(f"カテゴリー名を入力してください")
#         category_info = check_category(cursor, user_id, category_name)
#         if not category_info:
#             sql = 'insert into categories (user_id, category_name) values (%s, %s)'
#             data = [user_id, category_name]
#             cursor.execute(sql, data)
#             cnx.commit()
#             print("カテゴリーの追加が完了しました")
#             return True
#         else:
#             print(f"[Error]: {category_name}はすでに登録済みです")
#     else:
#         print(f"[Error]: {user_id}は登録されていません。一度ログアウトしてログインしなおしてください")    
# if __name__ == '__main__':
#     create_category(2)