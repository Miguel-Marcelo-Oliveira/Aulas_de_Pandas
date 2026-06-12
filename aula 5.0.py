import pandas as pd

people = {
    'first': ['Corey', 'Jane', 'John'],
    'last': ['Schafer', 'Doe', 'Doe'],
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@gmail.com', 'JohnDoe@gmail.com']
}
df = pd.DataFrame(people)
# print(df.columns, '\n')

# Replacing the column names with new ones
df.columns = ['first_name', 'last_name', 'email']
# print(df.columns)
# print()
# print(df)

# Turning the column names to uppercase
# df.columns = [single_column.upper() for single_column in df.columns]
# print(df)

# Replacing columns' names
# df.columns = df.columns.str.replace('_', ' ')
# # print(df)

# df.columns = df.columns.str.replace(' ', '_')
# print(df)

df.rename(columns={'first_name': 'first', 'last_name': 'last'}, inplace=True)
print(df)