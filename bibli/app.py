from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = "biblioteca.db"


def conectar():
    conexao = sqlite3.connect(DATABASE)
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_banco():
    conexao = conectar()

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS autores (
            id_autor INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    """)

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS categorias (
            id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    """)

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS livros (
            id_livro INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            ano INTEGER,
            id_autor INTEGER NOT NULL,
            id_categoria INTEGER NOT NULL,
            FOREIGN KEY (id_autor) REFERENCES autores(id_autor),
            FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
        )
    """)

    conexao.commit()
    conexao.close()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    conexao = conectar()

    autores = conexao.execute(
        "SELECT * FROM autores ORDER BY nome"
    ).fetchall()

    categorias = conexao.execute(
        "SELECT * FROM categorias ORDER BY nome"
    ).fetchall()

    if request.method == "POST":
        titulo = request.form["titulo"]
        ano = request.form["ano"]
        id_autor = request.form["id_autor"]
        id_categoria = request.form["id_categoria"]

        conexao.execute("""
            INSERT INTO livros
            (titulo, ano, id_autor, id_categoria)
            VALUES (?, ?, ?, ?)
        """, (titulo, ano, id_autor, id_categoria))

        conexao.commit()
        conexao.close()

        return redirect(url_for("livros"))

    conexao.close()

    return render_template(
        "cadastrar.html",
        autores=autores,
        categorias=categorias
    )


@app.route("/livros")
def livros():
    conexao = conectar()

    livros = conexao.execute("""
        SELECT
            livros.id_livro,
            livros.titulo,
            livros.ano,
            autores.nome AS autor,
            categorias.nome AS categoria
        FROM livros
        INNER JOIN autores
            ON livros.id_autor = autores.id_autor
        INNER JOIN categorias
            ON livros.id_categoria = categorias.id_categoria
        ORDER BY livros.titulo
    """).fetchall()

    conexao.close()

    return render_template("livros.html", livros=livros)


@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    conexao = conectar()

    if request.method == "POST":
        titulo = request.form["titulo"]
        ano = request.form["ano"]
        id_autor = request.form["id_autor"]
        id_categoria = request.form["id_categoria"]

        conexao.execute("""
            UPDATE livros
            SET titulo = ?,
                ano = ?,
                id_autor = ?,
                id_categoria = ?
            WHERE id_livro = ?
        """, (titulo, ano, id_autor, id_categoria, id))

        conexao.commit()
        conexao.close()

        return redirect(url_for("livros"))

    livro = conexao.execute("""
        SELECT * FROM livros
        WHERE id_livro = ?
    """, (id,)).fetchone()

    autores = conexao.execute(
        "SELECT * FROM autores ORDER BY nome"
    ).fetchall()

    categorias = conexao.execute(
        "SELECT * FROM categorias ORDER BY nome"
    ).fetchall()

    conexao.close()

    return render_template(
        "cadastrar.html",
        livro=livro,
        autores=autores,
        categorias=categorias
    )


@app.route("/excluir/<int:id>")
def excluir(id):
    conexao = conectar()

    conexao.execute("""
        DELETE FROM livros
        WHERE id_livro = ?
    """, (id,))

    conexao.commit()
    conexao.close()

    return redirect(url_for("livros"))


@app.route("/adicionar-autor", methods=["POST"])
def adicionar_autor():
    nome = request.form["nome"]

    conexao = conectar()

    conexao.execute(
        "INSERT INTO autores (nome) VALUES (?)",
        (nome,)
    )

    conexao.commit()
    conexao.close()

    return redirect(url_for("cadastrar"))


@app.route("/adicionar-categoria", methods=["POST"])
def adicionar_categoria():
    nome = request.form["nome"]

    conexao = conectar()

    conexao.execute(
        "INSERT INTO categorias (nome) VALUES (?)",
        (nome,)
    )

    conexao.commit()
    conexao.close()

    return redirect(url_for("cadastrar"))


if __name__ == "__main__":
    criar_banco()
    app.run(debug=True)