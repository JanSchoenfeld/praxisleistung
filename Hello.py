import os
import io
from flask import Flask, url_for, request, render_template
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
    filepath = request.form['path']
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
    files_unicode = [i.decode('UTF-8') if isinstance(i, basestring) else i for i in files]
    directories = next(os.walk(cwd))[1]
    directories_unicode = [i.decode('UTF-8') if isinstance(i, basestring) else i for i in directories]
    return render_template("index_files.html", cwd = cwd, files = files_unicode, directories = directories_unicode)

@app.route("/open", methods = ["POST", "GET"])
def read_file():
    filename = request.form['filepath']
    cwd = os.getcwd()
    file_data = io.open(cwd + '/' + filename, 'r', encoding = 'utf-8').readlines()
    file_data = [line.strip() for line in file_data]
    return render_template("index_open.html", open_file = file_data, cwd = cwd, filename = filename)


if __name__ == "__main__":
    app.run(debug = True)
