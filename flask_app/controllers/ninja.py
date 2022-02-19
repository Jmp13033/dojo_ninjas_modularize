from flask_app import app
from flask import render_template, sessions, redirect, request
from flask_app.controllers.dojo import Dojo # lower cased 
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja

@app.route("/ninjas")
def add():
    return render_template("new_ninjas.html")


# starting here to work on my ninja

@app.route("/creating_ninja", methods=["POST"])
def create(): 
    Ninja.save(request.form)
    return redirect("/create_ninja") # changed here here


@app.route("/create_ninja")
def new_ninja():
    dojos_list = Dojo.all_dojos()
    return render_template("new_ninjas.html", dojos = dojos_list)