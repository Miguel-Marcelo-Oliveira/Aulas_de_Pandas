import pandas as pd

df = pd.read_csv('pokemon.csv', index_col='No')
# print(df.to_string())
print(df.loc[:, 'Name':'Height'].to_string(index=True))
