import pandas as pd

df = pd.DataFrame({'A': [12, 6, 20, 3, 9], 'B': [2, 8, 5, 4, 10]})

print("question 1")
filtered_df = df[(df['A'] > 8) & (df['B'] < 7)]
print(filtered_df)

print("question 2")
subset_df = df.iloc[:4, :2]
print(subset_df)

print("question 3")
df2 = pd.DataFrame({
    'A': [3, 4, 6, 8, 10],
    'B': [7, 5, 6, 9, 3],
    'C': ['valide', 'invalide', 'valide', 'valide', 'invalide']
})

valid_df = df2.query("C == 'valide'")
print(valid_df)


print("question 4")
isin_df = df2[df2['A'].isin([4, 8, 10])]
print(isin_df)
