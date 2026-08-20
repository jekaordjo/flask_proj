from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from sqlalchemy.exc import DatabaseError, IntegrityError
from werkzeug.exceptions import BadRequest, InternalServerError, NotFound

from core.models.database import db
from core.models.shift import Shift
from views.forms.shifts import ShiftForm

shifts_app = Blueprint("shifts_app", __name__)


@shifts_app.get("/", endpoint="shifts")
def index():
    shifts = Shift.query.order_by(Shift.id).all()
    return render_template("shifts/index.html", shifts=shifts)


@shifts_app.route("/add", methods=["GET", "POST"], endpoint="add_shift")
def add_shift():
    form = ShiftForm()
    if request.method == "GET":
        return render_template("shifts/add.html", form=form)
    if not form.validate_on_submit():
        return render_template("shifts/add.html", form=form), 400

    shift_year = form.year.data
    shift_day = form.day.data
    shift_month = form.month.data
    shift_type_shift_start = form.type_shift_start.data

    shift = Shift(
        year=shift_year,
        day=shift_day,
        month=shift_month,
        type_shift_start=shift_type_shift_start,
    )
    db.session.add(shift)
    try:
        db.session.commit()
    except IntegrityError:
        raise BadRequest(f"Not save shift {shift_year!r} not unique")
    except DatabaseError:
        raise InternalServerError("internal error")

    flash(f"График «{form.year.data}» добавлен!", "success")

    return redirect(url_for("shifts_app.shifts"))
