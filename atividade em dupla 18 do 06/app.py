from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = "senha123"

@app.route("/")
def inicio():
    if "placar" not in session:
        session["placar"] = {
            "Time A": 0,
            "Time B": 0,
            "Time C": 0,
            "Time D": 0
        }

    return render_template(
        "index.html",
        placar=session["placar"]
    )

@app.route("/ponto/<time>")
def ponto(time):
    placar = session["placar"]

    if time in placar:
        placar[time] += 1

    session["placar"] = placar
    return redirect("/")

@app.route("/zerar")
def zerar():
    session["placar"] = {
        "Time A": 0,
        "Time B": 0,
        "Time C": 0,
        "Time D": 0
    }

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)