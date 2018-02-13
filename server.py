from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
@app.route('/')
def index():    
    return render_template("index.html")

@app.route('/proccess', methods=['POST'])
def redirect_process():
    abc = request.form['name']
    abcd = request.form['location']
    abcde = request.form['lang']
    abcdef = request.form['updown']
    return render_template("/proccess.html", name = abc, location = abcd, lang = abcde, updown = abcdef)

   
app.run(debug=True)