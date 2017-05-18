from flask import Flask, render_template, request

app = Flask("webapp")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/info/<username>")
def info(username):
    return render_template("info.html", username=username)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        page = "Name: {}, Mail: {}, Message: {}".format(
            request.form["user_name"],
            request.form["user_mail"],
            request.form["user_message"]
            )
        return page
    else:
        return render_template("contact.html")

if __name__ == "__main__":
    app.run("0.0.0.0")
