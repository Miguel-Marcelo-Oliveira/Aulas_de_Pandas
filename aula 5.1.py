import pandas as pd

people = {
    'first': ['Corey', 'Jane', 'John', 'Nate'],
    'last': ['Schafer', 'Doe', 'Doe', 'Diaz'],
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@gmail.com', 'JohnDoe@gmail.com', 'NateDiaz@gamil.com']
}
df = pd.DataFrame(people)

# Changing the columns' names
# df.columns = ['first_name', 'last_name', 'email']
# print(df)
# print()

# df.rename(columns={'last_name': 'last', 'first_name': 'first'}, inplace=True)
# print(df)
# print()

# print(df.loc[[2]])
# print()

# Changing the values of a row and of single values 
# df.loc[2] = ['John', 'Smith', 'JohnSmith@gmail.com']
# print(df)
# print()

# df.loc[2, ['last', 'email']] = ['McBrian', 'JohnMcBrian@gmail.com']
# print(df)
# print()

# df.loc[2, 'last'] = 'Smith'
# print(df)

# df.at[2, 'last'] = 'Doe'
# df.at[2, 'email'] = 'JohnDoe@gmail.com'
# print(df)

# filt = (df['email'] == 'JohnDoe@gmail.com')
# print(df[filt]['last'])
# df.loc[filt, 'last'] = 'Smith'
# print(df)

# Changing the values of various rows
df['email'] = df['email'].str.lower()
# print(df)

# Counting the lenght of each row on a certain column
# print(df['email'].apply(len))

def update_email(email):
    return email.upper() 

# It doesn't change the dataframe itself
# print(df['email'].apply(update_email))

# It changes the dataframe
df['email'] = df['email'].apply(update_email)
# print(df)

# df['email'] = df['email'].apply(lambda x: x.lower())
# print(df)

# Differents ways to count the lenght of Series and single values 
# print(df)
# print()

# print(df.apply(len, axis='columns'))
# print()

# print(len(df['email']))
# print()

# The smallest item on each Series
# print(df.apply(pd.Series.min))

# The lenght of each item on the Series
# print(df.map(len))

# print(df.map(str.lower))

# It gives changes the values I told to change
print(df['first'].map({'Corey': 'Chris',
                       'Jane': 'Mary',
                    }))
print()
# It gives changes the values I told to change, 
# and it doesn't change the values that I didn't say
print(df['first'].replace({'Corey': 'Chris',
                       'Jane': 'Mary',
                    }))
