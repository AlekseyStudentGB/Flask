from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def func():
    context = {'title': 'Главная',
                'text': 'Новости нашего магазина'}
    return render_template('index1.html', **context)

@app.route('/index2')
def shop():
    context = {'title': 'Shop'}
    return render_template('index2.html', **context)

@app.route('/index3')
def index3():
    context = {'title': 'Одежда'}
    return render_template('index3.html', **context)

@app.route('/index4')
def index4():
    context = {'title': 'Обувь'}
    return render_template('index4.html', **context)

@app.route('/index5')
def index5():
    context = {'title': 'Верхняя одежда'}
    return render_template('index5.html', **context)


if __name__ == '__main__':
    app.run()
