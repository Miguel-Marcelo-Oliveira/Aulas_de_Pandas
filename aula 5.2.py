import pandas as pd

df = pd.read_csv('pokemon.csv')
# print(df.columns)

df['Legendary'] = df['Legendary'].replace({0: 'No',
                                1: 'Yes'})
df.rename(columns={'No': 'Number'}, inplace=True)
print(df.to_string(index=0))
# filt = df['Legendary'] == 'Yes'
# print(df[filt].to_string(index=False))