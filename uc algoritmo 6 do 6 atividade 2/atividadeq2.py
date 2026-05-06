from flask import Flask, render_template

app = Flask(__name__)

@app.route('/alunos')
def alunos():
    lista_alunos = [
        {"nome": "Alice", "matricula": "12345678"},
        {"nome": "Bruno", "matricula": "86123962"},
        {"nome": "Clara", "matricula": "27167398"},
        {"nome": "Marlison", "matricula": "38271612"},
        {"nome": "Valéria", "matricula": "75826163"}
    ]
    return render_template('alunos.html', alunos=lista_alunos)

if __name__ == '__main__':
    app.run(debug=True)