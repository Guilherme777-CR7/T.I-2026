from flask import Flask

app = Flask(__name__)

@app.route("/o/<tipo>/<op1>/<op2>")
def o(tipo, op1, op2):
    try:
        num1 = float(op1)
        num2 = float(op2)
    except:
        return "Valores inválidos"

    if tipo == "sum":
        r = num1 + num2
    elif tipo == "sub":
        r = num1 - num2
    elif tipo == "mult":
        r = num1 * num2
    elif tipo == "div":
        if num2 == 0:
            return "Erro: divisão por zero"
        r = num1 / num2
    else:
        return "Operação inválida"

    return f"Resultado: {r}"

if __name__ == "__main__":
    app.run(debug=True)