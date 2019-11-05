import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

## read data
path = "Dropbox/CarbonFootprintEGU/data/"
df = pd.read_excel(path+"data_processed.xlsx")

# how many countries to plot, then grouped as other.
n = 11

## SCENARIO REALISTIC
S1 = np.array(df["per country Realistic"])
N = np.array(df["Country"])

S1[np.isnan(S1)] = 0
args1 = np.argsort(S1)
names1 = N[args1][::-1]
carbon1 = S1[args1][::-1]
carbon_percent1 = carbon1 / sum(carbon1) * 100

# others grouped
C1 = np.hstack((sum(carbon_percent1[n:]),carbon_percent1[:n]))
names1 = np.hstack(('All other countries',names1[:n]))

## SCENARIO EUROPE BY RAIL
S2 = np.array(df["per country Rail"])

S2[np.isnan(S2)] = 0
args2 = np.argsort(S2)
names2 = N[args2][::-1]
carbon2 = S2[args2][::-1]
carbon_percent2 = carbon2 / sum(carbon2) * 100

# others grouped
C2 = np.hstack((sum(carbon_percent2[n:]),carbon_percent2[:n]))
names2 = np.hstack(('All other countries',names2[:n]))

## PLOT
cmap = matplotlib.cm.get_cmap('viridis')
colors = cmap(np.linspace(0,0.9,n+1))
colors[0,:3] = 0.5

fig,(ax1,ax2) = plt.subplots(1,2,figsize=(12,4))

# REALISTIC
wedges1, texts1, autotexts1 = ax1.pie(C1,labels=names1,autopct="%d%%",colors=colors)
plt.setp(autotexts1, size=8, weight="bold", color="white")
ax1.axis('equal')
ax1.set_title("a) Breakdown by country, total %d tC02e" % sum(carbon1),loc="left",weight="bold")

# RAIL
wedges2, texts2, autotexts2 = ax2.pie(C2,labels=names2,autopct="%d%%",colors=colors)
plt.setp(autotexts2, size=8, weight="bold", color="white")
ax2.axis('equal')
ax2.set_title("b) All journeys <1500km by rail, total %d tC02e" % sum(carbon2),loc="left",weight="bold")

plt.tight_layout()
plt.show()