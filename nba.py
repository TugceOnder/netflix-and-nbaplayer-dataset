import pandas as pd
df=pd.read_csv('player_data.csv')
result =df.head(10) # rad first 10 columns
print(result)
result=len(df.index)
print(result)  #toplam kaç index var
result=df["weight"].mean()
print(result) #ortalma weight
result=df["year_start"].max
print(result)
result= df[df["weight"]==df["weight"].max()]["name"].iloc[0]
print(result)#en kilolu kişi
result= df[(df["year_start"]>=1974)&(df["year_start"]<=1991)][["name","position"]].sort_values("name")
#1975 ile 1991 oyuncu ve pozisyon ada göre sırala
print(result)
result=df[df["name"]=="David Andersen"]["height"] #listeden bir ad seçme
print(result)
#collegeler göre başlangıç yılı
result =df.groupby("college").mean("year_start")
print(result)
result =len(df.groupby("college"))
print(result) #kaç grup var
result=df["college"].value_counts()
print(result) # üniversiteye giden oyuncular sayı dağlımı
df=df.dropna()
result=df[df["name"].str.contains("David")]
print(result) # david adı geçen oyuncuların listesi

