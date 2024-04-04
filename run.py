import os
import json
from flask import Flask, render_template


app = Flask (__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/benefits.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", benefit=data)


    @app.route("/about/<benefits_name>")
    def about_avail(avail.name):
        avail = {}
        with open("data/benefits.json", "r") as json_data:
            data = json.load(json_data)
            for obj in data:
                if obj["url"] == avail_name:
                    avail = obj
        return render_template("avail.html", avail=avail)


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=False)
