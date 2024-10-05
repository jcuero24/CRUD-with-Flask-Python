from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Función para conectarse a la base de datos
def get_db_connection():
    conn = sqlite3.connect('motos.db')
    conn.row_factory = sqlite3.Row
    return conn

# Ruta para ver todas las motos deportivas
@app.route('/')
def index():
    conn = get_db_connection()
    motos = conn.execute('SELECT * FROM motos').fetchall()
    conn.close()
    return render_template('index.html', motos=motos)

# Ruta para agregar una nueva moto deportiva
@app.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        modelo = request.form['modelo']
        marca = request.form['marca']
        velocidad_maxima = request.form['velocidad_maxima']

        conn = get_db_connection()
        conn.execute('INSERT INTO motos (modelo, marca, velocidad_maxima) VALUES (?, ?, ?)', 
                     (modelo, marca, velocidad_maxima))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('add.html')

# Ruta para editar una moto deportiva
@app.route('/edit/<int:id>', methods=('GET', 'POST'))
def edit(id):
    conn = get_db_connection()
    moto = conn.execute('SELECT * FROM motos WHERE id = ?', (id,)).fetchone()

    if request.method == 'POST':
        modelo = request.form['modelo']
        marca = request.form['marca']
        velocidad_maxima = request.form['velocidad_maxima']

        conn.execute('UPDATE motos SET modelo = ?, marca = ?, velocidad_maxima = ? WHERE id = ?', 
                     (modelo, marca, velocidad_maxima, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    conn.close()
    return render_template('edit.html', moto=moto)

# Ruta para eliminar una moto deportiva
@app.route('/delete/<int:id>', methods=('POST',))
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM motos WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
