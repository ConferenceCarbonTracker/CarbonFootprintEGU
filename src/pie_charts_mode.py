import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

## read data
path = "Dropbox/CarbonFootprintEGU/data/"
df = pd.read_excel(path+"data_processed.xlsx")

dist = np.array(df["Distance to Vienna"])
n = len(dist)

## SCENARIO REALISTIC
S1 = np.array(df["per country Realistic"])
N = np.array(df["Country"])

S1[np.isnan(S1)] = 0

C1lh = sum([S1[i] for i in range(n) if dist[i] > 1500])/sum(S1)*100
C1sh = sum([S1[i] for i in range(n) if dist[i] >= 700 and dist[i] < 1500])/sum(S1)*100
C1ra = sum([S1[i] for i in range(n) if dist[i] < 700])/sum(S1)*100

## SCENARIO EUROPE BY RAIL
S2 = np.array(df["per country Rail"])

S2[np.isnan(S2)] = 0
C2lh = sum([S2[i] for i in range(n) if dist[i] > 1500])/sum(S2)*100
C2ra = sum([S2[i] for i in range(n) if dist[i] <= 1500])/sum(S2)*100

## PLOT
cmap = matplotlib.cm.get_cmap('viridis')
colors = cmap(np.linspace(0,0.9,3))

fig,(ax1,ax2) = plt.subplots(1,2,figsize=(12,4))

# REALISTIC

wedges1, texts1, autotexts1 = ax1.pie([C1lh,C1sh,C1ra],labels=["Long-haul","Short-haul","Rail"],autopct="%.1f%%",colors=colors)
plt.setp(autotexts1, size=8, weight="bold", color="white")
ax1.axis('equal')
ax1.set_title("a) Breakdown by mode of transport, total %d tC02e" % sum(S1),loc="left",weight="bold")

# RAIL
wedges2, texts2, autotexts2 = ax2.pie([C2lh,C2ra],labels=["Long-haul","Rail"],autopct="%.1f%%",colors=colors)
plt.setp(autotexts2, size=8, weight="bold", color="white")
ax2.axis('equal')
ax2.set_title("b) All journeys <1500km by rail, total %d tC02e" % sum(S2),loc="left",weight="bold")

plt.tight_layout()
plt.show()