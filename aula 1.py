import pandas as pd

df = pd.read_csv('pokemon.csv')

print(df.shape, '\n')

# print(df.info())

# pd.set_option('display.max_columns', 5)
# pd.set_option('display.max_rows', None)
# print(df)

# print(df.head(50))
# print(df.tail(50))


# Parte da Aula 2

print(df.columns, '\n')
print(df[['Type2']].value_counts())
# print(df.loc[6:21, 'Name':'Height'])