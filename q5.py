from flask import Flask

app = Flask(__name__)

@app.route('/repetir/<palavra>/<int:vezes>')
def repetir(palavra, vezes):
    return ' '.join([palavra] * vezes)

if __name__ == '__main__':
    app.run(debug=True)