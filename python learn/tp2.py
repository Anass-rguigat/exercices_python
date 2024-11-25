class Person:
    def __init__(self, nom=None, age=None, date_naissance=None, adresse=None, telephone=None):
        self._nom = nom
        self._age = age
        self._date_naissance = date_naissance
        self._adresse = adresse
        self._telephone = telephone

    def afficher_info(self):
        print("Le nom : " + str(self.nom) + 
              ", Age : " + str(self.age) + 
              ", Date de naissance : " + str(self.date_naissance) + 
              ", Téléphone : " + str(self.telephone))
        
    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def date_naissance(self):
        return self._date_naissance

    @date_naissance.setter
    def date_naissance(self, value):
        self._date_naissance = value

    @property
    def adresse(self):
        return self._adresse

    @adresse.setter
    def adresse(self, value):
        self._adresse = value

    @property
    def telephone(self):
        return self._telephone

    @telephone.setter
    def telephone(self, value):
        self._telephone = value


class Employee(Person):
    def __init__(self, nom=None, age=None, date_naissance=None, adresse=None, telephone=None,
                 employee_id=None, position=None, salaire=0.0):
        super().__init__(nom, age, date_naissance, adresse, telephone)
        self.employee_id = employee_id  
        self.position = position          
        self.salaire = salaire         

    def afficher_info(self):
        super().afficher_info()
        print("ID Employé : " + str(self.employee_id) + 
              ", Position : " + str(self.position) + 
              ", Salaire : " + str(self.salaire))

    def augmenter_salaire(self, pourcentage):
        if pourcentage < 0:
            print("Le pourcentage ne peut pas être négatif.")
            return
        
        augmentation = self.salaire * (pourcentage / 100)
        self.salaire += augmentation
        print(f"Nouveau salaire après augmentation de {pourcentage}% : {self.salaire}")

    @staticmethod
    def calculer_moyenne_salaire(employes):
        if not employes:
            return 0
        
        total_salaire = sum(emp.salaire for emp in employes)
        moyenne = total_salaire / len(employes)
        
        return moyenne