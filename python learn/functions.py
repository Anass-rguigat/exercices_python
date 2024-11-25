class company:
    def __init__(self , n,nbr) :
        self.name = n
        self.number_employe = nbr
    def affiche(self):
        print("company is ",self.name," number of employe is",self.number_employe)
class personne2:
    def __init__(self,name= None,age= None,cmp=None):#constructeur par defaut ou avec params
        self.name=name
        self.age=age 
        self.Company=cmp
    def affiche(self):
        print("je suis personne 2 le nom",self.name,"et age ",self.age,"travail dans l'entreprise ",self.Company.name) 
    def __str__(self):
        return "je suis personne 2 le nom "+self.name+" et age "+str(self.age)+" travail dans l'entreprise "+self.Company.name
        
cmpa = company(input("entrez le nom entreprise : "),input("entrez le nombre des employe : ")) 
p2 = personne2(input("entrez le nom : "),input("entrez l'age : "),cmpa)
"""
p2.name = str(input("entrez le nom : "))
p2.age = int(input("entrez l'age : "))
"""
cmpa.affiche()
print(p2)
print(isinstance(p2,personne2))