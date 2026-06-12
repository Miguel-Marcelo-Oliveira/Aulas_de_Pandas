import pandas as pd

df = pd.read_csv('pokemon.csv')

# water_filter = (df['Type1'] == 'Water') | (df['Type2'] == 'Psychic') 
# print(df.loc[water_filter, 'No':].to_string(index=False))

# types1 = ['Water', 'Grass', 'Fire', 'Electric']
# filt = df['Type1'].isin(types1)
# print(df.loc[filt].to_string(index=False))
# print('\n', filt.sum())

filt = df['Type2'].str.contains('Poison|Flying', na=False)
# print(df.loc[filt, ['Name', 'Type2']])
