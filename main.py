from flask import Flask, render_template, request, redirect, url_for
from db_connect import dbc

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/after")
def after():
    return render_template("after.html")


@app.route('/register', methods=['post'])
def register_user():
    name = request.form['name']
    username = request.form["username"]
    password = request.form["password"]
    email = request.form["email"]

    try:
        query = "INSERT INTO users(name, username, password, email) VALUES(%s, %s, %s, %s)"
        value = (name, username, password, email)
        dbc.execute(query, value)
        return redirect(url_for("after"))

    except Exception as e:
        print(f"Xato: {e}")
        return render_template('index.html', error_message="Xato! Qayta urinib ko'ring!"), 500

@app.route('/login', methods=["post"])
def login_user():
    username = request.form['username']
    password = request.form['password']
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    value = (username, password)
    dbc.execute(query, value)
    result = dbc.fetchone()

    if result:
        return redirect(url_for("after"))
    return "Noto'g'ri username yoki parol!", 400

if __name__ == "__main__":
    app.run(debug=True)
