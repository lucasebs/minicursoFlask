"""Moving the template code to a separate file.

Mixing Python code with HTML is ugly. Templates usually live in their own
location. By default, flask will look up for templates in a 'templates'
directory living in the same path as the application.

"""

from flask import Flask
from flask import render_template  # !Importante

app = Flask(__name__)


@app.route('/')
def hello_world():
    nome_biblioteca = "Poe"
    return render_template('index.html', nome_biblioteca=nome_biblioteca)
