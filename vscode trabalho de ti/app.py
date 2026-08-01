from flask import Flask, render_template, request, redirect, url_for, session, flash
import json
import os

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

ARQUIVO_BANCO = 'usuarios.json'

def carregar_usuarios():
    if not os.path.exists(ARQUIVO_BANCO):
        return {}
    with open(ARQUIVO_BANCO, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def salvar_usuarios(usuarios):
    with open(ARQUIVO_BANCO, 'w', encoding='utf-8') as f:
        json.dump(usuarios, f, ensure_ascii=False, indent=4)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('username', '').strip()
        senha = request.form.get('password', '')
        casa = request.form.get('casa', '')

        usuarios = carregar_usuarios()

        if user not in usuarios:
            flash('Usuário não encontrado! Faça o cadastro primeiro.', 'danger')
            return render_template('login.html')

        dados_usuario = usuarios[user]
        if dados_usuario['senha'] != senha or dados_usuario['casa'] != casa:
            flash('Senha ou Casa incorretas!', 'danger')
            return render_template('login.html')

        session['usuario_logado'] = user
        flash(f'Bem-vindo, {dados_usuario["nome"]}!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        usuario = request.form.get('usuario', '').strip()
        senha = request.form.get('senha', '')
        casa = request.form.get('casa', '')

        if not nome or not usuario or not senha or not casa:
            flash('Todos os campos são obrigatórios!', 'warning')
            return render_template('cadastro.html')

        usuarios = carregar_usuarios()

        if usuario in usuarios:
            flash('Este usuário já existe! Escolha outro.', 'warning')
            return render_template('cadastro.html')

        usuarios[usuario] = {
            'nome': nome,
            'senha': senha,
            'casa': casa,
            'agendamentos': []
        }
        salvar_usuarios(usuarios)

        session['usuario_logado'] = usuario
        flash('Cadastro realizado com sucesso!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('cadastro.html')

@app.route('/dashboard')
def dashboard():
    if 'usuario_logado' not in session:
        flash('Faça login para acessar esta página.', 'warning')
        return redirect(url_for('login'))
    
    usuario_atual = session['usuario_logado']
    usuarios = carregar_usuarios()
    dados_usuario = usuarios.get(usuario_atual, {})
    
    return render_template('dashboard.html', 
                         usuario=usuario_atual,
                         nome=dados_usuario.get('nome', ''),
                         casa=dados_usuario.get('casa', ''))

@app.route('/logout')
def logout():
    session.pop('usuario_logado', None)
    flash('Você foi desconectado.', 'info')
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(debug=True)