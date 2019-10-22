from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'type' : 'WatchMan',
        'units' : 10,
        'date' : '10/10/19'
    },
    {
        'type' : 'BodyGuard',
        'units' : 2,
        'date' : '16/12/19'
    }
]
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)