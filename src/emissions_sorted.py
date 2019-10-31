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

names = names[args][::-1]
carbon = carbon[args][::-1]
numbers = numbers[args][::-1]

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
i1 = 29
l1, = ax.plot([cnumpercent[i1],cnumpercent[i1]],[0,ccarbonpercent[i1]],"C0")
ax.plot([0,cnumpercent[i1]],[ccarbonpercent[i1],ccarbonpercent[i1]],"C0")
ax.text(cnumpercent[i1]+1,4,"{:d}%".format(int(cnumpercent[i1])),rotation=90,color="C0")
ax.text(1,ccarbonpercent[i1]+1,"{:d}%".format(int(ccarbonpercent[i1])),color="C0")

# SCENARIO 2
i2 = 46
ax.plot([cnumpercent[i2],cnumpercent[i2]],[0,ccarbonpercent[i2]],"C2")
ax.plot([0,cnumpercent[i2]],[ccarbonpercent[i2],ccarbonpercent[i2]],"C2")
ax.text(cnumpercent[i2]+1,4,"{:d}%".format(int(cnumpercent[i2])),rotation=90,color="C2")
ax.text(1,ccarbonpercent[i2]+1,"{:d}%".format(int(ccarbonpercent[i2])),color="C2")

# A FEW COUNTRY NAMES
for j in [30,34]:
    ax.text(cnumpercent[j-1]+1, ccarbonpercent[j-1]+2,names[j], rotation=90, fontsize=8)

# A FEW COUNTRIES NUMBERED
n_countries1 = [3,20,21,27,36]
n_countries2 = [41,72,80,86,98,99]
for n,j in enumerate(n_countries1):
    ax.text(cnumpercent[j-1]+0.2, ccarbonpercent[j-1]+0.5,"{}".format(n+1), fontsize=5)

for n,j in enumerate(n_countries2):
    ax.text(cnumpercent[j-1]+0.2, ccarbonpercent[j]+0.5,"{}".format(n+len(n_countries1)+1), fontsize=5)

# RECTANGLES
ax.fill_between(x,y1,y2,alpha=0.3,color="k")

countrynames = ["{:d} {:s}".format(i+1,names[n]) for i,n in enumerate(n_countries1+n_countries2)]
ax.legend([l1,]*len(countrynames),countrynames,title="Countries",loc=4,handlelength=0,fontsize=7)

ax.set_xlim(0.0,100.0)
ax.set_ylim(0.0,100.0)

ax.set_title("Sorted carbon emissions",loc="left")

ax.set_xlabel("% of highest emitting participants")
ax.set_ylabel("% of total emissions")

plt.tight_layout()
plt.savefig("carbon_sorted.png",dpi=200)
plt.close(fig)