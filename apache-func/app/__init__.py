# from flask import Flask

# app = Flask(__name__)

# # Página inicial
# @app.route('/')
# def home():
#     return "Página Inicial"

# # Página Sobre
# @app.route('/sobre')
# def sobre():
#     return "Sobre nós"

# # Página Contato
# @app.route('/contato')
# def contato():
#     return "Entre em contato"

# if __name__ == "__main__":
#     app.run(debug=True, port=8080)


import os
from flask import Flask, render_template

def create_app():
    app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'templates'))

    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/sobre')
    def sobre():
        return render_template('sobre.html')

    @app.route('/contato')
    def contato():
        return render_template('contato.html')

    return app
