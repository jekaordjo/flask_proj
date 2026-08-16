from flask import Flask, render_template
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

from core.models import db
from views.shifts import shifts_app

app = Flask(__name__)
# python -c 'import secrets; print(secrets.token_hex())'
app.config.update(
    SECRET_KEY="93d0bcf0bce0df9d694c958566690c66df71b8ffbb3aa591ce87c0df099275d5",
    SQLALCHEMY_DATABASE_URI="sqlite:///app.db",
)

app.register_blueprint(shifts_app, url_prefix="/shifts")

csrf = CSRFProtect(app)
db.init_app(app)
migrate = Migrate(app, db)


@app.get("/", endpoint="index")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
