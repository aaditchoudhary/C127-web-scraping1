import pandas as pd
import csv
df=pd.read_csv(r"C:\Users\kanis\Downloads\Realtime-Image-detection-master\Realtime-Image-detection-master\final.csv")
print(df.shape)
del df["hyperlink"]
print(df.shape)
del df["planet_mass"]
print(df.shape)
del df["orbital_radius"]
print(df.shape)
del df["eccentricity"]
print(df.shape)
del df["stellar_magnitude"]
print(df.shape)
del df["discovery_date"]
print(df.shape)
del df["planet_type"]
print(df.shape)
del df["planet_radius"]
print(df.shape)
del df["orbital_period"]
print(df.shape)


print(df.head())
df=df.rename({'name':"planetName",'light_years_from_earth':"DistanceFromTheEarth"},axis='columns')
df.to_csv('main.csv')