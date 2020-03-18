# Site pt temele de la Structuri de date si algoritmi

Site-ul este scris in python folosind modulul flask<br>  
Pe acest site se gasesc variante de probleme rezolvate de proiectele primite la laboratul de SDA.

## Functionalitati
*  Copierea proiectelor din repozistorul de github
*  Rularea proiectelor si generarea variantelor
*  Adaugarea optiunii de upload (in prezent poseda imperfectiuni)
*  Pentru proiectul final:
  *  modulele matplotlib si networkx;
  *  aranjarea fisierelor, rezolvarea coliziuniilor de nume ale imaginilor.

## Afisare graf cu matplotlib si networkx

* Adaugati un atribut nou in clasa: **ImgName**
  * atributul trebuie declarat in init();
  * ex: *self.ImgName = ['Graf.png']*
* La salvarea figurii: *plt.savefig(self.ImgName[0])*
* Daca vreti sa aveti imaginile in cerinta(statement), adaugati un atribut **statementPicture**, care reprezinta numarul de imagini pe care le vreti in statement;
  * i.e.: primele *statementPicture* for fi puse in statement celelalte in solution.
  * daca aveti o singura imagine si o vreti in statement: *ImgName = ['numele imaginii'], statementPicture = 1*
* Se pot pune mai multe imagini  
### Imaginele trebuie generate in solve() sau alte functi apelate in solve(), nu in init()
