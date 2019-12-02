import os
import glob
from problem import Problem
from shutil import copyfile
import subprocess

import sys


def numere(nume):
# ''' Returneaza numarul problemui.  CONDITIE: Numarul problemei sa fie scris la sfarsit ''' 
    for i in range(len(nume)-1,0,-1):
        try:
            nr = int(nume[i:]);
        except:
            if i == len(nume)-1:
                return None;
            else:
                return int(nume[i+1:])
        #nu ar trebui sa ajunga aici
    return None;
    
  
def Verificare(module,grupa):
    try:
        __import__('uploads.'+str(grupa)+'.'+  module[:-3], locals(), globals())
    except Exception as e:
        os.remove("uploads/"+str(grupa)+"/"+module)
        return e;
    for derived in Problem.__subclasses__():
        try:
            p = derived()

            statement = str(p.statement)

            solution = p.solve()
        except Exception as e:
                # solution +='<code>Probleme la rulare</code>'
                print(e);
                os.remove("uploads/"+str(grupa)+"/"+module)
                return e;
    #Sa urcam pe github
    # os.system("python3 git_clone.py");
    os.system("cd Lab"+str(grupa)+" && git pull");
    subprocess.run('git fetch --all'.split(), cwd=os.getcwd() + '/Lab' + str(grupa))
    subprocess.run('git reset --hard origin'.split(), cwd=os.getcwd() + '/Lab' + str(grupa))
    copyfile("uploads/"+str(grupa)+"/"+module,"Lab"+str(grupa)+"/"+module);
    #asta ramane pt cand fac cont pe github
    os.system("cd Lab"+str(grupa)+" && git add "+module);
    os.system('cd Lab'+str(grupa)+' && git commit -m "Added '+module+'"');
    os.system('cd Lab'+str(grupa)+' && git push -u origin');
    return "Totul bine";
