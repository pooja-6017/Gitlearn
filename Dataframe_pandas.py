# in this we create multi dimensional data structure i.e. called dataframe
import pandas as pd
table = pd.DataFrame({'Name': ['Pooja', 'Pritee', 'Vinayak', 'Vivek'], 'Marks': [89, 87, 90, 88]})
print(table)
file = pd.read_csv("country.csv")
print(file.head())          #it gives th first five data from file
print(file.tail())          #it gives the last five data
#print(file.shape())         #it gives the info of rows and columns
print(file.describe())      #it gives the info of table