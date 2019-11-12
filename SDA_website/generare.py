import os
import glob
from problem import Problem

import sys



if __name__ == '__main__':
    
    if(len(sys.argv) != 3):
        exit();
        
    for module in os.listdir('Lab'+str(sys.argv[1])+'/.'):
        if module[-3:] == '.py':
            try:
                __import__('Lab'+str(sys.argv[1])+'.' + module[:-3], locals(), globals())
            except Exception as e:
                print('error import ' + module + '\nNow will delete it')
                with open("import_error"+str(sys.argv[1])+".txt","a") as f:
                    f.write(module + ":\n");
                    f.write(str(e));
                os.remove('Lab'+str(sys.argv[1])+'/' + module)

    # For each subclass generate a statement and 
    # the detailed solution for that statement
    statements = []
    solutions = []
    
    for derived in Problem.__subclasses__():
        p = derived()
        statement = str(derived.__name__);
        statement+="\n";
        
        statement += str(p)
        
        solution = str(derived.__name__);
        solution +="\n";
        
        solution += p.solve()

        statements.append(statement)
        solutions.append(solution)


    path = "static/"
    folder_var = path + 'variante/'
    folder_sol = path + 'solutii/'
    
    #Cerinte:
    with open(folder_var + 'Lab' + str(sys.argv[1]) + '/' + str(sys.argv[2]) + '.txt', 'w') as f:
        nr = 0
        for statement in statements:
            f.write('<pre id="'+str(nr)+'" onclick="afisare('+str(nr)+')">\n')
            f.write(statement)
            f.write('</pre>')
            nr+=1;
    
    #print('')

    #Rezolvari:
    with open(folder_sol + 'Lab' + str(sys.argv[1]) + '/' + str(sys.argv[2]) + '.txt', 'w') as f:
        nr = 0
        for solution in solutions:
            f.write('<pre id="'+str(nr)+'" onclick="afisare('+str(nr)+')">\n')
            f.write(solution)
            f.write('</pre>')
            nr+=1

