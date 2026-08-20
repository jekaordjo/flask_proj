import os

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

from core.models import db
from views.shifts import shifts_app

load_dotenv()

app = Flask(__name__)
# python -c 'import secrets; print(secrets.token_hex())'
app.config.update(
    SECRET_KEY=os.environ.get("SECRET_KEY", "local-dev-key-12345"),
    # after adding .env the key was regenerated
    SQLALCHEMY_DATABASE_URI=os.environ.get(
        "SQLALCHEMY_DATABASE_URI", "sqlite:///app.db"
    ),
)

app.register_blueprint(shifts_app, url_prefix="/shifts")

csrf = CSRFProtect(app)
db.init_app(app)
migrate = Migrate(app, db)


@app.get("/", endpoint="index")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    debug_mode = os.environ.get("FLASK_DEBUG", "False").lower() in ("true", "1", "yes")
    app.run(debug=debug_mode)
