from urllib import response
from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

todos=['TODO 1','TODO 2','TODO 3']

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
    context = {
        'user_ip': user_ip, 
        'todos': todos
    }

    # return 'Hello World Flask :), para la ip {}'.format(user_ip)
    # return render_template('hello.html', user_ip=user_ip)
    # return render_template('hello.html', user_ip=user_ip, todos=todos)
    # return render_template('hello.html', user_ip=user_ip, context=context)
    return render_template('hello.html', **context)


#if __name__ == "__main__":
#    app.run(port=8080)

