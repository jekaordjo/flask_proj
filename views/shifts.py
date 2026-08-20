from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    url_for,
)

from views.forms.shifts import ShiftForm

shifts_app = Blueprint("shifts_app", __name__)


@shifts_app.get("/", endpoint="shifts")
def index():
    return render_template("shifts/index.html")


@shifts_app.route("/add", methods=["GET", "POST"], endpoint="add_shift")
def add_shift():
    form = ShiftForm()
    if request.method == "GET":
        return render_template("shifts/add.html", form=form)
    if not form.validate_on_submit():
        return render_template("shifts/add.html", form=form), 400
    return redirect(url_for("shifts_app.shifts"))
