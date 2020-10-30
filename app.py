from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html', lista=range(15))

@app.route('/<nome>')
def ola_com_nome(nome):
    return render_template('index.html', nome_pessoa=nome)