from flask import Flask,render_template, redirect, url_for, request, make_response, flash
import urllib.request
from werkzeug.utils import secure_filename

from config import Config
app = Flask(__name__)
app.config.from_object(Config)

UPLOAD_FOLDER = "uploads";
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024 #max file size = 2 MB

import subprocess 
import shutil

ALLOWED_EXTENSIONS = set(['py'])
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def grupe():
    return render_template('grupe.html')

from verificare import Verificare

@app.route('/<int:grupa>',methods=['GET','POST'])
def index(grupa):
    # print(grupa);
    
    #UPLOAD
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'] +'/'+ str(grupa), filename))
            # flash('File successfully uploaded')
            flash(str(Verificare(file.filename,grupa)));
            return redirect('/'+str(grupa))
        else:
            flash('Allowed file types is py')
            return redirect(request.url)
    #/UPLOAD
    
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'import_error'+str(grupa)+'.txt')
    try:
        f = open(path)
        content = f.readlines()
    except:
        content = ["Totul bine pana acum!",":)"]
    return render_template('index.html',grupa = grupa,content=content)

#salvare problema github
import os
import importlib

@app.route('/index/get_github/<int:GRUPA>')
def github(GRUPA):
    # delete old repo
    try:
        shutil.rmtree('Lab' + str(GRUPA))
    except:
        pass;

    # clone current repo
    subprocess.call(('git clone https://github.com/AdminSDA/Lab' + str(GRUPA)  + '.git').split())
    #Stergere exeple
    try:
        os.remove('Lab'+str(GRUPA)+'/problem_test1.py')
        os.remove('Lab'+str(GRUPA)+'/problem_test2.py')
        os.remove('Lab'+str(GRUPA)+'/main.py')
        os.remove('Lab'+str(GRUPA)+'/problem.py')
    except Exception as e:
        print(e);
    for module in os.listdir('uploads/'+str(GRUPA)+'/.'):
        if module[-3:] == '.py':
            shutil.copyfile("uploads/"+str(GRUPA)+"/"+module,"Lab"+str(GRUPA)+"/"+module);
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
        try:
            os.remove('import_error'+str(GRUPA)+'.txt')
        except:
            pass;
        os.system('python3 generare.py '+ str(GRUPA) + ' ' + str(i))
    return redirect(url_for('grupe'))
    
if __name__ == "__main__":
    app.run(debug=True)