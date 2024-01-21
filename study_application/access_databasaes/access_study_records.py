import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
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
    sql = 'select * from study_records where user_id = %s and study_date between %s and %s'
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


# 勉強記録の追加の際に使う関数
# @database_connect
# def create_study_record(cnx, cursor, user_id):
#     user_info = access_users.check_user_by_id(cursor, user_id)   # ログイン中に他のユーザーによって削除される可能性を考慮
#     if user_info:
#         study_info = access_studying_users.get_studying_user_info(cursor, user_id)
#         if study_info:
#             category_id = study_info[0]['category_id']
#             category_name = access_categories.get_category(cursor, category_id)
#             if category_name:
#                 category_name = category_name[0]['category_name']
#             else:
#                 # 学習中にカテゴリが消されてた場合はその他に書き換え
#                 category_id = 1
#                 category_name = 'その他'
#             study_date = study_info[0]['start_time'].date()
#             # datetime.timedeltaから合計秒数を求めそこから時間と分を取得
#             difference = int((datetime.datetime.now() - study_info[0]['start_time']).total_seconds())
#             MinutesGet, SecondsGet = divmod(difference, 60)   # 分, 秒
#             HoursGet, MinutesGet = divmod(MinutesGet, 60)   # 時間, 分
#             study_time = f"{HoursGet}:{MinutesGet}:00"   # 秒は切り捨て
#             # ==============================================================================
#             # 時間制限を入れる必要あり
#             # ==============================================================================
#             print(f"カテゴリリー名: {category_name}")
#             print(f"勉強年月日: {study_date}")
#             print(f"勉強時間: {HoursGet}時間{MinutesGet}分")
#             if input_util.input_boolean("記録しますか?"):
#                 sql = 'insert into study_records (user_id, category_id, study_date, study_time) values (%s, %s, %s, %s)'
#                 data = [user_id, category_id, study_date, study_time]
#                 cursor.execute(sql, data)
#                 cnx.commit()
#                 access_studying_users.delete_studying_user(cnx, cursor, user_id)
#                 print("勉強の記録が完了しました")
#             else:
#                 print("キャンセルしました")
#                 if input_util.input_boolean("引き続き同じ勉強をしますか?しない場合現在の勉強中の記録を削除します"):
#                     pass
#                 else:
#                     access_studying_users.delete_studying_user(cnx, cursor, user_id)
#         else:
#             print(f"[Error]: 現在ID{user_id}は勉強中ではありません")
#     else:
#         print(f"[Error]: {user_id}は登録されていません。一度ログアウトしてログインしなおしてください")