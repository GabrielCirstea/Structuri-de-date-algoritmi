from problem import Problem
import random

class myProblem(Problem):
    def __init__(self):
        data = random.sample(range(100), random.randint(5,9))
        statement = "Se primesc nr" + ', '.join(map(str,data)) + '\n';
        statement += "Aici e problema facuta de mine\n Sa se aleaga nr min din sir.\n"

        super().__init__(statement,data)
    def solve(self):
        solution = 'Se parcurge vectorul si se alge minimul.\n'
        min = self.data[0]
        for x in self.data:
            if min > x:
                min = x;
        solution += 'S-a gasit ' + str(min) + ',ca fiind cel main mic nr'
        
        return solution

    def __str__(self):
        return self.statement

