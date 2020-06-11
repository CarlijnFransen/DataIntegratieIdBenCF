from flask import Flask, render_template, request
from werkzeug import secure_filename
import search_db.py
app = Flask(__name__)


@app.route("/", endpoint='func1')
def func1():
    return render_template('home.html')


@app.route("/results", methods=['POST'], endpoint='func2')
def func2():
    return render_template('results.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        search_db.main()
    return 'file uploaded successfully'


#if __name__ == "__main__":
    #app.run()
