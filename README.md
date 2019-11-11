[![DOI](https://zenodo.org/badge/218331367.svg)](https://zenodo.org/badge/latestdoi/218331367)
# Travel carbon footprint of the EGU General Assembly 2019
*How much carbon dioxide does travelling to the annual EGU General Assembly emit and how it can be reduced to less than 5% of current emissions in short time.*


**Milan Klöwer**\
Atmospheric, Oceanic and Planetary Physics, University of Oxford\
*milan.kloewer@physics.ox.ac.uk*

For comments and changes, please raise an [issue](https://github.com/milankl/CarbonFootprintEGU/issues) or create a pull request.

## Summary

16,273 scientists from 113 countries participated in the [European Geoscience Union's (EGU) General Assembly 2019](https://egu2019.eu) in Vienna, Austria. We estimate that these scientists travelled in total 94 million km to Vienna and back, which emitted 22,300 tC02e, an average of ca 1.4 tCO2e per scientist. 86% of these carbon emissions result from long-haul flights (>1500km), 13% from short-haul (between 700 and 1500km) and <1% from rail journeys (<700km). Scientists from China and the United States are responsible for 40% of emissions. If all short-haul flights were replaced by rail journeys the total travel carbon footprint would be reduced by 11.5% down to 19,750 tCO2e. If the equivalent of the 9% highest emitting participants would participate virtually, then the carbon emissions would be reduced by 34%. Virtual participation for 26% of the highest emitting participants would reduce the carbon footprint by 80%. An EGU General Assembly with most European scientists arriving by train and 26% virtual participation reduces the current travel carbon emissions by 91%. Combining this scenario with a completely virtual format every other year, travel emissions to the EGU General Assembly would be reduced by 96% to less than 1000 tCO2e.

## 1. Introduction

International aviation is projected to contribute 22% to global greenhouse gas emissions in 2050 [[1](http://www.europarl.europa.eu/RegData/etudes/STUD/2015/569964/IPOL_STU(2015)569964_EN.pdf)], as doubling of passengers is expected by 2036 [[2](https://www.iata.org/pressroom/pr/Pages/2017-10-24-01.aspx)]. In Paris 2015, world governments have agreed to keep the global temperature increase well below 2°C [[3](https://treaties.un.org/doc/Treaties/2016/02/20160215%2006-03%20PM/Ch_XXVII-7-d.pdf)], which requires drastic reductions in greenhouse gas emissions. Universities and other research institutions are high emitters [[4](https://tyndall.ac.uk/sites/default/files/twp161.pdf)], with individual carbon emissions an order of magnitude larger [[5](https://www.sciencedirect.com/science/article/pii/S0959652619311862)] than the suggested personal carbon allowance [[6](https://wordpress.hotorcool.org/wp-content/uploads/2019/02/15_Degree_Lifestyles_MainReport.pdf), [7](https://iopscience.iop.org/article/10.1088/1748-9326/aa7541/pdf), [8](https://www.sciencedirect.com/science/article/pii/S0969699719303229)]. Research-associated carbon emissions are dominated by air travel to conferences, meetings and for fieldwork [[4](https://tyndall.ac.uk/sites/default/files/twp161.pdf)]. Recent studies suggest that academic air travel has limited direct link to professional success [[5](https://www.sciencedirect.com/science/article/pii/S0959652619311862), [9](https://www.tandfonline.com/doi/full/10.1080/17450101.2019.1589727)].

Most conferences do not provide live-streaming, nor allow for remote-speaking, although alternatives exist. Very few conferences are fully virtual (e.g. [virtual island summit](https://www.islandinnovation.co/summit/)) and therefore often almost carbon neutral [[10](https://hiltner.english.ucsb.edu/index.php/ncnc-guide/)]. Continuous virtual seminar series allow for frequent academic exchange (e.g. [Virtual Blue COP 25](https://virtualbluecop25.org/)) sometimes with a focus on field-specific subjects (e.g. [EBUS Webinars](https://ebuswebinars.wixsite.com/ebuswebinars)). Live-streaming is provided by more conferences (e.g. [JuliaCon](https://juliacon.org/2019/), with an automatic archive on [YouTube](https://www.youtube.com/playlist?list=PLP8iPy9hna6StY9tIJIUN3F_co9A0zh0H)), mainly to make them more accesible for participants with constraints on time, money, or freedom of travel.

The carbon footprint of most conferences and meetings is dominated by a small amount of participants with disproportionate travel emissions due to long distance flights [[11](https://dx.doiorg/10.1038/news031208-13),[12](https://dx.doi.org/10.1126/science.318.5847.36)]. For the EGU General Assembly 2012 it was estimated that 20% of the highest emitting participants are responsible for 70% of the travel emissions [[4](https://tyndall.ac.uk/sites/default/files/twp161.pdf)]. Here, we calcuate the travel emissions for the same conference in 2019 and present reduction scenarios based on an increased number of rail journeys and virtual participation.

## 2. Results
![](https://github.com/milankl/CarbonFootprintEGU/blob/master/plots/world.png)

Figure 1: The journeys of all 16,273 scientists are illustrated on an equi-distant map, which preserves the distances with respect to Vienna. Line thicknesses are weighted by the amount of participants per country. Capital cities or largest cities are assumed as the departure location, with a few exceptions (see section [4.1](https://github.com/milankl/CarbonFootprintEGU#41-departure-location)). The total distance travelled is ca 94 million km. A version of this Figure covering only Europe can be found [here](https://github.com/milankl/CarbonFootprintEGU/blob/master/plots/europe.png).

![](https://github.com/milankl/CarbonFootprintEGU/blob/master/plots/CO2_permode.png)

Figure 2: a) Splitting the total carbon footprint of 22,300 tCO2e into the modes of transport shows that long-haul flights are the major contributor with 86%. Contribution of rail journeys are less than 1%. b) A scenario, in which all short-haul flights are replaced with rail journeys, decreases the carbon footprint by 11.5% to 19,750 tCO2e. This scenario makes long-haul flights the dominating contribution to the overall carbon footprint with 97% and the emissions from rail journeys are negligible (<3%).

![](https://github.com/milankl/CarbonFootprintEGU/blob/master/plots/CO2_percountry.png)

Figure 3: a) China (1194 scientists) and USA (1068) are the biggest contributors, due to large number of participants and large distances to Vienna. Although many scientists come from Germany (2587), UK (1355), Italy (1191), France (1151), Austria (754), and Switzerland (723), their contribution is minor due to short distances to Vienna, despite short-haul flights. On the other hand, 51 scientists (0.3% of participants) from New Zealand contribute 2% of the overall carbon emissions. b) A scenario, in which short-haul flights are replaced with rail journeys, decreases the carbon emissions from the United Kingdom, Germany, France by a factor of 7, which results from the assumptions on carbon emission per mode of transport (30gCO2e / km / person for rail versus 200gCO2e / km / person for short-haul (see section [4.5](https://github.com/milankl/CarbonFootprintEGU#45-carbon-emissions)). Same holds for other countries in regions like Benelux, Scandinavia and Eastern Europe (incl. South-East and North-East, like Greece, Turkey, Romania, Estonia, Bulgaria, Latvia and Ukraine, to name a few), although travel times from these countries may be considerable given current rail and bus infrastructure.

![](https://github.com/milankl/CarbonFootprintEGU/blob/master/plots/carbon_sorted.png)

Figure 4: Carbon emissions sorted by highest per capita emissions. Each grey rectangle represents one country, some of the largest in terms of emissions and participants are named. The 26% furthest-travelling EGU participants (green lines) are responsible for 80% of the conference's total travel carbon footprint, with the top 9% (blue lines) responsible for 34% of the total. The [Gini-coefficient](https://en.wikipedia.org/wiki/Gini_coefficient) is 63% and therefore similar to the global inequality of income.

## 3. Data

Data is based on number of participants per country, [published by EGU](https://egu2019.eu/#CountryStatistics). The processed data, including coordinates of departure location, distance to Vienna and sum of emissions per country, can be found in [`data/data_processed.csv`](https://github.com/milankl/CarbonFootprintEGU/blob/master/data/data_processed.csv)

## 4. Methods

All scripts can be found in [`src/`](https://github.com/milankl/CarbonFootprintEGU/tree/master/src) and the assumptions are discussed in section [4.6](https://github.com/milankl/CarbonFootprintEGU#46-sensitivity-to-assumptions).

### 4.1 Departure location

The departure location per country is chosen as the capital or largest city (see [data](https://github.com/milankl/CarbonFootprintEGU/blob/master/data/data_processed.csv)), with a few exceptions that are explained in the following:

  a) Germany: Participants from Germany are split into 4 groups (Berlin 20%, Hamburg 20%, Munich 20%, Cologne 40%) to better represent the participant distribution and their distance to Vienna across Germany.
  
  b) United Kingdom: For similar reasons scientists from the UK are split into 2 groups (London 70%, Manchester 30%).
  
  c) United States: Washington DC 70%, Los Angeles 30%.
  
  d) Austria: Vienna 50%, Graz 50%. Graz has a relatively high number to account for journey distances of participants from Innsbruck, Salzburg, etc.

  e) Canada: Toronto 80%, Vancouver 20%.
  
The named location `city, country` is converted to geographical coordinates with [Nominatim](https://nominatim.org/release-docs/develop/api/Overview/) from the [OpenStreetMap database](https://www.openstreetmap.org/) (see [`src/get_locations.py`](https://github.com/milankl/CarbonFootprintEGU/blob/master/src/get_locations.py)).
  
### 4.2 Retour and other conferences

Every participant is assumed to travel back to their departure location with the same mode of transport. Due to the lack of data, we have to assume that every scientists only came to Vienna for the purpose of the EGU General Assembly. Some scientists likely connected their journey to Vienna with other conferences, meetings or holidays, which has to be taken into account in case the carbon footprint of individuals or a whole research field is calculated.
  
### 4.3 Mode of transport

Rail is assumed for all journeys with distances of less than 700km. Airplanes are assumed for longer distances. Short-haul is defined as distances of less than 1500km, longer distances are long-haul.

## 4.4 Indirect journeys

We assume all journeys to be direct, that means, we calculate the distance as the great circle distance. This is more accurate for long-haul than for short-haul, and may have some considerable errors for railways, but less than a factor of 2. More in section [4.6](https://github.com/milankl/CarbonFootprintEGU#46-sensitivity-to-assumptions).

### 4.5 Carbon emissions

Rail journeys are assumed to emit 30gCO2e / km / person.
[[13](http://ecopassenger.hafas.de/hafas-res/download/Ecopassenger_Methodology_Data.pdf),
[14](http://www.cer.be/sites/default/files/publication/Facts%20and%20figures%202014.pdf),
[15](https://www.eea.europa.eu/data-and-maps/indicators/energy-efficiency-and-specific-co2-emissions/energy-efficiency-and-specific-co2-9),
[16](https://dataportal.orr.gov.uk/media/1114/rail-infrastructure-assets-environmental-2017-18.pdf)]

Short-haul flights are assumed to emit 200gCO2e / km / person, long-haul flights are assumed to emit 250gCO2e / km / person
[[17](https://www.atmosfair.de/wp-content/uploads/atmosfair-flight-emissions-calculator-englisch-1.pdf),
[18](https://www.icao.int/environmental-protection/CarbonOffset/Documents/Methodology%20ICAO%20Carbon%20Calculator_v10-2017.pdf)]. We assume economy class for every participant.

Carbon emissions of live-streaming are assumed to be negligible.

### 4.6 Sensitivity to assumptions

Sensitivity to the assumptions is fairly low. Main contributions to the uncertainty of the carbon footprint are

a) The carbon dioxide equivalent emissions of long-haul flights: These are assumed to be 250gCO2e / km / person, which is a representative average with less than 10% error [[17](https://www.atmosfair.de/wp-content/uploads/atmosfair-flight-emissions-calculator-englisch-1.pdf),
[18](https://www.icao.int/environmental-protection/CarbonOffset/Documents/Methodology%20ICAO%20Carbon%20Calculator_v10-2017.pdf)]
. The emissions of individual flights have much higher uncertainty and depend on number of passengers, airline / flight class, type of aircraft, potential detours, flight height, and weather conditions. 

b) The exact departure location of scientists from USA: A flight from Los Angeles to Vienna emits 1.8 times more tCO2e than a flight from New York City to Vienna [[17](https://www.atmosfair.de/wp-content/uploads/atmosfair-flight-emissions-calculator-englisch-1.pdf)]. We assume that a ratio of 70% of scientists depart from Washington DC and 30% from Los Angeles is representative to account for longer journeys (but therefore probably also fewer scientists) from Midwestern, Southern USA or the West Coast. Assuming 50% of scientists from the USA depart from Washington and 50% from Los Angeles, would increase the emission of those by 17%. As the USA contribution to the overall carbon dioxide emissions of EGU travel is 20%, this uncertainty accounts for less than 4% in total.

c) The exact departure location of scientists from China: We assume that all scientists from China fly in from Beijing. A flight from Shanghai emits less than 20% more tCO2e than a flight from Beijing. Assuming half of the scientists from China flew in from Shanghai, this would increase China's emission by 10%. Taking into account that China contributes 20% to the overall emissions of EGU travel, this uncertainty is less than 2% in total.

d) Similar arguments hold for the exact departure locations of scientists from Canada, Brazil, Australia, and India. Smaller countries like New Zealand, Taiwan, South Korea, contribute even less to the uncertainty.

e) The carbon dioxide equivalent emissions of rail journeys. These are assumed to be 30gCO2e / km / person [[13](http://ecopassenger.hafas.de/hafas-res/download/Ecopassenger_Methodology_Data.pdf),
[14](http://www.cer.be/sites/default/files/publication/Facts%20and%20figures%202014.pdf),
[15](https://www.eea.europa.eu/data-and-maps/indicators/energy-efficiency-and-specific-co2-emissions/energy-efficiency-and-specific-co2-9),
[16](https://dataportal.orr.gov.uk/media/1114/rail-infrastructure-assets-environmental-2017-18.pdf)], which can be considered as an European average. Emissions from individual trains can, however, be lower by an order of magnitude depending on the type of train (electric, diesel, highspeed or regional), the local energy mix (for electric trains), number of passengers, etc. The highspeed train in France is estimated to emit only 3gCO2e / km  / person [[19](https://en.oui.sncf/en/help-en/calculation-of-co2-emissions-on-your-train-journey)], due to a very low carbon electric grid, but average trains in the UK emit 40gCO2e / km / person [[16](https://dataportal.orr.gov.uk/media/1114/rail-infrastructure-assets-environmental-2017-18.pdf)] as many services are not electrified and diesel trains are used instead. As the contribution of rail journeys to the overall carbon footprint of EGU-related travel is negligible (<1%), the uncertainty here is negligible too.

f) Indirect rail journeys. We assume great circle distances of rail journeys such that we likely underestimate the actually travelled distance. However, this error is within a factor of 2. Since the contribution of rail travel to the overall carbon emissions is very small, the resultant uncertainty in the overall budget is negligible.

# References

[1] [Cames, M, J Graichen, A Siemons, V Cook, 2015. *Emission Reduction Targets for International Aviation and Shipping*, European Parliament, Policy Department A: Economic and Scientific Policy](http://www.europarl.europa.eu/RegData/etudes/STUD/2015/569964/IPOL_STU(2015)569964_EN.pdf)

[2] [International Air Transport Association, 2017. *20 Year Passenger Forecast*](https://www.iata.org/publications/store/Pages/20-year-passenger-forecast.aspx)

[3] [Paris Agreement of the United Nations Framework Convention on Climate Change, 2016.](https://treaties.un.org/doc/Treaties/2016/02/20160215%2006-03%20PM/Ch_XXVII-7-d.pdf)

[4] [Le Quere, C, et al., 2015. *Towards a culture of low-carbon research for the 21st century*, Tyndall Centre for Climate Change Research, Working paper 161.](https://tyndall.ac.uk/sites/default/files/twp161.pdf)

[5] [Wynes, S, SD Donner, S Tannason, N Nabors, 2019. *Academic air travel has a limited influence on professional success*. **Journal of Cleaner Production**, 226, p. 959-967.](https://www.sciencedirect.com/science/article/pii/S0959652619311862)

[6] [Institute for Global Environmental Strategies, Aalto University, and D-mat ltd. 2019. *1.5-Degree Lifestyles: Targets and Options for Reducing Lifestyle Carbon Footprints*. Technical Report.Institute for Global Environmental Strategies, Hayama, Japan. ](https://wordpress.hotorcool.org/wp-content/uploads/2019/02/15_Degree_Lifestyles_MainReport.pdf)

[7] [Wynes, S and KA Nicholas, 2017. *The climate mitigation gap: education andgovernment recommendations miss the mosteffective individual actions.* **Environ. Res. Lett.**,12,074024.](https://iopscience.iop.org/article/10.1088/1748-9326/aa7541/pdf)

[8] [Goessling, S, P Hanna, J Higham, S Cohen, D Hopkins, 2019. *Can we fly less? Evaluating the ‘necessity’ of air travel*,**Journal of Air Transport Management**, 81](https://www.sciencedirect.com/science/article/pii/S0969699719303229)

[9] [Higham, JES, Hopkins D, Orchiston C, 2019. *The work-sociology of academic aeromobility at remote institutions*, **Mobilities**, 14, p. 612-631](https://www.tandfonline.com/doi/full/10.1080/17450101.2019.1589727)

[10] [Ken Hiltner, 2016. *A Nearly Carbon Neutral Conference Model*](https://hiltner.english.ucsb.edu/index.php/ncnc-guide/)

[11] [Mason, B, 2003. *Scientists contribute to greenhouse-gas emissions*, **Nature News**, doi:10.1038/news031208-13](https://dx.doi.org/10.1038/news031208-13)

[12] [Lester, B, 2007. *Greening the Meeting*. **Science**, 318, 5847, pp. 36-38, doi:10.1126/science.318.5847.36](https://dx.doi.org/10.1126/science.318.5847.36)

[13] [Knoerr, W and R Huettermann, 2016. *EcoPassenger: Environmental Methodology and Data, Update 2016*](http://ecopassenger.hafas.de/hafas-res/download/Ecopassenger_Methodology_Data.pdf)

[14] [International Railway Association UIC and Community  of  European  Railway  and  Infrastructure  Companies CER, 2016. *Rail Transport and Environment: Facts & Figures.*](http://www.cer.be/sites/default/files/publication/Facts%20and%20figures%202014.pdf)

[15] [European Environment Agency EEA, 2017. *Energy efficiency and specific CO2 emissions*](https://www.eea.europa.eu/data-and-maps/indicators/energy-efficiency-and-specific-co2-emissions/energy-efficiency-and-specific-co2-9)

[16] [UK Office of Rail and Road ORR, 2018: *Rail infrastructure, assets and environmental 2017-18 Annual Statistical Release*](https://dataportal.orr.gov.uk/media/1114/rail-infrastructure-assets-environmental-2017-18.pdf)

[17] [Atmosfair, 2016. *atmosfair Flight Emissions Calculator: Documentation of the Method and Data*](https://www.atmosfair.de/wp-content/uploads/atmosfair-flight-emissions-calculator-englisch-1.pdf)

[18] [International Civil Aviation Organization ICAO, 2017. *ICAO Carbon Emissions Calculator Methodology, Version 10*](https://www.icao.int/environmental-protection/CarbonOffset/Documents/Methodology%20ICAO%20Carbon%20Calculator_v10-2017.pdf)

[19] [OUI SNCF, 2018. *Calculation of CO2 emissions on your train journey*](https://en.oui.sncf/en/help-en/calculation-of-co2-emissions-on-your-train-journey)
