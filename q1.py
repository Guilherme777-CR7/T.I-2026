from flask import Flask

app = Flask(__name__)

@app.route('/ola/<nome>')
def ola(nome):
    return f'Olá, {nome}! Seja bem-vinda ao sistema.'

if __name__ == '__main__':
    app.run(debug=True)