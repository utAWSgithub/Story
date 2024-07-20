import numpy as nu
import pandas as pd
a=pd.read_csv("C:/Users/hp/Desktop/batsman_season_record.csv")
#a.set_index("batsman_season_record",inplace=True)
print(a)

df4=reset_index(inplace=True)
print(df4)

df4[(["avg"]>45) & (df4["strike_rate"]>125)]
  