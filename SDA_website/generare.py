import os
import glob
from problem import Problem

import sys
import subprocess 
import re
import time
import timeout_decorator

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


if __name__ == '__main__':

    if(len(sys.argv) != 3):
        exit();

    GRUPA = str(sys.argv[1]) #numarul grupei
    p = subprocess.run(('python3.7 main.py '+str(sys.argv[2])).split(),capture_output=True, cwd=os.getcwd() + '/Lab' + str(GRUPA) +'/')
    
    (_, _, output) = p.stdout.decode('utf-8').partition('### Test SDA ###')
    # os.system("mv Lab/"+str(sys.argv[1])+"/*.png static/solutii/Lab"+str(sys.argv[1])+"/")
    (statements, _, solutions) = output.partition('Rezolvari:')
    (errors,_,statements) = statements.partition('Cerinte:')
    statements = statements.rstrip() # stergem spatiile de la final
    solutions = solutions.lstrip().rstrip() # stergem spatiile de la inceput si final

   
    path = "static/"
    folder_var = path + 'variante/'
    folder_sol = path + 'solutii/'
    
    
    #Errori
    with open("import_error"+GRUPA+".txt","a") as f:
                f.write(str(errors)+"\n");
                
                
    statements = statements.replace('\n','<br>');
    solutions = solutions.replace('\n','<br>');
    #Cerinte:
    with open(folder_var + 'Lab' + str(sys.argv[1]) + '/' + str(sys.argv[2]) + '.txt', 'w') as f:
        f.write(statements);
    
    #print('')

    #Rezolvari:
    with open(folder_sol + 'Lab' + str(sys.argv[1]) + '/' + str(sys.argv[2]) + '.txt', 'w') as f:
        f.write(solutions);
