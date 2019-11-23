from problem import Problem
import random

class Problem16(Problem):
    def __init__(self):
        statement = "ceva";
        data = [0,0];
        data[0] = [random.randint(0,5) for i in range(10)];
        # data[0]=[4, 0, 5, 5, 4, 4, 2, 0, 3, 5];
        # data[1] = 5;
        data[1] = random.choice(data[0]);
        
        super().__init__(statement,data);
    
    def partition(self,v,left,right,Ipiv):
        #v - vector
        #left, right - capetele
        #Ipiv - indexul pivotului
        v[Ipiv],v[right] = v[right],v[Ipiv]; #punem pivotul ultimul;
        Ipiv = right;
        #vom exclude toate elementele egale cu pivotul de la capatul sirului
        
        i = -1;         #pleaca de la incepu1
                        #j pleaca de la sfarsit
        # print(v);
        for j in range(left,right+1):
            while(v[j] == v[Ipiv]):
                if(j< right):
                    right-=1;
                    v[j], v[right] = v[right], v[j];
                    
                else:
                    break;
            if(v[j]<v[Ipiv]):
                i+=1;
                v[i],v[j] = v[j], v[i];
            # print(j)
            # print(v);
        #i se opreste la ultimul element mai mic decat pivotul
        #mutam pivotul dupa i;
        print("in part",v)
        # v[i+1], v[Ipiv] = v[Ipiv],v[i+1];
        #acum mutam pivotul si toate elementel...
        print("");
        for j in range(0,Ipiv-right+1):
            v[j+i+1],v[Ipiv] = v[Ipiv],v[j+i+1];
            Ipiv-=1;
            # print(v)
        return i+1; #pozitia pivotului
            
    def verificare(self,v,Ipiv):
        for i in range(0,Ipiv):
            if v[i]>v[Ipiv]:
                print("aiurea");
                return;
        for i in range(Ipiv,len(v)-1):
            if(v[i]<v[Ipiv]):
                print("aiurea");
                return;
    def solve(self):
        solution = "solutie";
        # print(self.data);
        v = self.data[0];
        Ipiv = v.index(self.data[1]);
        print(v);
        print("pos - val")
        print(Ipiv," - ",v[Ipiv]);
        Ipiv = self.partition(v,0,len(v)-1,Ipiv);
        print(v);
        self.verificare(v,Ipiv);
        return solution;
        
        
p = Problem16();
p.solve();