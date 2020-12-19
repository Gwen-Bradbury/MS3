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


# Get Walks and Parks
@app.route("/")
@app.route("/get_walks_parks")
def get_walks_parks():
    park = list(mongo.db.park.find().sort("park_name", 1))
    walks = list(mongo.db.walks.find().sort("walk_name", 1))
    return render_template("walks.html", walks=walks, park=park)


# search Bar
@app.route("/search", methods=["GET", "POST"])
def search():
    search = request.form.get("search")
    walks = list(mongo.db.walks.find({"$text": {"$search": search}}))
    return render_template("walks.html", walks=walks)


# Register Account
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


# Log In
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


# Get Users Username
@app.route("/mywalks/<username>", methods=["GET", "POST"])
def mywalks(username):
    # Get walks from DB
    walks = list(mongo.db.walks.find())
    # Get session users username from DB
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        return render_template("mywalks.html", username=username, walks=walks)

    return redirect(url_for("login"))


# Log Out
@app.route("/logout")
def logout():
    # Remove user from session cookies
    flash("You've Been Logged Out")
    session.pop("user")
    return redirect(url_for("login"))


# Add Walk to DB
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
        return redirect(url_for("get_walks_parks"))

    park = mongo.db.park.find().sort("park_name", 1)
    return render_template("add_walk.html", park=park)


# Edit Walks
@app.route("/edit_walks/<walk_id>", methods=["GET", "POST"])
def edit_walks(walk_id):
    if request.method == "POST":
        submit = {
            "park_name": request.form.get("park_name"),
            "walk_name": request.form.get("walk_name"),
            "walk_description": request.form.get("walk_description"),
            "walk_length": request.form.get("walk_length"),
            "created_by": session["user"]
        }
        mongo.db.walks.update({"_id": ObjectId(walk_id)}, submit)
        flash("Walk Successfully Updated!")
        return redirect(url_for("get_walks_parks"))
    walk = mongo.db.walks.find_one({"_id": ObjectId(walk_id)})
    park = mongo.db.park.find().sort("park_name", 1)
    return render_template("edit_walk.html", walk=walk, park=park)


# Delete Walks
@app.route("/delete_walks/<walk_id>")
def delete_walks(walk_id):
    mongo.db.walks.remove({"_id": ObjectId(walk_id)})
    flash("Walk Successfully Deleted!")
    return redirect(url_for("get_walks_parks"))


# Get Parks
@app.route("/get_park")
def get_park():
    park = list(mongo.db.park.find().sort("park_name", 1))
    return render_template("parks.html", park=park)


# Add Park to DB
@app.route("/add_park", methods=["GET", "POST"])
def add_park():
    if request.method == "POST":
        park = {
            "park_name": request.form.get("park_name"),
            "park_image": request.form.get("park_image"),
            "park_description": request.form.get("park_description")
        }
        mongo.db.park.insert_one(park)
        flash("Park Successfully Added!")
        return redirect(url_for("get_park"))

    return render_template("parks.html")


# Edit Parks
@app.route("/edit_park/<park_id>", methods=["GET", "POST"])
def edit_park(park_id):
    if request.method == "POST":
        submit = {
            "park_name": request.form.get("park_name"),
            "park_image": request.form.get("park_image"),
            "park_description": request.form.get("park_description")
        }
        mongo.db.park.update({"_id": ObjectId(park_id)}, submit)
        flash("Park Successfully Updated!")
        return redirect(url_for("get_park"))
    park = mongo.db.park.find_one({"_id": ObjectId(park_id)})
    return render_template("edit_park.html", park=park)


# Delete Parks
@app.route("/delete_park/<park_id>")
def delete_park(park_id):
    mongo.db.park.remove({"_id": ObjectId(park_id)})
    flash("Park Successfully Deleted!")
    return redirect(url_for("get_park"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
