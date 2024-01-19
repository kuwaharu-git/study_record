import mysql.connector
# 関数実行前にデータベースに接続、実行後にcloseするでデコレーター
# エラーが起きた場合はFalseを返す
class database_connect:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        try:
            cnx = mysql.connector.connect(
                # データベースにアクセスする際の情報
                host = "",
                user = "",
                password="",
                database = "" 
            )
            cursor = cnx.cursor(dictionary=True)
            # コネクションが切れた時に再接続する
            cnx.ping(reconnect=True)
            try:
                result = self.func(cnx, cursor, *args, **kwargs)
                return result
            except Exception as e:
                print("データベースの操作でエラーが起きました。")
                print(e)
                return False
            finally:
                cursor.close()
                cnx.close()
        except Exception as e:
            print("データベース接続でエラーが起きました。")
            print(e)
            return False
        
