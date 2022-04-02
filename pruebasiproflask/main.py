from urllib import response
from flask import Flask, request, make_response, redirect

app = Flask(__name__)

@app.route('/')
def index():
    user_ip=request.remote_addr

    response= make_response(redirect('/hello'))
    response.set_cookie('user_ip',user_ip)

    return response

# @app.route('/')
@app.route('/hello')
def hello():
    # user_ip=request.remote_addr
    user_ip=request.cookies.get('user_ip')

    return 'Hello World Flask :), para la ip {}'.format(user_ip)

#if __name__ == "__main__":
#    app.run(port=8080)

