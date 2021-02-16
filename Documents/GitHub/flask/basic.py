from flask import Flask
app = Flask(__name__)  # root namespace

# '@' signifies a decorator- way to wrap a function and modifying its behaviour
@app.route('/')  # root directory
# routing webpage to the function
def index():
    return 'This is the homepage'


@app.route('/hello')
def hello():
    return '<h2>Hello!<h2>'  # we can add html elements


@app.route('/profile/<username>')  # adding variable
def profile(username):
    return "<h1>Hello %s<h1>" % username


@app.route('/post/<int:post_id>')  # adding int variable, need to define type
def post(post_id):
    return "<h1>Post ID is %s<h1>" % post_id


if __name__ == "__main__":
    app.run()  # start the app
