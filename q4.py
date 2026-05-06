from flask import Flask

app = Flask(__name__)

@app.route('/produto/<nome>/<float:preco>')
def produto(nome, preco):
    return f'O produto {nome} custa R$ {preco:.2f}'

if __name__ == '__main__':
    app.run(debug=True)