import _sqlite3
import pandas as pd
from numpy .random import random

#part1
#connection=_sqlite3.connect("netflix_titles.csv")
df=pd.read_csv('netflix_titles.csv')
result =  df
print(result)
result=df.columns #print columns
print(result)
result=df.info #print rows and columns
print(result)

#df =pd.read_sql_query("SELECT * FROM director",connection)
#print(df) connection kısmını okuyor
#part 2
result = df.head() #ilk 5 kayıt okuyor
print(result)
result=df.tail(10) # son 10 kayıt
print(result)
result=df[["date_added","release_year"]].head() # ilk 5 kayıt
print(result)
result=df[5:10][["date_added","release_year"]].head() #5 ile9 arası kayıtlar
print(result)
result =df.dropna(inplace=True)
print(result)
df["type"]=df["type"].str.upper()
print(df.head(10))


