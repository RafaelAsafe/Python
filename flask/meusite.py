from flask import Flask, render_template
app = Flask(__name__)


@app.route('/inicial')
def ola_mundo():
    return render_template("index.html")


@app.route('/sobre')
def sobre():
    return render_template("sobre.html")


@app.route('/<string:nome>')
def error(nome):
    MsgError = f'página "{nome}" não existe'
    return render_template("error404.html", MsgError2=MsgError)
