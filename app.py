# app.py 파일입니다.
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/mypage')
def my_page():
    return 'This is My Page!'


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)