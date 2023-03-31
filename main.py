import flask 

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')
@app.route('/portfolio')
def portfolio():
    return flask.render_template('portfolio.html')
@app.route('/contact')
def contact():
    return flask.render_template('contact.html')
@app.route('/about')
def about():
    return flask.render_template('about.html')


def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()