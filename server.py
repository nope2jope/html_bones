from flask import Flask, render_template

server = Flask(__name__)

@server.route('/')
def greet_visitor():
    return render_template('index.html')

@server.route('/contact')
def contact():
    return render_template('gittact.html')

@server.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')

if __name__ == '__main__':
    server.run()