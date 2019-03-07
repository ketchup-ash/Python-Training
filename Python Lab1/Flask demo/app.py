from flask import Flask, render_template, request
from database import Database
import os

app = Flask(__name__)  

@app.route('/index')   
def index():      
    data = list(range(0,100, 2))
    return render_template('index.html', numbers = data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/', methods = ['GET', 'POST'])
def expense():
    msg = ""
    if request.method == "POST":
        db = Database()
        db.create_table()
        name = request.form.get('item')
        price = request.form.get('price')
        status = db.add(name, price)
        if status:
            msg = "Saved successfully"
        else:
            msg = "Error saving data"
        db.view()
    return render_template('expense.html')

if __name__ == "__main__":
    app.run(debug = True) 