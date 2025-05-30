import mysql.connector


# 例外の定義
class Database_connect_Error(Exception):
    pass


class Database_operation_Error(Exception):
    pass


# 関数実行前にデータベースに接続、実行後にcloseするでデコレーター
# エラーが起きた場合は例外を発生させる
class database_connect:
    def __init__(self, func):
        self.func = func
             
    def __call__(self, *args, **kwargs):
        try:
            cnx = mysql.connector.connect(
                # データベースにアクセスする際の情報
                host = "localhost",
                user = "root",
                password="password",
                database = "23010015_exam_db"
            )
            cursor = cnx.cursor(dictionary=True)
            # コネクションが切れた時に再接続する
            cnx.ping(reconnect=True)
        except:
            raise Database_connect_Error("データベースとの接続に失敗")
        try:
            result = self.func(cnx, cursor, *args, **kwargs)
            return result
        except Exception as e:
            print(e)
            raise Database_operation_Error("データベースの操作中にエラーが発生")
        finally:
            if cursor:
                cursor.close()
            if cnx:
                cnx.close()
    

# 例外を検知するデコレーター
class check_error:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        try:
            self.func(*args, **kwargs)
        except Database_operation_Error as e:
            print(e)
            return 
        except Database_connect_Error as e:
            print(e)
            return
        except Exception as e:
            print("予期しないエラーが発生")
            print(e)