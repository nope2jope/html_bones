from flask import Flask, render_template

server = Flask(__name__)

@server.route('/')
def greet_visitor():
    return render_template('index.html')

@server.route('/gittact.html')
def provide_contacts():
    return render_template('gittact.html')

@server.route('/hobbies.html')
def serve_hobbies():
    return render_template('hobbies.html')

if __name__ == '__main__':
    server.run(debug=True)