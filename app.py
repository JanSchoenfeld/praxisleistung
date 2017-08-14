import os, io, magic, gzip, codecs
from flask import Flask, url_for, request, render_template

app = Flask(__name__)

# Root URL, 127.0.0.1:5000/
# Offers interface to change working directory and view files.
@app.route("/")
def start():
    cwd = os.getcwd()
    return render_template("index.html", cwd=cwd)


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
    return render_template("index.html", cwd=cwd)


# Method to list the content (directories, files) of the specified path using an extended index.html
@app.route("/content")
def content():
    cwd = os.getcwd()
    files = next(os.walk(cwd))[2]
    files_unicode = [i.decode('UTF-8', 'replace') if isinstance(i, basestring) else i for i in files]
    directories = next(os.walk(cwd))[1]
    directories_unicode = [i.decode('UTF-8', 'replace') if isinstance(i, basestring) else i for i in directories]
    return render_template("index_files.html", cwd=cwd, files=files_unicode, directories=directories_unicode)


# Method to open a file and show its content on an extended index.html
@app.route("/open", methods = ["POST", "GET"])
def read_file():
    filename = request.form['filepath']
    cwd = os.getcwd()
    if filename.endswith('.gz'):
        file_data = codecs.getreader('utf-8')(gzip.open(filename), errors='replace')
    else:
        file_data = codecs.getreader('utf-8')(open(filename), errors='replace')
    return render_template("index_open.html", open_file=file_data, cwd=cwd, filename=filename)


# Method to serch for a string in a directories .txt files
@app.route('/search', methods =['POST', 'GET'])
def search_files():
    cwd = os.getcwd()
    resultlist = list()
    search_string = request.form['search_string']
    txtlist = find_txt()
    for file in txtlist:
        if file.endswith('.gz'):
            zipped_content = codecs.getreader('utf-8')(gzip.open(file), errors='replace')
            file_content = zipped_content.read()
            zipped_content.close()
            if search_string in file_content:
                resultlist.append(file)
        else:
            if search_string in io.open(file, 'r', encoding='utf-8', errors='replace').read():
                resultlist.append(file)
    return render_template("search.html", resultlist=resultlist, search_string=search_string, cwd=cwd)


# Method to find all .txt files in a directory
def find_txt():
    txtlist = list()
    files = next(os.walk(os.getcwd()))[2]
    mime = magic.Magic(mime=True)
    for file in files:
        if mime.from_file(file) == 'text/plain':
            	txtlist.append(file)
	elif mime.from_file(file) == 'application/gzip':
		txtlist.append(file)
	elif mime.from_file(file) == 'text/x-python':
		txtlist.append(file)
    return txtlist



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
