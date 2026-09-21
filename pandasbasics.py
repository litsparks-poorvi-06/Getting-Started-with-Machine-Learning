import numpy as np
import pandas as pd

'''data = {
    'name': ['john', 'mary'],
    'age': [19, 20],
    'city': ['new york', 'san fransico'],
    'salary': [10000, 12000]
}

df = pd.DataFrame(data)
print(df)'''



'''# Creating a DataFrame using lists
data1 = [
    ['john', 19, 'new york', 10000],
    ['mary', 20, 'san fransico', 12000]
]
columns = ['name', 'age', 'city', 'salary']
df2 = pd.DataFrame(data1, columns=columns)
print(df2)
print(df2['name'])
#creating a new columns
df2['designation']=['doctor','engineer']
print(df2)
#removing a column
print(df2.drop('designation',axis=1))
print(df2.drop('designation',axis=1,inplace=True))'''



#finding missing values 
'''
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [1, 2, 3, 4, 5],
    'C': [1, 2, 3, np.nan, np.nan],
    'D': [1, np.nan, np.nan, np.nan, 5]
}
df = pd.DataFrame(data)
print(df)
print(df.isna())
#it will tell that which row has more null value 
print(df.isna().sum())
print(df.dropna())
print(df.dropna(thresh=3))'''

#to fill the missing values
'''data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [1, 2, 3, 4, 5],
    'C': [1, 2, 3, np.nan, np.nan],
    'D': [1, np.nan, np.nan, np.nan, 5]
}
df = pd.DataFrame(data)
print(df.fillna(0))
values={'A':100,'B':200,'C':600,'D':300}
print(df.fillna(value=values))'''

'''#groupby
data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Store': ['S1', 'S1', 'S2', 'S2', 'S1', 'S2', 'S2', 'S1'],
    'Sales': [100, 200, 150, 250, 120, 180, 200, 300],
    'Quantity': [10, 15, 12, 18, 8, 20, 15, 25],
    'Date': pd.date_range('2023-01-01', periods=8)
}
df = pd.DataFrame(data)
print(df)
cat=df.groupby('Category')
for i,v in cat:
    print(i)
    print(v)

print(cat)
print(df.groupby('Category')['Sales'].sum())'''

#working with pivot tables
data = {
    'Date': pd.date_range('2023-01-01', periods=20),
    'Product': ['A', 'B', 'C', 'D'] * 5,
    'Region': ['East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West',
               'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South'],
    'Sales': np.random.randint(100, 1000, 20),
    'Units': np.random.randint(10, 100, 20),
    'Rep': ['John', 'Mary', 'Bob', 'Alice', 'John', 'Mary', 'Bob', 'Alice', 'John', 'Mary',
            'Bob', 'Alice', 'John', 'Mary', 'Bob', 'Alice', 'John', 'Mary', 'Bob', 'Alice']
}

df = pd.DataFrame(data)
print(df)

'''df['Month'] = df['Date'].dt.month_name()
df['Quarter'] = 'Q' + df['Date'].dt.quarter.astype(str)
print(df)
print(pd.pivot_table(df,values="Sales",index="Region",columns="Product"))
print(pd.pivot_table(df,values="Sales",index="Region",columns="Product",aggfunc='median'))'''
