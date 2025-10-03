from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/ejemplo1')
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route('/juego1')
def juego1():
    return render_template("juego1.html")

if __name__ == "__main__":
    app.run(debug=True)
