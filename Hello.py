import os
from flask.json import jsonify
from flask import Flask, redirect, url_for, request, render_template, Markup
from flask_bootstrap import Bootstrap

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app

app = create_app()

@app.route("/")
def start():
    cwd = os.getcwd()
    return render_template("index.html", cwd = cwd)


@app.route("/", methods = ["POST", "GET"])
def browse_path():
    filepath = request.form['filepath']
    if filepath == "":
        os.chdir("..")
        cwd = os.getcwd()
    else:
        os.chdir(filepath)
        cwd = os.getcwd()
    return render_template("index.html", cwd = cwd)

@app.route("/content")
def content():
    cwd = os.getcwd()
    files = next(os.walk(cwd))[2]
    directories = next(os.walk(cwd))[1]
    return render_template("index_files.html", cwd = cwd, files = files, directories = directories)

if __name__ == "__main__":
    app.run(debug = True)
