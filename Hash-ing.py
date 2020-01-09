# generare fisier cu Hash
import random
import pickle
letters = "abcdefghijklmnopqrstuvwxyz";
dict = {};
fOut = open("HashTxt.txt","wb");
def checkWords(list):
    # aven lista de caractere
    characters = {};
    finded = "";
    for c in list:
        characters[letters[c]] = 1;
    fIn = open("cuvinte.txt","r");
    for word in fIn:        # read line by line
        bifat = True;
        for c in word[:-1]:
            if c not in characters:
                bifat = False;
        if bifat and len(word[:-1]):
            finded+=word[:-1];
            finded+=" ";
    if(len(finded)):
        printedlist = "";
        for x in list:
            printedlist+=letters[x];
        dict[printedlist] = finded.split(" ");
        # fOut.write(printedlist);
        # fOut.write(" : ");
        # fOut.write(finded);
        # fOut.write("\n");
    fIn.close();
    
def HashTxt():
    list  = []; # lista de caractere
    for length in range(4,7):    #cuvinte doar intre 3 si 8 caractere
        list = [j for j in range(0,length)];    # initializam lista
        da = 1;
        while(da):
            # for j in range(0,len(list)):
                # try:
                    # print(letters[list[j]],end="");
                # except:
                    # print(da);
                    # print(list[j]," ",j);
                    # return;
            # print("");
            checkWords(list);
            list[-1]+=1;
            for k in range(len(list)-1,-1,-1):
                if(list[k]>=(len(letters)-len(list)+k)+1):
                    list[k] = k;
                    if(k == 0):
                        da = 0;
                        break;
                    list[k-1] += 1;
            # urmatoarea litera va fi mai mare decat cureta
            for k in range(0,len(list)-1):
                if(list[k] > list[k+1]):
                    list[k+1] = list[k]+1;
    for x in dict:
        print(x," ",dict[x]);
    # salveaza dictionarul in fisier binar
    pickle.dump(dict,fOut)


def randPonds(nr):
    v = [0 for i in range(0,nr)];
    N = 100;
    N += N%nr;
    for i in range(0,len(v)):
        v[i] = N//nr;
    v[0]-=N%nr;
    #acum suma lor este 100;
    for i in range(len(v)-1,0,-1):
        d = random.randint(1,v[i]//2);
        v[i]-=d;
        v[i-1]+=d;
        while(v.count(v[i]) != 1):
            v[i]-=1;
            v[i-1]+=1;
    print(v);
def test():
    ana = "ana are mere";
    ana2 = ana[:];
    print(ana);
    print(ana2);
    del ana
    # print(ana);
    print(ana2);
    fOut = open("HashTxt.txt","a");
    fOut.write(ana2);
    fOut.close();
    
# test();
HashTxt();
fOut.close();
# randPonds(6);
