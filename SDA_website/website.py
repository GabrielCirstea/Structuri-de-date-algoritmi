from flask import Flask,render_template, redirect, url_for, request, make_response

app = Flask(__name__)

import subprocess 
import shutil

@app.route('/')
def grupe():
    return render_template('grupe.html')

@app.route('/<int:grupa>')
def index(grupa):
    # print(grupa);
    return render_template('index.html',grupa = grupa)

#salvare problema github
import os
import importlib

@app.route('/index/get_github/<int:GRUPA>')
def github(GRUPA):
    # delete old repo
    shutil.rmtree('Lab' + str(GRUPA))

    # clone current repo
    subprocess.call(('git clone https://github.com/AdminSDA/Lab' + str(GRUPA)  + '.git').split())
    return "Okay. <a href='/'>Back</a>"
           

#se introduce nr variantei in url
@app.route('/<int:grupa>/<int:number>')
# @app.route('/index/<int:number>')
def varianta(grupa,number):
    
    #filename = os.path.join(app.instance_path, 'files', 'var'+ str(number) +'.txt')
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/variante/Lab' + str(grupa)+'/',str(number)+'.txt')
    try:
        f = open(path)
        content = f.readlines()
    except:
        content = ["<center>Fisierul nu a fost gasit",":(</center>"]
    return render_template('Varianta.html',title = 'Varianta '+str(number),number = number,content = content, grupa = grupa)
    
#solutia variantei number
@app.route('/<int:grupa>/<int:number>/sol')
# @app.route('/index/<int:number>/sol')
def solutie(grupa,number):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/solutii/Lab' + str(grupa)+'/',str(number)+'.txt')
    try:
        f = open(path)
        content = f.readlines()
    except:
        content = ["<center>Fisierul nu a fost gasit",":(</center>"]
    return render_template('Solutie.html',title = 'Solutia '+str(number),number = number,content = content,grupa = grupa)
    
import random
@app.route('/<int:grupa>/random')
# @app.route('/index/random')
def random_page(grupa):
    nr_var = random.randint(1,100)
    resp = make_response(varianta(grupa,nr_var))
    resp.set_cookie('var',str(nr_var))
    return resp
    
@app.route('/<int:grupa>/random/sol')
# @app.route('/index/random/sol')
def random_page_sol(grupa):
    nr_var = request.cookies.get('var')
    return solutie(grupa,nr_var)

@app.route('/index/generare/<int:GRUPA>')
def generare(GRUPA):
    #path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'static/')
    for i in range(1,101):
        os.system('python3 generare.py '+ str(GRUPA) + ' ' + str(i))
    return redirect(url_for('grupe'))
    
if __name__ == "__main__":
    app.run(debug=True)