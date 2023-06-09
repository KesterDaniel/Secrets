from flask import Flask, render_template
import os
from dotenv import load_dotenv
from forms import LoginForm
from flask_bootstrap import Bootstrap

load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("MY_SECRET_KEY")

bootstrap = Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
