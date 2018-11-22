"""Raising custom erros.

Sometimes users will perform invalid actions
(either intentionally, or unintentionally)

In order to protect our application and also inform the user about her
mistake, we'll need to raise custom errors.
The HTTP protocol support error responses with different
status codes. For example:
* 4XX: Client Error.
       These errors are caused by user's fault. The user tried to perform
       an invalid operation, forgot to send some data, etc.
* 5XX: Server Error.
       These are errors generated in our end. The error was produced
       in the server.

If we're raising an error after a user's action, we'll probably raise a `4XX`.
The most common `4XX` errors are:
* 404 (Not Found): Resource not found
* 400 (Bad Request): A general error. Used for example if the user forgets
                     to submit important data.
* 401 (Unauthorized): The user hasn't been authorized to access this resource.
                      Usually, will need to perform some type of authentication
* 403 (Forbidden): Similar to 401, but in this case the server knows who
                   the user is, but that user is not allowed to access
                   that resource. Usually an unprivileged user is trying to
                   perform admin actions.

Useful Resources:
https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#4xx_Client_Error
https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#5xx_Server_Error
"""

from flask import Flask, render_template, abort

app = Flask(__name__)

AUTORES_INFO = {
    'poe': {
        'nome_completo': 'Edgar Allan Poe',
        'nacionalidade': 'US',
        'principal_livro': 'The Raven',
        'data_de_nascimento': 'January 19, 1809',
        'foto': 'https://upload.wikimedia.org/wikipedia/commons/7/75/Edgar_Allan_Poe_2_retouched_and_transparent_bg.png'
    },
    'borges': {
        'nome_completo': 'Jorge Luis Borges',
        'nacionalidade': 'Argentine',
        'principal_livro': 'The Aleph',
        'data_de_nascimento': 'August 24, 1899',
        'foto': 'https://upload.wikimedia.org/wikipedia/commons/c/cf/Jorge_Luis_Borges_1951%2C_by_Grete_Stern.jpg'
    }
}

@app.route('/')
def autores():
    return render_template('routing/autores.html')


@app.route('/autor/<string:sobrenome_autor>')
def autor(sobrenome_autor):
    if sobrenome_autor not in AUTORES_INFO:
        abort(404)
    return render_template('routing/autor.html',
                           autor=AUTORES_INFO[sobrenome_autor])

@app.route('/autor/<string:sobrenome_autor>/edit')
def autor_admin(sobrenome_autor):
    abort(401)

@app.errorhandler(404)
def not_found(error):
    return render_template('routing/404.html'), 404
