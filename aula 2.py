import pandas as pd

person = {
    'first': 'Corey',
    'last': 'Schafer',
    'email': 'CoreyMSchafer@gmail.com'
}

people = {
    'first': ['Corey'],
    'last': ['Schafer'],
    'email': ['CoreyMSchafer@gmail.com']
}

people = {
    'first': ['Corey', 'Jane', 'John'],
    'last': ['Schafer', 'Doe', 'Doe'],
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@gmail.com', 'JohnDoe@gmail.com']
}

# Printing the values in the key 'email'
# print(people['email'])

# Transforming the dictionary into a DataFrame
df = pd.DataFrame(people)
print(df, '\n')
# print(df['email'])
# print(type(df['email']))

# Could cause errors if the column's name is the same as a method of the DataFrame
# print(df.email)

# Multilpe columns
# print(df[['last', 'email']])

# Only columns
# print(df.columns)

# interger location - locating using the index
# print(df.iloc[[0, 1]])

# Selecting specific columns with iloc
# print(df.iloc[[0, 1], [1, 2]])

# Seaarching by label
print(df.loc[[0, 1], ['email', 'last']])
