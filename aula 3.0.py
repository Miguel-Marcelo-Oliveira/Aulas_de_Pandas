import pandas as pd

people = {
    'first': ['Corey', 'Jane', 'John'],
    'last': ['Schafer', 'Doe', 'Doe'],
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@gmail.com', 'JohnDoe@gmail.com']
}
df = pd.DataFrame(people)
print(df)
print()

# Now the 'email' column is the index of the DataFrame
df.set_index('email', inplace=True)
print(df)
print()
print(df.index)
print()

# Locating a row using the index
print(df.loc['CoreyMSchafer@gmail.com'], '\n')
print(df.iloc[0], '\n')

# Resetting the index to the default integer index
df.reset_index(inplace=True)
print(df)