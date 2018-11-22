"""Flask routing.

Specifying routes for our Flask app is simple. We do it just by providing
the desired route in the `@app.route()` decorator. Sometimes our routes have
dynamic parameters. For example:
* `/posts/23` -> The number 23 (post id) is dynamic
* `/repo/flask-introduction/stars` -> The name of the repo (flask-introduction)
                                      is dynamic

Supporting dynamic routing parameters is really simple. We just need to
specify the desired dynamic portion by giving it a name and surrounding
it between `<>`.
"""

from flask import Flask, render_template

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


@app.route('/autor/<sobrenome_autor>')
def autor(sobrenome_autor):
    return render_template('routing/autor.html',
                           autor=AUTORES_INFO[sobrenome_autor])
