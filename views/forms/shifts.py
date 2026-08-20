from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, InputRequired, NumberRange


class ShiftForm(FlaskForm):
    year = IntegerField(
        "Год начала работы",
        validators=[
            InputRequired(message="Укажите год"),
            NumberRange(min=1, message="Не может быть отрицательным"),
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "0",
        },
    )

    day = IntegerField(
        "День начала работы",
        validators=[
            InputRequired(message="Укажите номер дня"),
            NumberRange(min=1, max=31, message="Должен быть от 1 до 31"),
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "0",
        },
    )

    month = IntegerField(
        "Месяц начала работы",
        validators=[
            InputRequired(message="Укажите номер месяц"),
            NumberRange(min=1, max=12, message="Должен быть от 1 до 12"),
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "0",
        },
    )

    type_shift_start = SelectField(
        "Тип смены",
        validators=[DataRequired(message="Введите тип смены")],
        choices=["дневная", "ночная"],
        render_kw={
            "class": "form-control",
            "placeholder": "Например: дневная",
        },
    )

    submit = SubmitField(
        "Сохранить",
        render_kw={"class": "btn btn-primary w-100"},
    )
