class Etudiant:
    def __init__(self, nom=None, age=None):
        self.nom = nom
        self.age = age
        self.matiere_notes = {} 

    def ajouter_matiere(self, matiere, note):
        self.matiere_notes[matiere] = note
        

    def supprimer_matiere(self, matiere):
        if matiere in self.matiere_notes:
            del self.matiere_notes[matiere]
        else:
            print("pas trouvé")
    
    def modifier_note(self, matiere, nouvelle_note):
        if matiere in self.matiere_notes:
            self.matiere_notes[matiere] = nouvelle_note
        else:
            print("pas trouvé")
            
    def lister_matieres(self):
        if self.matiere_notes:
            for matiere, note in self.matiere_notes.items():
                print(f"- {matiere}: {note}")
        else:
            print("pas d'enregistrement")
    
    def calcul_moyenne(self):
        moyenne = 0
        cmp = 0
        for note in self.matiere_notes.items():
            moyenne += note
            cmp +=1
        moyenne /=cmp
        print("la moyenne est "+moyenne)
    
    def a_reussi(self):
        si_reussi = calcul_moyenne()
        if si_reussi>10:
            print("il est reussi")
        else:
            print("pas")
            
            



    
