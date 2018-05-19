from flask import Flask, render_template, url_for

app = Flask('__name__')

posts = [
    {
        'author': 'Steve',
        'title': 'Hello World',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    }
]


@app.route('/')
def hello():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)