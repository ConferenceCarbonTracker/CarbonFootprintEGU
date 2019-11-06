import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

## read data
path = "/local/home/kloewer/dbx/Dropbox/CarbonFootprintEGU/data/"
df = pd.read_excel(path+"data_processed.xlsx")

## Sort by carbon emissions from highest country to lowest
carbon = df["per country Realistic"].to_numpy()
names = df["Country"].to_numpy()
numbers = df["Numbers"].to_numpy()

notzero = carbon != 0
numbers = numbers[notzero]
carbon = carbon[notzero]
names = names[notzero]

percapita = carbon/numbers
args = np.argsort(percapita)

names = names[args]
carbon = carbon[args]
numbers = numbers[args]

ccarbon = np.cumsum(carbon)
cnumbers = np.cumsum(numbers)

ccarbonpercent = ccarbon/sum(carbon)*100
cnumpercent = cnumbers/sum(numbers)*100

names[names == "United States"] = "USA"

# for rectangles
x = np.vstack((cnumpercent,cnumpercent)).flatten("F")
y1 = np.hstack((ccarbonpercent[0],np.vstack((ccarbonpercent[:-1],ccarbonpercent[:-1])).flatten("F"),ccarbonpercent[-1]))
y2 = np.hstack((ccarbonpercent[0],np.vstack((ccarbonpercent[1:],ccarbonpercent[1:])).flatten("F"),ccarbonpercent[-1]))

## PLOT
fig,ax = plt.subplots(1,1,figsize=(5.08,5))

# SCENARIO 1
i1 = 80
l1, = ax.plot([cnumpercent[i1],cnumpercent[i1]],[0,ccarbonpercent[i1]],"C0")
ax.plot([0,cnumpercent[i1]],[ccarbonpercent[i1],ccarbonpercent[i1]],"C0")
ax.text(cnumpercent[i1]+2,10,"{:d}%".format(int(round(100-cnumpercent[i1]))),color="C0")
ax.text(35,ccarbonpercent[i1]+1,"{:d}%".format(int(round(ccarbonpercent[i1]))),color="C0")
ax.arrow(cnumpercent[i1]+5,9,3,0,head_width=0.5,color="C0")
ax.arrow(cnumpercent[i1]+5.2,9,-4,0,head_width=0.5,color="C0")

# SCENARIO 2
i2 = 68
ax.plot([cnumpercent[i2],cnumpercent[i2]],[0,ccarbonpercent[i2]],"C2")
ax.plot([0,cnumpercent[i2]],[ccarbonpercent[i2],ccarbonpercent[i2]],"C2")
ax.text(cnumpercent[i2]+2,4,"{:d}%".format(int(round(100-cnumpercent[i2]))),color="C2")
ax.text(1,ccarbonpercent[i2]+1,"{:d}%".format(int(round(ccarbonpercent[i2]))),color="C2")
ax.arrow(cnumpercent[i2]+5,3,19.5,0,head_width=0.5,color="C2")
ax.arrow(cnumpercent[i2]+5.2,3,-4,0,head_width=0.5,color="C2")

# A FEW COUNTRY NAMES
for j in [76,80]:
    ax.text(cnumpercent[j-1]+1, ccarbonpercent[j-1]+2,names[j], rotation=90, fontsize=8)

# A FEW COUNTRIES NUMBERED
n_countries1 = [1,10,11,12,24,30,38,74]
n_countries2 = [83,89,90,107]
for n,j in enumerate(n_countries1):
    ax.text(cnumpercent[j-1]+0.2, ccarbonpercent[j-1]+0.5,chr(97+n), fontsize=5)

for n,j in enumerate(n_countries2):
    ax.text(cnumpercent[j-1]+0.2, ccarbonpercent[j-1]+0.5,chr(97+n+len(n_countries1)), fontsize=5)

# RECTANGLES
ax.fill_between(x,y1,y2,alpha=0.3,color="k")

# LEGEND
countrynames = ["      {:s}".format(names[n]) for i,n in enumerate(n_countries1+n_countries2)]
ax.legend([l1,]*len(countrynames),countrynames,title="Countries",loc=2,handlelength=0,fontsize=7)

for i,n in enumerate(n_countries1+n_countries2):
    ax.text(4,91.4-3.535*i,chr(97+i),fontsize=7,color="k",zorder=10)


ax.set_xlim(0.0,100.0)
ax.set_ylim(0.0,100.0)

ax.set_title("Sorted carbon emissions",loc="left")

ax.set_xlabel("% of participants by per capita emission")
ax.set_ylabel("% of total emissions")

plt.tight_layout()
plt.savefig("carbon_sorted.png",dpi=200)
plt.close(fig)