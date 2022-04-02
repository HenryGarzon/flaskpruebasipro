from urllib import response
from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

todos=['Implementar los modelos seleccionados de CV','Construir base de datos BD','Implementar e integrar BD con FrontEnd y BackEnd', 'Divulgar']

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def unexpectedError(error):
    return render_template('500.html', error=error)



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

