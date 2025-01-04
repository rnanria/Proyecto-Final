from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/info")
def info():
    return render_template('info.html')


app.run(debug=True)
