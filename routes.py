from app import app
from flask import redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash
from db import db
import secrets

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
        return render_template("wrong_passwd.html")
    else:
        hash_value = user[0]
    if check_password_hash(hash_value,password):
        session["username"] = username
        session["csrf_token"] = secrets.token_hex(16)
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
    sql = "SELECT a.id, a.description, b.username, a.minutes, d.description, c.description, a.salary_amount FROM chores a LEFT OUTER JOIN users b ON a.responsible_id = b.id LEFT OUTER JOIN categories c ON a.category_id = c.id LEFT OUTER JOIN statuses d ON a.status_id = d.id WHERE a.status_id = 1 ORDER BY id DESC"
    result = db.session.execute(sql)
    chores = result.fetchall()
    return render_template("homechores.html", chores=chores)

@app.route("/add_chore")
def add_chore():
    return render_template("new_chore.html")

@app.route("/new_chore", methods=["POST"])
def new_chore():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    kuvaus= request.form["kuvaus"]
    kesto = request.form["kesto"]
    kukapa = session["username"]
    sql = "SELECT id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":kukapa})
    kukapaid = result.fetchone()[0]
    sql2 = "INSERT INTO chores (description,responsible_id,minutes,status_id,category_id) VALUES (:description,:responsible_id,:minutes,:status_id,:category_id)"
    db.session.execute(sql2, {"description":kuvaus,"responsible_id":kukapaid,"minutes":kesto,"status_id":3,"category_id":3})
    db.session.commit()
    return redirect("/homechores")

@app.route("/forward_chore/<int:id>")
def chore(id):
    kukapa = session["username"]
    sql2 = "SELECT id FROM users WHERE username=:username"
    result2 = db.session.execute(sql2, {"username":kukapa})
    kukapaid = result2.fetchone()[0]
    sql3 = "SELECT role FROM users WHERE username=:username"
    result3 = db.session.execute(sql3, {"username":kukapa})
    role = result3.fetchone()[0]
    if role == 1:
        sql = "SELECT a.id, a.description, b.username, a.minutes, d.description, c.description FROM chores a LEFT OUTER JOIN users b ON a.responsible_id = b.id LEFT OUTER JOIN categories c ON a.category_id = c.id LEFT OUTER JOIN statuses d ON a.status_id = d.id WHERE a.id=:id"
        sql4 = "SELECT * FROM statuses"
    else:
        sql = "SELECT a.id, a.description, b.username, a.minutes, d.description, c.description FROM chores a LEFT OUTER JOIN users b ON a.responsible_id = b.id LEFT OUTER JOIN categories c ON a.category_id = c.id LEFT OUTER JOIN statuses d ON a.status_id = d.id WHERE a.id=:id AND a.status_id IN (1, 2, 3)"
        sql4 = "SELECT * FROM statuses WHERE value in (1, 2, 3)"
    result = db.session.execute(sql, {"id":id})
    content = result.fetchall()
    result4 = db.session.execute(sql4)
    statuses = result4.fetchall()
    return render_template("chore.html", id=id, content=content, statuses=statuses)

@app.route("/choose_chore/<int:id>")
def choose_chore(id):
    sql = "SELECT a.id, a.description, b.username, a.minutes, d.description, c.description FROM chores a LEFT OUTER JOIN users b ON a.responsible_id = b.id LEFT OUTER JOIN categories c ON a.category_id = c.id LEFT OUTER JOIN statuses d ON a.status_id = d.id WHERE a.id=:id"
    result = db.session.execute(sql, {"id":id})
    content = result.fetchall()
    sql2 = "SELECT * FROM statuses WHERE value in (2,3)"
    result2 = db.session.execute(sql2)
    statuses = result2.fetchall()
    return render_template("chore_tome.html", id=id, content=content, statuses=statuses)

@app.route("/update_chore", methods=["POST"])
def update_chore():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    id = request.form["id"]
    minutes = request.form["kesto"]
    status_id = request.form["status"]
    kukapa = session["username"]
    sql5 = "SELECT wage_id FROM users WHERE username=:username"
    result5 = db.session.execute(sql5, {"username":kukapa})
    wage_id = result5.fetchone()[0]
    sql6 = "SELECT hour_wage FROM wages WHERE id=:id"
    result6 = db.session.execute(sql6, {"id":wage_id})
    hour_wage = result6.fetchone()[0]
    if minutes in (None, "", ''):
        sql = "UPDATE chores SET status_id=:status_id WHERE id=:id"
        db.session.execute(sql, {"status_id":status_id,"id":id})
        db.session.commit()
    elif int(status_id)==5:
        sql = "UPDATE chores SET status_id=:status_id WHERE id=:id"
        db.session.execute(sql, {"status_id":status_id,"id":id})
        db.session.commit()
        sql2 = "UPDATE chores SET minutes=:minutes WHERE id=:id"
        db.session.execute(sql2, {"minutes":minutes,"id":id})
        db.session.commit()
        salary_amount = float(((float(hour_wage))/60)*float(minutes))
        sql3 = "UPDATE chores SET salary_amount=:salary_amount WHERE id=:id"
        db.session.execute(sql3, {"salary_amount":int(salary_amount),"id":id})
        db.session.commit()
    else:
        sql = "UPDATE chores SET status_id=:status_id WHERE id=:id"
        db.session.execute(sql, {"status_id":status_id,"id":id})
        db.session.commit()
        sql2 = "UPDATE chores SET minutes=:minutes WHERE id=:id"
        db.session.execute(sql2, {"minutes":minutes,"id":id})
        db.session.commit()
    return redirect("/homechores")

