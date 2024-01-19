import mysql.connector
# 例外の定義
class Database_connect_Error(Exception):
    pass
class Database_operation_Error(Exception):
    pass

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
            except:
                raise Database_operation_Error("データベースの操作中にエラーが発生")
            finally:
                cursor.close()
                cnx.close()
        except:
            raise Database_connect_Error("データベースとの接続に失敗")
        
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
            