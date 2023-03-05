# 使用するモジュールをimportする。
from flask import Flask

# Flaskのインスタンス（Webアプリの実体）を作成する。
app = Flask(__name__)


# この下の部分を「ルーティング」といい、「クライアントのリクエストにどのような処理を行うか」を設定する。
@app.route("/")  # "/" にアクセスした際の処理を書く。
def index():  # 処理全体は関数として定義する。
    return "Hello world!"  # ユーザに返す内容を"return"に書く。


# 以下の部分は、全てのルーティングよりも下に記述する必要がある。
if __name__ == "__main__":  # このファイル自体が実行されたときに実行する。
    app.run(debug=True)  # Flaskアプリを立ち上げる。デバッグモードを有効にする。
