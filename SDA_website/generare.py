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
            except:
                print('error import ' + module + '\nNow will delete it')
                os.remove('Lab'+str(sys.argv[1])+'/' + module)

    # For each subclass generate a statement and 
    # the detailed solution for that statement
    statements = []
    solutions = []

    for derived in Problem.__subclasses__():
        p = derived()

        statement = str(p)
        solution = p.solve()

        statements.append(statement)
        solutions.append(solution)


    path = "static/"
    folder_var = path + 'variante/'
    folder_sol = path + 'solutii/'
    
    #Cerinte:
    with open(folder_var + 'Lab' + str(sys.argv[1]) + '/' + str(sys.argv[2]) + '.txt', 'w') as f:
        for statement in statements:
            f.write('<pre>\n')
            f.write(statement)
            f.write('\n</pre>\n')
    
    #print('')

    #Rezolvari:
    with open(folder_sol + 'Lab' + str(sys.argv[1]) + '/' + str(sys.argv[2]) + '.txt', 'w') as f:
        for solution in solutions:
            f.write('<pre>\n')
            f.write(solution)
            f.write('\n</pre>\n')

