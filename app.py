from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def cadastro():

    mensagem = ""
    dados = {}

    if request.method == "POST":

        nome = request.form.get("nome", "").strip().title()
        email = request.form.get("email", "").strip().lower()
        telefone = request.form.get("telefone", "").strip()
        cpf = request.form.get("cpf", "").strip()
        cidade = request.form.get("cidade", "").strip().title()
        estado = request.form.get("estado", "").strip().upper()
        curso = request.form.get("curso", "").strip()
        idade = request.form.get("idade", "").strip()
        senha = request.form.get("senha", "").strip()

        telefone = telefone.replace("(", "")
        telefone = telefone.replace(")", "")
        telefone = telefone.replace("-", "")
        telefone = telefone.replace(" ", "")

        cpf = cpf.replace(".", "")
        cpf = cpf.replace("-", "")

        if (not nome or not email or not telefone or not cpf or
            not cidade or not estado or not curso or
            not idade or not senha):

            mensagem = "Preencha todos os campos obrigatórios."

        elif len(nome) < 8:
            mensagem = "Nome inválido."

        elif "@" not in email or ".com" not in email:
            mensagem = "E-mail inválido."

        elif not telefone.isdigit() or len(telefone) != 11:
            mensagem = "Telefone inválido."

        elif not cpf.isdigit() or len(cpf) != 11:
            mensagem = "CPF inválido."

        elif len(cidade) < 3:
            mensagem = "Cidade inválida."

        elif len(estado) != 2 or not estado.isalpha():
            mensagem = "Estado inválido."

        elif not idade.isdigit():
            mensagem = "Idade inválida."

        elif int(idade) < 16:
            mensagem = "Idade mínima é 16 anos."

        elif len(senha) < 8 or not re.search(r"\d", senha):
            mensagem = "Senha muito fraca."

        else:
            mensagem = "Cadastro realizado com sucesso!"

            dados = {
                "nome": nome,
                "email": email,
                "telefone": telefone,
                "cpf": cpf,
                "cidade": cidade,
                "estado": estado,
                "curso": curso,
                "idade": idade
            }

    return render_template("index.html", mensagem=mensagem, dados=dados)

if __name__ == "__main__":
    app.run(debug=True)