from access_databasaes import access_studying_users, access_users, access_categories
from util.db_util import check_error

@check_error
def main():
    rows = access_studying_users.get_all_info()
    if rows:
        for row in rows:
            user_info = access_users.check_user_by_id(row['user_id'])
            user_name = user_info[0]['user_name']
            affiliaton = user_info[0]['affiliaton']
            category_name = access_categories.get_category(row['category_id'])[0]['category_name']
            print(f"ユーザー名:{user_name} カテゴリ: {category_name} 勉強開始時間: {row['start_time']} 所属: {affiliaton}")
    elif rows == None:
        print("現在だれも勉強していません")