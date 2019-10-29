import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import pandas as pd

## read data
path = "Dropbox/CarbonFootprintEGU/data/"
df = pd.read_excel(path+"data_processed.xlsx")

n = len(df["City"])

## Great circle, equi-distant projection
# higher resolution for great circles
class AziEqui(ccrs.AzimuthalEquidistant):

    @property
    def threshold(self):
        return 1e3

vienna_lon = 16.3725042
vienna_lat = 48.2083537

##
fig = plt.figure(figsize=(6,6))

#proj = AziEqui(central_latitude=vienna_lat,central_longitude=vienna_lon)
proj = ccrs.AzimuthalEquidistant(central_latitude=vienna_lat,central_longitude=vienna_lon)

ax = fig.add_subplot(1,1,1,projection=proj)

ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.LAND,facecolor="white")

nums = np.array([10,50,100,500,1000,2000])
lws = [0.5,1,1.5,2,3,4]

for i in range(n):
    lon = df["Longitude"].iloc[i]
    lat = df["Latitude"].iloc[i]
    num = df["Numbers"].iloc[i]*df["Fraction"].iloc[i]
    
    lw = lws[np.argmin(num > nums)]
    
    ax.plot([lon, vienna_lon], [lat, vienna_lat], "C3", transform=ccrs.Geodetic(), lw=lw, alpha=.6)


# for legend
ax.plot([0,0],[0,0],"C3", lw=lws[0], label="1-10")
ax.plot([0,0],[0,0],"C3", lw=lws[1], label="11-50")
ax.plot([0,0],[0,0],"C3", lw=lws[2], label="50-100")
ax.plot([0,0],[0,0],"C3", lw=lws[3], label="100-500")
ax.plot([0,0],[0,0],"C3", lw=lws[4], label="500-1000")
ax.plot([0,0],[0,0],"C3", lw=lws[5], label="1000+")

ax.set_title("Participants of EGU 2019",loc="left",fontsize=20)
plt.legend(loc=4,title="# of participants")

plt.tight_layout()

plt.show()