# in this we create multi dimensional data structure i.e. called dataframe
import pandas as pd
table = pd.DataFrame({'Name': ['Pooja', 'Pritee', 'Vinayak', 'Vivek'], 'Marks': [89, 87, 90, 88]})
print(table)
file = pd.read_csv("country.csv")
print('hello')