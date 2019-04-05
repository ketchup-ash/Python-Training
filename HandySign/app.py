from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    data = list(range(0, 100, 2))
    return render_template('index.html', numbers = data)

if __name__ == "__main__":
    app.run(debug = True)