from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)
app.secret_key = getenv("SECRET_KEY")

@app.route("/")
def index():
    db.session.execute("INSERT INTO visitors (time) VALUES (NOW())")
    db.session.commit()
    result = db.session.execute("SELECT COUNT(*) FROM visitors")
    counter = result.fetchone()[0]
    return render_template("index.html", counter=counter)

@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    sql = "SELECT password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if user == None:
        return redirect("/register")
    else:
        hash_value = user[0]
    if check_password_hash(hash_value,password):
        session["username"] = username
        return redirect("/homechores")
    else:
        return render_template("wrong_passwd.html")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/registering", methods=["POST"])
def registering():
    username = request.form["username"]
    password = request.form["password"]
    age = request.form["age"]
    if int(age) < 7:
        wage_id = 3
    elif int(age) >=7 and int(age) < 13:
        wage_id = 2
    else:
        wage_id = 1
    role = 2
    hash_value = generate_password_hash(password)
    sql = "INSERT INTO users (username,password,role,wage_id) VALUES (:username,:password,:role,:wage_id)"
    db.session.execute(sql, {"username":username,"password":hash_value,"role":role,"wage_id":wage_id})
    db.session.commit()
    return redirect("/")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/homechores")
def homechores():
    return render_template("homechores.html")
