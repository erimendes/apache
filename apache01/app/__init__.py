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
