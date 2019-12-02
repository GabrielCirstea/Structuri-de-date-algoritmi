#script pt clonarea repozitorului de git
#facut pt rulare automata

import subprocess 
import shutil
import os

def github(GRUPA):
    # delete old repo
    try:
        shutil.rmtree('Lab' + str(GRUPA))
    except:
        pass;
        
    # clone current repo
    subprocess.call(('git clone git@github.com:AdminSDA/Lab' + str(GRUPA)  + '.git').split())
    try:
        os.remove('Lab'+str(GRUPA)+'/problem_test1.py')
        os.remove('Lab'+str(GRUPA)+'/problem_test2.py')
    except Exception as e:
        print(e);
    #recopiere in folder, pana reusim sa dam push pe github
    # ~ for module in os.listdir('uploads/'+str(GRUPA)+'/.'):
        # ~ if module[-3:] == '.py':
            # ~ shutil.copyfile("uploads/"+str(GRUPA)+"/"+module,"Lab"+str(GRUPA)+"/"+module);
	shutil.copyfile("main_github.py","Lab"+str(GRUPA)+"/main.py")

github(211);
github(212);
