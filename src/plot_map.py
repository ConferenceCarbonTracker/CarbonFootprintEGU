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
        return 1e4

vienna_lon = 16.3725042
vienna_lat = 48.2083537

##
fig = plt.figure(figsize=(6,6))

#proj = AziEqui(central_latitude=vienna_lat,central_longitude=vienna_lon)
proj = ccrs.AzimuthalEquidistant(central_latitude=vienna_lat,central_longitude=vienna_lon)

ax = fig.add_subplot(1,1,1,projection=proj)

ax.add_feature(cfeature.OCEAN,facecolor="#97BACD")
ax.add_feature(cfeature.LAND,facecolor="white")

nums = np.array([10,50,100,500,1000,2000])
lws = [0.5,1,1.5,2,2.5,3]
mss = [1,2,3.5,5,6.5,8]

colr = "#D71455"

for i in range(n):
    lon = df["Longitude"].iloc[i]
    lat = df["Latitude"].iloc[i]
    num = df["Numbers"].iloc[i]*df["Fraction"].iloc[i]
    
    lw = lws[np.argmin(num > nums)]
    ms = mss[np.argmin(num > nums)]
    
    ax.plot([lon, vienna_lon], [lat, vienna_lat], "o-",c=colr,ms=ms, transform=ccrs.Geodetic(), lw=lw, alpha=.6)


# for legend
ax.plot([0,0],[0,0],"o-",c=colr,ms=mss[0], lw=lws[0], label="1-10")
ax.plot([0,0],[0,0],"o-",c=colr,ms=mss[1], lw=lws[1], label="11-50")
ax.plot([0,0],[0,0],"o-",c=colr,ms=mss[2], lw=lws[2], label="50-100")
ax.plot([0,0],[0,0],"o-",c=colr,ms=mss[3], lw=lws[3], label="100-500")
ax.plot([0,0],[0,0],"o-",c=colr,ms=mss[4], lw=lws[4], label="500-1000")
ax.plot([0,0],[0,0],"o-",c=colr,ms=mss[5], lw=lws[5], label="1000+")

ax.set_title("Travel routes to EGU19",loc="left")
plt.legend(loc=1,title="# of participants")

plt.tight_layout()

plt.show()