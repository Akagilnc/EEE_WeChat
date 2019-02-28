# coding: utf-8

from flask import Flask
from werobot.contrib.flask import make_view
from index import robot

app = Flask(__name__)
app.add_url_rule(rule='/robot',  # WeRoBot 挂载地址
                 endpoint='robot',  # Flask 的 endpoint
                 view_func=make_view(robot),
                 methods=['GET', 'POST'])


@app.route("/")
def hello():
    return "Hello Flask World!"


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
