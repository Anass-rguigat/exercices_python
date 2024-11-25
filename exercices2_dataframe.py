import pandas as pd

# Création du DataFrame
data = [{'Nom': 'Alice', 'Age': 22, 'Note': 85},
        {'Nom': 'Bob', 'Age': 24, 'Note': 90},
        {'Nom': 'Charlie', 'Age': 23, 'Note': 78},
        {'Nom': 'David', 'Age': 21, 'Note': 88}]

df = pd.DataFrame(data)

#1
age_filtered = df[df['Age'] > 22]
print(age_filtered)
note_filtered = df[df['Note'] > 85]
print(note_filtered)

#2
#a
des = df.describe()
print(des)
#b
ress = df.info()
print(ress)



