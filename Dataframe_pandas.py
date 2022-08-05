# in this we create multi dimensional data structure i.e. called dataframe
import pandas as pd
table = pd.DataFrame({'Name': ['Pooja', 'Pritee', 'Vinayak', 'Vivek'], 'Marks': [89, 87, 90, 88]})
print(table)
file = pd.read_csv("country.csv")
'''print(file.head())                  #it gives th first five data from file
print(file.tail())                  #it gives the last five data
print(file.shape)                   #it gives the info of rows and columns
print(file.describe())              #it gives the info of table
print(file.iloc[5:11, 0:5])         #it gives the 5 to 10 rows and 0 to 4 columns from the record
print(file.loc[5:11, ['name', 'country-code']])         #it gives 5 to 10 rows and specified columns
print(file.drop('alpha-2', axis =1))                #it help to delete column alpha-2
print(file.drop([1,3,4], axis=0))                   #it delete row 1 3 4
#print(file.min())                                  # it return minimum value of data
def add(s):
    print(s+3)

print(file.loc[0:5, ['country-code']])
file[['country-code']].apply(add)                   #if we want to do specific operation with paritcular data'''

print(file['sub-region'].value_counts())
print(file.sort_values(by='region'))
