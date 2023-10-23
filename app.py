from flask import Flask, redirect, render_template, request

import use_cases
from database import db

app = Flask(__name__)

# Configura banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost:3306/byte_card'
app.config['SQLALCHEMY_ECHO'] = True
db.init_app(app)


@app.route('/')
def index():
    return redirect('/cartoes/lista')


@app.route('/cartoes/lista')
def lista_cartoes():
    return render_template('cartao/lista.html', cartoes=use_cases.lista_cartoes())


@app.route('/cartoes/formulario')
def formulario_cartao():
    return render_template('cartao/formulario.html')


@app.route('/cartoes/cadastrar', methods=['POST'])
def cadastra_cartao():
    form = request.form
    use_cases.cadastra_cartao(form['cliente'], float(form['limite']))

    return redirect('/cartoes/lista')


@app.route('/cartoes/<id>/cancelar')
def cancela_cartao(id):
    cartao_id = int(id)
    use_cases.cancela_cartao(cartao_id)

    return redirect('/cartoes/lista')


@app.route('/cartoes/<id>/ativar')
def ativa_cartao(id):
    cartao_id = int(id)
    use_cases.ativa_cartao(cartao_id)

    return redirect('/cartoes/lista')


@app.route('/cartoes/<id>/limite')
def formulario_limite(id):
    cartao = use_cases.pesquisa_cartao_por_id(int(id))
    return render_template('cartao/limite.html', cartao=cartao)


@app.route('/cartoes/alterar-limite', methods=['POST'])
def altera_limite():
    form = request.form
    cartao_id = int(form['id'])
    limite = float(form['limite'])

    use_cases.define_limite(cartao_id, limite)

    return redirect('/cartoes/lista')


@app.route('/compras/formulario')
def formulario_compra():
    cartoes = use_cases.lista_cartoes()

    return render_template('compra/formulario.html', cartoes=cartoes)


@app.route('/compras/cadastrar', methods=['POST'])
def cadastra_compra():
    use_cases.cadastra_compra(
        request.form['cartao'],
        request.form['valor'],
        request.form['categoria'],
        request.form['estabelecimento']
    )
    return redirect('/compras/formulario')


if __name__ == '__main__':
    app.run(debug=True)
