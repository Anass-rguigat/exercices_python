class student:
    def __init__(self):#constructeur par defaut
        self.name="new"
        self.age=0
    def affiche(self):
        print("je suis etudiant la nom",self.name,"et age ",self.age)    
class personne:
    def __init__(self,name,age):#constructeur avec params
        self.name=name
        self.age=age
    def affiche(self):
        print("je suis personne la nom",self.name,"et age ",self.age) 
class personne2:
    def __init__(self,name="",age=0):#constructeur par defaut ou avec params
        self.name=name
        self.age=age 
    def affiche(self):
        print("je suis personne 2 la nom",self.name,"et age ",self.age) 
     
s1= student()#creer une variable et instance objet
s2= personne("youssef",22)#creer une variable et instance objet
s3= personne2()#creer une variable et instance objet
s1.sexe="male"
print(s1.__dict__)
print(s2.__dict__)
print(s3.__dict__)
print(dir(s1))
s1.affiche()
s2.affiche()
s3.affiche()

