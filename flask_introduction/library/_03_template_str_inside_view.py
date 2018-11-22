"""Using Flask template engines.

In this example we're using Flask template engine (Jinja2) to simplify
the process to generate the resulting HTML.

**TODO**
In our previous example we had to do a lot of string handling to
create the <ul> with authors.
It's your turn to use the template engine to build the same result.
"""
from flask import Flask
from flask import render_template_string  # !Important

app = Flask(__name__)


@app.route('/')
def hello_world():
    nome_biblioteca = "Legal"
    html = """
        <html>
            <h1>Bem vindo a Biblioteca {{nome_biblioteca}} !</h1>
        </html>
    """
    autores = ["Alan Poe", "Jorge L. Borges", "Mark Twain"]
    rendered_html = render_template_string(html, nome_biblioteca=nome_biblioteca)
    # Construa novamente a lista de autores(utilize <ul>) utilizando a biblioteca Jinja2 {{autores[]}}
    return rendered_html
