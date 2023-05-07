from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/urls')
def urls():
    return render_template('urls.html')


@app.route('/<short>')
def short():
    pass

if __name__ == '__main__':
    app.run(debug=True)
