from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route("/")
@app.route('/index')
def hello_world():
    return render_template('index.html')

@app.route('/aboutme')
def about_me():
	return render_template('aboutMe.html')

if __name__=="__main__":
	app.run(host='0.0.0.0', port=5000)