@app.route("/assign_chore", methods=["POST"])
def assign_chore():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    if request.form["status"] in (None, "", ''):
        if request.form["kesto"] in (None, "", ''):
            render_template("error.html")
        else:
            pass
    else:
        pass
    id = request.form["id"]
    kukapa = session["username"]
    kesto = request.form["kesto"]
    sql = "SELECT id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":kukapa})
    kukapaid = result.fetchone()[0]
    status_id = request.form["status"]
    if status_id in (None, "", ''):
        pass
    else:
        sql2 = "UPDATE chores SET status_id=:status_id WHERE id=:id"
        db.session.execute(sql2, {"status_id":status_id,"id":id})
        db.session.commit()
    sql3 = "UPDATE chores SET responsible_id=:responsible_id WHERE id=:id"
    db.session.execute(sql3, {"responsible_id":kukapaid,"id":id})
    db.session.commit()
    if kesto in (None, "", ''):
        pass
    else:
        sql4 = "UPDATE chores SET minutes=:minutes WHERE id=:id"
        db.session.execute(sql4, {"minutes":kesto,"id":id})
        db.session.commit()
    return redirect("/homechores")

@app.route("/add_chore_todo")
def add_chore_todo():
    sql = "SELECT * FROM categories"
    result = db.session.execute(sql)
    categories = result.fetchall()
    sql2 = "SELECT * FROM statuses WHERE value in (1, 2)"
    result2 = db.session.execute(sql2)
    statuses = result2.fetchall()
    return render_template("chore_todo.html", categories=categories, statuses=statuses)

@app.route("/new_undone_chore", methods=["POST"])
def new_undone_chore():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    kuvaus= request.form["kuvaus"]
    kesto = request.form["kesto"]
    luokka = request.form["luokka"]
    sql2 = "INSERT INTO chores (description,minutes,status_id,category_id) VALUES (:description,:minutes,:status_id,:category_id)"
    db.session.execute(sql2, {"description":kuvaus,"minutes":kesto,"status_id":1,"category_id":luokka})
    db.session.commit()
    return redirect("/homechores")

@app.route("/ongoing_chore")
def ongoing_chore():
    kukapa = session["username"]
    sql = "SELECT id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":kukapa})
    kukapaid = result.fetchone()[0]
    sql2 = "SELECT role FROM users WHERE username=:username"
    result = db.session.execute(sql2, {"username":kukapa})
    role = result.fetchone()[0]
    if role==1:
        sql3 = "SELECT a.id, a.description, b.username, a.minutes, d.description, c.description FROM chores a LEFT OUTER JOIN users b ON a.responsible_id = b.id LEFT OUTER JOIN categories c ON a.category_id = c.id LEFT OUTER JOIN statuses d on a.status_id = d.id WHERE status_id in (2,3,4) ORDER BY id DESC"
        result = db.session.execute(sql3)
    else:
        sql3 = "SELECT a.id, a.description,b.username, a.minutes, d.description, c.description FROM chores a LEFT OUTER JOIN users b ON a.responsible_id = b.id LEFT OUTER JOIN categories c ON a.category_id = c.id LEFT OUTER JOIN statuses d on a.status_id = d.id WHERE a.status_id in (2,3,4) AND a.responsible_id=:responsible_id ORDER BY a.id DESC"
        result = db.session.execute(sql3,{"responsible_id":kukapaid})
    chores = result.fetchall()
    return render_template("ongoing_homechores.html", chores=chores)

@app.route("/payed_chores")
def payed_chores():
    kukapa = session["username"]
    sql = "SELECT id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":kukapa})
    kukapaid = result.fetchone()[0]
    sql2 = "SELECT role FROM users WHERE username=:username"
    result = db.session.execute(sql2, {"username":kukapa})
    role = result.fetchone()[0]
    if role==1:
        sql3 = "SELECT a.id, a.description, b.username, a.minutes, d.description, c.description, a.salary_amount FROM chores a LEFT OUTER JOIN users b ON a.responsible_id = b.id LEFT OUTER JOIN categories c ON a.category_id = c.id LEFT OUTER JOIN statuses d on a.status_id = d.id WHERE status_id in (4,5) ORDER BY id DESC"
        result = db.session.execute(sql3)
    else:
        sql3 = "SELECT a.id, a.description,b.username, a.minutes, d.description, c.description, a.salary_amount FROM chores a LEFT OUTER JOIN users b ON a.responsible_id = b.id LEFT OUTER JOIN categories c ON a.category_id = c.id LEFT OUTER JOIN statuses d on a.status_id = d.id WHERE status_id in (4,5) AND a.responsible_id=:responsible_id ORDER BY id DESC"
        result = db.session.execute(sql3,{"responsible_id":kukapaid})
    chores = result.fetchall()
    return render_template("payed_chores.html", chores=chores)
