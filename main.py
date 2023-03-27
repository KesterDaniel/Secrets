from flask import Flask, render_template
import os
from dotenv import load_dotenv
from forms import LoginForm

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("MY_SECRET_KEY")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("login.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
