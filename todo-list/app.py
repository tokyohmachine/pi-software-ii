from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Configuração do Banco de Dados SQLite (Model)
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            status TEXT DEFAULT 'Pendente'
        )
    ''')
    conn.commit()
    conn.close()

# Rota Principal (Listar e Adicionar) - Controller
@app.route('/', methods=['GET', 'POST'])
def index():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    if request.method == 'POST':
        titulo = request.form['titulo']
        cursor.execute("INSERT INTO tarefas (titulo) VALUES (?)", (titulo,))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    conn.close()
    return render_template('index.html', tarefas=tarefas)

# Rota para Excluir Tarefa
@app.route('/deletar/<int:id>')
def deletar(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
    