from util import input_util
import show_studying_users
from login_user import login
from user_manegement import user_management_menu


def main():
    print("=== 勉強記録アプリ ===")
    print("※入力の際に'cancel'と入力すると入力をキャンセルできます")
    print()
    while True:
        print("*** TOPメニュー ***")
        print("1: ログイン")
        print("2: ユーザー管理(新規ユーザーはこちらから登録)")
        print("3: 勉強中のユーザーを確認する")
        print("4: 終了")
        print()
        num = input_util.input_int("メニューを選択してください:")
        if num == 1:
            login.select_menu()
        elif num == 2:
            user_management_menu.select_menu()
        elif num == 3:
            show_studying_users.main()
        elif num == 4 or num == "cancel":
            break
        else:
            print("1~4で入力してください")
            continue


if __name__ == '__main__':
    main()