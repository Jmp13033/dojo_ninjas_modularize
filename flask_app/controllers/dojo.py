from flask_app import app
from flask import render_template, sessions, redirect, request

from flask_app.models.dojos import Dojo 
from flask_app.models.ninjas import Ninja

@app.route("/")
def index():
    return redirect("/dojo")

@app.route("/dojo")
def dojo():
    return render_template("dojos.html", dojo_list= Dojo.all_dojos()) # this is what we pass through to return the list


@app.route("/dojo/show/<int:id>")
def show(id):
    data = {
        "id": id

    }
    
    dojo = Dojo.get_one(data)
    dojo_ninjas = Ninja.get_dojo_ninjas(data)
    print(dojo_ninjas)
    return render_template("show.html", dojo = dojo , dojo_ninjas = dojo_ninjas)
    


@app.route("/create_dojo", methods = ["POST"])
def create_dojo():
    data = {
        "name": request.form["name"]

    }
    Dojo.create_dojo(data)
    return redirect("/")

