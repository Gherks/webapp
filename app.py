from flask import Flask, render_template

app = Flask("webapp")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/info/<username>")
def info(username):
    return render_template("info.html", username=username)


@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run("0.0.0.0")
