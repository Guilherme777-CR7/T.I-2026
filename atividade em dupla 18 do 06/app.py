from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Banco de dados da Copa do Mundo (Todos começam com 0)
copa_dados = {
    "Países-Sede": {"Canadá": 0, "Estados Unidos": 0, "México": 0},
    "América do Sul (CONMEBOL)": {"Argentina": 0, "Brasil": 0, "Colômbia": 0, "Equador": 0, "Paraguai": 0, "Uruguai": 0},
    "Europa (UEFA)": {
        "Alemanha": 0, "Áustria": 0, "Bélgica": 0, "Bósnia e Herzegovina": 0, "Croácia": 0, 
        "Escócia": 0, "Espanha": 0, "França": 0, "Holanda": 0, "Inglaterra": 0, 
        "Noruega": 0, "Portugal": 0, "República Tcheca": 0, "Suécia": 0, "Suíça": 0, "Turquia": 0
    },
    "África (CAF)": {
        "África do Sul": 0, "Argélia": 0, "Cabo Verde": 0, "Costa do Marfim": 0, 
        "Egito": 0, "Gana": 0, "Marrocos": 0, "RD do Congo": 0, "Senegal": 0, "Tunísia": 0
    },
    "Ásia (AFC)": {
        "Arábia Saudita": 0, "Austrália": 0, "Catar": 0, "Coreia do Sul": 0, 
        "Irã": 0, "Iraque": 0, "Japão": 0, "Jordânia": 0, "Uzbequistão": 0
    },
    "América do Norte, Central e Caribe (Concacaf)": {"Curaçau": 0, "Haiti": 0, "Panamá": 0},
    "Oceania (OFC)": {"Nova Zelândia": 0}
}

@app.route('/')
def home():
    return render_template('index.html', confederacoes=copa_dados)

@app.route('/adicionar/<confederacao>/<pais>')
def adicionar_ponto(confederacao, pais):
    if confederacao in copa_dados and pais in copa_dados[confederacao]:
        copa_dados[confederacao][pais] += 1
    return redirect(url_for('home'))

@app.route('/resetar')
def resetar():
    for confederacao in copa_dados:
        for pais in copa_dados[confederacao]:
            copa_dados[confederacao][pais] = 0
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)