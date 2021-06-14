from flask import Blueprint, render_template, flash, redirect, url_for, request

second = Blueprint("home",__name__,template_folder="templates",url_prefix='/home')


@second.route("/")
def index():
    return render_template("index.html")