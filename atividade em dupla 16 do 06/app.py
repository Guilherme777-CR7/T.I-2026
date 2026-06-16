from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

app.secret_key = 'chave_secreta_super_segura_para_o_trabalho'

USUARIO_CORRETO = "admin"
SENHA_CORRETA = "1234"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        
        if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
            session['usuario'] = usuario
            return redirect(url_for('dashboard'))
        else:

            flash('Usuário ou senha incorretos!', 'danger')
            
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'usuario' not in session:
        flash('Você precisa fazer login para acessar esta página.', 'warning')
        return redirect(url_for('login'))
        
    return render_template('dashboard.html', usuario=session['usuario'])

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    flash('Você saiu da sessão com sucesso.', 'info')
    return redirect(url_for('login'))

@app.route('/rotalogin')
def rotalogin():
    return "Olá! Sou uma IA e esta é a rota extra solicitada no enunciado da atividade."

if __name__ == '__main__':
    app.run(debug=True)