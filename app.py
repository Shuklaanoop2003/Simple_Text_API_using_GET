from flask import Flask, request
app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    username = request.args.get('username')
    if username:
        return f'Hello, {username}!'
    else:
        return 'Please provide a username.'

if __name__ == '__main__':
    app.run()
    
