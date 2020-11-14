# app.py 파일입니다.
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/test')
def my_page():
    return render_template('contents1.html')

@app.route('/result/yellow', methods=['GET'])
def result_yellow():
    return render_template('yellow.html')



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)