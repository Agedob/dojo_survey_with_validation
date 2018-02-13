from flask import Flask, render_template, request, redirect, session , flash
import random
app = Flask(__name__)
app.secret_key = "notthekey"

@app.route('/')
def index():    
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def redirect_process():
    abc = request.form['name']
    abcd = request.form['location']
    abcde = request.form['lang']
    abcdef = request.form['updown']
    if len(abc) < 1 or len(abcd) < 1 or len(abcde) < 1 or len(abcdef) < 1 and len(abcdef) < 120:
        flash("please fillout form")
        return redirect('/')
    else:
        print "that was easy enough"
        return render_template("/process.html", name = abc, location = abcd, lang = abcde, updown = abcdef)

   
app.run(debug=True)