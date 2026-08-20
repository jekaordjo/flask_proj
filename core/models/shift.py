from sqlalchemy import Column, Integer, String

from .database import db


class Shift(db.Model):
    id = Column(
        Integer,
        primary_key=True,
    )

    year = Column(
        Integer,
        nullable=False,
    )

    day = Column(
        Integer,
        nullable=False,
    )

    month = Column(
        Integer,
        nullable=False,
    )

    type_shift_start = Column(
        String,
        nullable=False,
    )
