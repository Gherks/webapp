from flask import Flask, render_template, redirect, session, url_for
from forms import ContactForm, LoginForm
from database import db, Contact

import os

app = Flask("webapp")
app.config["WTF_CSRF_ENABLED"] = False
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "insecure dev key")

@app.before_request
def before_request():
    db.connect()


@app.after_request
def after_request(response):
    db.close()
    return response


@app.route("/")
def home():
    visits = int(session.get("number_of_visits", 0))
    visits += 1
    session["number_of_visits"] = visits
    welcome_message = ""
    if visits == 1:
        welcome_message = "This is your first visit!"
    else:
        welcome_message = "You have visited this site {} times.".format(visits)
    return render_template("index.html", welcome_message=welcome_message)


@app.route("/info/<username>")
def info(username):
    return render_template("info.html", username=username)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        miscellaneous = form.miscellaneous.data
        Contact.create(first_name=first_name, last_name=last_name, miscellaneous=miscellaneous)
        return redirect(url_for('show_db'))
    else:
        return render_template("contact.html", form=form)


@app.route("/show_db", methods=["GET"])
def show_db():
    entries = Contact.select()
    return render_template("show_db.html", entries=entries)

@app.route("/secrets", methods=["GET"])
def secrets():
    print("TRYING TO ENTER SECRETS")
    if "logged_in" in session.keys():
        print("KEY EXISTS")
        if session["logged_in"] == 1:
            print("SUCCESSFULLY LOGGED IN!")
            return render_template("secrets.html")
    return redirect(url_for('login'))

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.password.data == "asd":
            session["logged_in"] = 1
            return redirect(url_for('secrets'))
    return render_template("login.html", form=form)
    
@app.route("/logout", methods=["GET"])
def logout():
    session["logged_in"] = 0
    return login()


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
