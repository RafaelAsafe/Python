from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    Variavel = "Descubra os números"

    if request.method == 'GET':
        return render_template("index.html", Variavel=Variavel)
    else:
        Numero = [3.5, 4.5, 9.5, 3.5]
        PalpiteA = float(request.form.get('name'))
        PalpiteB = float(request.form.get('name1'))
        PalpiteC = float(request.form.get('name2'))
        PalpiteD = float(request.form.get('name3'))

        if PalpiteA == Numero[0] and PalpiteB == Numero[1] and PalpiteC == Numero[2] and PalpiteD == Numero[3]:
            return '<h1>Você Ganhou</h1>'
        else:
            return'<h1>Você Perdeu</h1>'


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/<string:nome>')
def error(nome):
    MsgError = f'página "{nome}" não existe'
    return render_template("error404.html", MsgError2=MsgError)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
