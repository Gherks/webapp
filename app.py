from flask import Flask, render_template, redirect, url_for
from forms import MyForm
from database import db, Contact

app = Flask("webapp")
app.config["WTF_CSRF_ENABLED"] = False


@app.before_request
def before_request():
    db.connect()


@app.after_request
def after_request(response):
    db.close()
    return response


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/info/<username>")
def info(username):
    return render_template("info.html", username=username)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = MyForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        miscellaneous = form.miscellaneous.data
        Contact.create(first_name=first_name, last_name=last_name, miscellaneous=miscellaneous)
        return redirect(url_for('contact'))
    else:
        return render_template("contact.html", form=form)


@app.route("/show_db", methods=["GET"])
def show_db():
    entries = Contact.select()
    return render_template("show_db.html", entries=entries)


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
