from geopy.geocoders import Nominatim
from geopy import distance
import pandas as pd
geolocator = Nominatim()

## read data
path = "/local/home/kloewer/dbx/Dropbox/CarbonFootprintEGU/data/"
df = pd.read_excel(path+"data_processed.xlsx")

n = len(df["City"])

cities = [df["City"].iloc[i] for i in range(n)]
countries = [df["Country"].iloc[i] for i in range(n)]

## get locations from openstreet map database
for i,(city,country) in enumerate(zip(cities,countries)):
    print(i)
    loc = geolocator.geocode(city+", "+country,timeout=30)
    plt.pause(0.5)

    try:
        df.at[i,"Latitude"] = loc.latitude
        df.at[i,"Longitude"] = loc.longitude
    except:
        print("ERROR in line "+str(i+2)+" with "+city+", "+country)

## calculate distances

vienna = geolocator.geocode("Vienna, Austria")
vienna_loc = (vienna.latitude,vienna.longitude)

for i in range(n):
    loc = (df.at[i,"Latitude"],df.at[i,"Longitude"])
    df.at[i,"Distance to Vienna"] = distance.distance(loc,vienna_loc).km

## export data
df.to_excel(path+"data_processed.xlsx")