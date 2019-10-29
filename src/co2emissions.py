import pandas as pd
import numpy as np

## read data
path = "/local/home/kloewer/dbx/Dropbox/CarbonFootprintEGU/data/"
df = pd.read_excel(path+"data_processed.xlsx")

n = len(df["City"])

## SCENARIO 1 "REALISTIC"

for i in range(n):

    dist = df["Distance to Vienna"].iloc[i]
    totaldist = df["Retour"].iloc[i]

    if dist < 700:   # RAIL JOURNEY
        df.at[i,"tCO2e - Realistic"] = totaldist*0.03 / 1000        # tCO2e
    elif dist < 1500:    # SHORT HAUL
        df.at[i,"tCO2e - Realistic"] = totaldist*0.2 / 1000
    else:    # LONG HAUL
        df.at[i,"tCO2e - Realistic"] = totaldist*0.25 / 1000

## SCENARIO 2 "ALL SHORT HAUL ARE RAIL"

for i in range(n):

    dist = df["Distance to Vienna"].iloc[i]
    totaldist = df["Retour"].iloc[i]

    if dist < 1500:   # RAIL JOURNEY
        df.at[i,"tCO2e - Rail"] = totaldist*0.03 / 1000        # tCO2e
    else:    # LONG HAUL
        df.at[i,"tCO2e - Rail"] = totaldist*0.25 / 1000

## EXPORT DATA
df.to_excel(path+"data_processed.xlsx")