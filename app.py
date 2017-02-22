
from flask import Flask, render_template

app = Flask("webapp")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/info")
def info():
    return render_template("info.html")

if __name__ == "__main__":
    app.run()
