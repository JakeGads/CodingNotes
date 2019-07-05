from app import app
from flask import render_template


@app.route('/')
@app.route('/index')

def index():
    return 'It is Wensday My Dudes'

@app.route('/test')
def test():
    return render_template('test.html', title='Home', user={'username': 'Jake'})