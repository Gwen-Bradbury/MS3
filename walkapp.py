import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_walks")
def get_walks():
    walks = list(mongo.db.walks.find())
    return render_template("walks.html", walks=walks)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if username already exists in DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Account Already Exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # Put the user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("mywalks", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if username already exists in DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for(
                    "mywalks", username=session["user"]))
            else:
                # Invalid password
                flash("Username and/or Password Incorrect")
                return redirect(url_for("login"))

        else:
            # Username doesn't exist
            flash("Username and/or Password Incorrect")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/mywalks/<username>", methods=["GET", "POST"])
def mywalks(username):
    # Get session users username from DB
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("mywalks.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # Remove user from session cookies
    flash("You've Been Logged Out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_walk", methods=["GET", "POST"])
def add_walk():
    if request.method == "POST":
        walk = {
            "park_name": request.form.get("park_name"),
            "walk_name": request.form.get("walk_name"),
            "walk_description": request.form.get("walk_description"),
            "walk_length": request.form.get("walk_length"),
            "created_by": session["user"]
        }
        mongo.db.walks.insert_one(walk)
        flash("Walk Successfully Added!")
        return redirect(url_for("get_walks"))
    parks = mongo.db.park.find().sort("park_name", 1)
    return render_template("add_walk.html", park=parks)


@app.route("/get_parks")
def get_parks():
    parks = list(mongo.db.parks.find().sort("park_name", 1))
    return render_template("parks.html", parks=parks)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
