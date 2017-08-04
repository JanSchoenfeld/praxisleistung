import os
import io
from flask import Flask, url_for, request, render_template

def create_app():
    app = Flask(__name__)
    return app

app = create_app()


# Root URL, 127.0.0.1:5000/
# Offers interface to change working directory and view files.
@app.route("/")
def start():
    cwd = os.getcwd()
    return render_template("index.html", cwd = cwd)


# Method to change the current working directory if specified, or go up into the parent directory
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


#Method to list the content (directories, files) of the specified path using an extended index.html
@app.route("/content")
def content():
    cwd = os.getcwd()
    files = next(os.walk(cwd))[2]
    files_unicode = [i.decode('UTF-8', 'replace') if isinstance(i, basestring) else i for i in files]
    directories = next(os.walk(cwd))[1]
    directories_unicode = [i.decode('UTF-8', 'replace') if isinstance(i, basestring) else i for i in directories]
    return render_template("index_files.html", cwd = cwd, files = files_unicode, directories = directories_unicode)


#Method to open a file and show its content on an extended index.html
#TODO: Keep file formatting for easier readability
@app.route("/open", methods = ["POST", "GET"])
def read_file():
    filename = request.form['filepath']
    cwd = os.getcwd()
    file_data = io.open(cwd + '/' + filename, 'r', encoding = 'utf-8', errors = 'replace').readlines()
    file_data = [line.strip() for line in file_data]
    return render_template("index_open.html", open_file = file_data, cwd = cwd, filename = filename)


@app.route('/search', methods =['POST', 'GET'])
def search_files():
    cwd = os.getcwd()
    resultlist = list()
    search_string = request.form['search_string']
    txtlist = find_txt()
    for file in txtlist:
        if search_string in io.open(file, 'r', encoding = 'utf-8', errors = 'replace').read():
            resultlist.append(file)
    return render_template("search.html", resultlist = resultlist, search_string = search_string, cwd = cwd)


def find_txt():
    txtlist = list()
    for file in os.listdir(os.getcwd()):
        if file.endswith(".txt"):
            txtlist.append(file)
    return txtlist

if __name__ == "__main__":
    app.run(debug = True)
