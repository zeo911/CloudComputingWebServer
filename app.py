from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database connection parameters
config = {
    'host': 'db',  # The service name from docker-compose.yml
    'user': 'user',
    'password': 'userpass',
    'database': 'library'
}

# Route to display all books
@app.route('/')
def index():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', books=books)

# Route to add a new book
@app.route('/add', methods=['POST'])
def add_book():
    bookid =request.form["book_id"]
    name = request.form['name']
    author = request.form['author']
    category = request.form['category']
    copies = request.form['copies']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (BOOK_ID,NAME, AUTHOR, CATEGORY, COPIES) VALUES (%s,%s, %s, %s, %s)", (bookid,name, author, category, copies))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
