import pandas as pd

people = {
    'first': ['Corey', 'Jane', 'John'],
    'last': ['Schafer', 'Doe', 'Doe'],
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@gmail.com', 'JohnDoe@gmail.com']
}
df = pd.DataFrame(people)
# print(df)
print()

# Filtering the DataFrame based on a condition
# print(df['last'] == 'Doe')
# filt = df['last'] == 'Doe'
# print(df[filt])
# print(df.loc[filt, 'email'])

filt = (df['last'] == 'Schafer') | (df['first'] == 'John')
# print(f'Does not match the condition:\n{df.loc[-filt]}\n')
# print(f'Matches the condition:\n{df.loc[filt]}\n')
print(df.loc[filt, ['last', 'email']])