import os
import sys
import glob
from problem import Problem
import timeout_decorator
import shutil

@timeout_decorator.timeout(2)
def executare(derived,statements,solutions,errors):
    try:
        p = derived();
        statement = str(derived.__name__);
        statement+="\n";
        nrPicturesStatement = 0;
        try:
            nrPicturesStatement = p.statementPicture;
        except:
            nrPicturesStatement = 0;
        try:
            imgNames = []
            if(getattr(p,"ImgName") !=  AttributeError):
                for imgName in p.ImgName:       #pt fiecare denumire de imagine
                    (name,token,extention) = imgName.partition('.');
                    name+=str(derived.__name__)+"Var"+str(sys.argv[1]);
                    imgNames.append(name+token+extention);     # adaugam VarX, X e nr
                del p.ImgName;
                p.ImgName = imgNames;
        except:
            pass;
        
        statement += str(p)
        
        solution = str(derived.__name__);
        solution +="\n";
        
        solution += p.solve()
        
        try:
            if(getattr(p,"ImgName") !=  AttributeError):
                for imgName in p.ImgName:
                    # get the group number
                    here = os.getcwd();
                    grupa = here[-3:]
                    # adaugam link in fisier
                    if(nrPicturesStatement > 0):
                        statement += "<img src=\"/static/solutii/Lab"+str(grupa)+"/"+imgName+"\">";
                        nrPicturesStatement-=1;
                    else:
                        solution+="<img src=\"/static/solutii/Lab"+str(grupa)+"/"+imgName+"\">";
                    # mutam imaginea in folderul cu rezolvari
                    shutil.move(imgName,"../static/solutii/Lab"+str(grupa)+"/"+imgName);
        except:
            pass;
        
        statements.append(statement)
        solutions.append(solution)
        print(statement);
    except Exception as e:
            # solution +='<code>Probleme la rulare</code>'
            print(e);
            errors.append('Eroare la ' + derived.__name__ + " " + str(e) + "\n")

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
        # nu ar trebui sa ajunga aici
    return None;

if __name__ == '__main__':
    errors = []

    # List all classes in this directory and
    # import all that are derived from Problem
    for module in os.listdir('.'):
        if module[-3:] == '.py':
            try:
                __import__(module[:-3], locals(), globals())
            except Exception as e:
                errors.append('Eroare la import modul: ' + module + "\n")

    # For each subclass generate a statement and 
    # the detailed solution for that statement
    statements = []
    solutions = []

    # for derived in Problem.__subclasses__():
        # try:
            # p = derived()
            # statement = '<h4>' + type(p).__name__ + '</h4><pre>' + str(p) + '</pre>'
            # solution = '<h4>' + type(p).__name__ + '</h4><pre>' + p.solve() + '</pre>'

            # statements.append((int(type(p).__name__[7:]), statement))
            # solutions.append((int(type(p).__name__[7:]), solution))
        # except Exception as e:
            # errors.append('Eroare la ' + type(p).__name__ + " " + str(e) + "\n")

    for derived in Problem.__subclasses__():
        executare(derived,statements,solutions,errors);
        
        
    
    #sortam statement-urile si solutiile in functie de numarul problemei
    statements = sorted(statements, key=lambda st: numere(st.split('\n',1)[0]))
    solutions = sorted(solutions, key=lambda st: numere(st.split('\n',1)[0]))

    print('### Test SDA ###')
    print('Erori:')
    nr = 0
    for error in errors:
        print(error)
        print('')
        nr+=1

    print('Cerinte:')
    nr = 0
    for statement in statements:
        print('<pre id="'+str(nr)+'" onclick="afisare('+str(nr)+')">\n')
        print(statement)
        print('</pre>')
        nr+=1
        
    print('Rezolvari:')
    nr = 0
    for solution in solutions:
        print('<pre id="'+str(nr)+'" onclick="afisare('+str(nr)+')">\n')
        print(solution)
        print('</pre>')
        nr+=1

