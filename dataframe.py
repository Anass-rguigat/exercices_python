import pandas as pd

# Liste prix
voitures_prix = [20000, 22000, 24000, 35000, 40000, 37000]

# Liste 
index_voiture = ["cadilac", "audi", "benz", "dacia", "bmw", "fiat"]

my_serie = pd.Series(voitures_prix, index=index_voiture)
print("Série des prix des voitures :")
print(my_serie["cadilac":"dacia"])
# ------------------------------------------


departements_budget = {
    "Marketing": 50000,
    "Ventes": 75000,
    "R&D": 120000,
    "Ressources Humaines": 40000,
    "Finance": 85000,
    "IT": 100000
}

serie_budget = pd.Series(departements_budget)

print(serie_budget)

print(serie_budget.iloc[0])

# ------------------------------------------

# Tuple 
notes_etudiant = (15, 18, 12, 17, 14)

matieres = ["Mathématiques", "Physique", "Chimie", "Informatique", "Anglais"]

serie_notes = pd.Series(notes_etudiant, index=matieres)
print("\nSérie des notes par matière :")
print(serie_notes)


#etudiant 
etud = {'ali':85,'siham':90,'ahmed':78,'Nora':92,'kamal':88}
seriess = pd.Series(etud)
print(seriess.iloc[2])
print(seriess['ahmed'])
print(seriess['siham':'Nora'])





data = {'Nom':['ahmed','fatima','youssef'],
        'age':[25,30,35],
        'ville':['rabat','fes','marrakech']}
df=pd.DataFrame(data)
print(df)


dt = [
    {'nom': 'aa', 'age': 25, 'ville': 'rabat'},
    {'nom': 'yy', 'age': 35, 'ville': 'fes'},
    {'nom': 'hh', 'age': 45, 'ville': 'marakech'},
]

df = pd.DataFrame(dt)

# Utilisation de loc pour accéder par labels
# Par exemple, accéder à la ligne où le nom est 'yy'
loc_result = df.loc[df['nom'] == 'yy']
print("Résultat de loc :")
print(loc_result)

# Utilisation de iloc pour accéder par index
# Par exemple, accéder à la première ligne
iloc_result = df.iloc[0]
print("\nRésultat de iloc :")
print(iloc_result)