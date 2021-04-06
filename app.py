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
    sql = "SELECT id, description, responsible_id, minutes, status_id, category_id FROM chores ORDER BY id DESC"
    result = db.session.execute(sql)
    chores = result.fetchall()
    return render_template("homechores.html", chores=chores)

@app.route("/add_chore")
def add_chore():
    return render_template("new_chore.html")

@app.route("/new_chore", methods=["POST"])
def new_chore():
    kuvaus= request.form["kuvaus"]
    kesto = request.form["kesto"]
    kukapa = session["username"]
    sql = "SELECT id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":kukapa})
    kukapaid = result.fetchone()[0]
    sql2 = "INSERT INTO chores (description,responsible_id,minutes,status_id,category_id) VALUES (:description,:responsible_id,:minutes,:status_id,:category_id)"
    db.session.execute(sql2, {"description":kuvaus,"responsible_id":kukapaid,"minutes":kesto,"status_id":3,"category_id":3})
    db.session.commit()
    return render_template("homechores.html")

@app.route("/choose_chore/<int:id>")
def chore(id):
    sql = "SELECT id, description, responsible_id, minutes, status_id, category_id FROM chores WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    content = result.fetchall()
    sql2 = "SELECT * FROM statuses WHERE value in (1, 2, 3, 4)"
    result2 = db.session.execute(sql2)
    statuses = result2.fetchall()
    return render_template("chore.html", id=id, content=content, statuses=statuses)

@app.route("/update_chore", methods=["POST"])
def update_chore():
    id = request.form["id"]
    minutes = request.form["kesto"]
    status_id = request.form["status"]
    print(id)
    print(minutes)
    print(status_id)
    if minutes in (None, "", ''):
        print("menee tähän ekaan vaihtoehtoon")
        sql = "UPDATE chores SET status_id=:status_id WHERE id=:id"
        db.session.execute(sql, {"status_id":status_id,"id":id})
        db.session.commit()
    else:
        print("ja nyt menee tähän tokaan")
        sql = "UPDATE chores SET status_id=:status_id WHERE id=:id" 
        db.session.execute(sql, {"status_id":status_id,"id":id})
        db.session.commit()
        sql2 = "UPDATE chores SET minutes=:minutes WHERE id=:id"
        db.session.execute(sql2, {"minutes":minutes,"id":id})
        db.session.commit()
    return redirect("/homechores")
