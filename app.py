import pyodbc
from flask import Flask, render_template, request, redirect, session, flash, url_for
import os
from flask import redirect, url_for

app = Flask(__name__)
app.secret_key = 'supersecretkey' # Cámbiala en producción

server = 'YORDIBELLO'
database = 'NotasDB'
driver = '{ODBC Driver 17 for SQL Server}'

def get_db_connection():
    conn = pyodbc.connect(
        f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
    )
    return conn

@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect('/login')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, titulo, contenido FROM notas WHERE usuario_id = ?", session['user_id'])
    notas = cursor.fetchall()
    conn.close()
    return render_template('index.html', notas=notas)

from flask import session

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        password = request.form.get('password')
        if not usuario or not password:
            error = "Error: El usuario y la contraseña son requeridos"
        elif not (usuario == "admin" and password == "admin123"):
            error = "Error: Credenciales incorrectas"
        else:
            session['user_id'] = 1
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

@app.route('/nueva', methods=['GET', 'POST'])
def nueva_nota():
    if 'user_id' not in session:
        return redirect('/login')
    if request.method == 'POST':
        titulo = request.form['titulo']
        contenido = request.form['contenido']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO notas (titulo, contenido, usuario_id) VALUES (?, ?, ?)",
            titulo, contenido, session['user_id']
        )
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('nueva_nota.html')

@app.route('/editar/<int:nota_id>', methods=['GET', 'POST'])
def editar_nota(nota_id):
    if 'user_id' not in session:
        return redirect('/login')
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == 'POST':
        titulo = request.form['titulo']
        contenido = request.form['contenido']
        cursor.execute(
            "UPDATE notas SET titulo = ?, contenido = ? WHERE id = ? AND usuario_id = ?",
            titulo, contenido, nota_id, session['user_id']
        )
        conn.commit()
        conn.close()
        return redirect('/')
    else:
        cursor.execute("SELECT id, titulo, contenido FROM notas WHERE id = ? AND usuario_id = ?", nota_id, session['user_id'])
        nota = cursor.fetchone()
        conn.close()
        if nota:
            return render_template('editar_nota.html', nota=nota)
        else:
            flash("Nota no encontrada o no tienes permiso")
            return redirect('/')

@app.route('/eliminar/<int:nota_id>', methods=['POST'])
def eliminar_nota(nota_id):
    if 'user_id' not in session:
        return redirect('/login')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notas WHERE id = ? AND usuario_id = ?", nota_id, session['user_id'])
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)