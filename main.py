from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect

from views.shifts import shifts_app

app = Flask(__name__)

app.register_blueprint(shifts_app, url_prefix="/shifts")

csrf = CSRFProtect(app)


@app.get("/", endpoint="index")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
