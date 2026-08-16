from flask import Blueprint, render_template

shifts_app = Blueprint("shifts_app", __name__)


@shifts_app.get("/", endpoint="shifts")
def index():
    return render_template("shifts/index.html")
