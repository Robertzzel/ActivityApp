from flask import Flask,render_template,url_for
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/activity")
def activity():
    return render_template('activity.html')

@app.route("/activity/carti")
def cartiActivity():
    return render_template('cartiActivity.html')
