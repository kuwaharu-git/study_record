import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util.db_util import database_connect
from util import input_util
from access_databasaes.access_users import check_user_by_id
from access_databasaes import access_categories
import datetime

# 勉強中テーブルからuser_idで情報の取得
def check_studying_user(cursor, user_id):
    sql = 'select * from studying_users where user_id = %s'
    data = [user_id]
    cursor.execute(sql, data)
    rows = cursor.fetchall()
    if len(rows) != 0:
        return rows
    else:
        return False

# 勉強中テーブルにユーザーの追加
@database_connect
def insert_studying_user(cnx, cursor, user_id):
    user_info = check_user_by_id(cursor, user_id)   # ログイン中に他のユーザーによって削除される可能性を考慮
    if user_info:
        if not check_studying_user(cursor, user_id):
            now = datetime.datetime.now()
            print("1  :その他")
            category_list = [1]
            rows = access_categories.get_categories(cursor, user_id)
            while True:
                if rows:
                    for row in rows:
                        print(f"{row['id']:<3}:{row['category_name']}")
                        category_list.append(row['id'])
                else:
                    print("登録しているカテゴリーがありません")
                category_id = input_util.input_int("勉強するカテゴリーのカテゴリーIDを入力してください")
                if category_id in category_list:
                    sql = 'insert into studying_users (user_id, category_id, start_time) values (%s, %s, %s)'
                    data = [user_id, category_id, now]
                    cursor.execute(sql, data)
                    cnx.commit()
                    print("勉強の開始記録が完了しました。勉強が終わった後忘れずに終了の記録をつけてください")
                    break
                else:
                    print("表示されているあなたのカテゴリーのカテゴリーIDを入力してください")
        else:
            print(f"[Error]: すでに勉強中なため開始できません。")
    else:
        print(f"[Error]: {user_id}は登録されていません。一度ログアウトしてログインしなおしてください") 

# 勉強中userの削除
def delete_studying_user(cnx, cursor, user_id):
    study_info = check_studying_user(cursor, user_id)
    if study_info:
        sql = 'delete from studying_users where user_id = %s'
        data = [user_id]
        cursor.execute(sql, data)
        cnx.commit()
    else:
        print(f"[Error]: ID:{user_id}は現在勉強中ではありません")

# 勉強中のユーザーの情報の取得
def get_studying_user_info(cursor, user_id):
    study_info = check_studying_user(cursor, user_id)
    if study_info:
        return study_info
    else:
        print(f"[Error]: ID:{user_id}は現在勉強中ではありません")
        return False

if __name__ == '__main__':
    insert_studying_user(2)
    # delete_studying_user(2)