# Travel carbon footprint of EGU General Assembly 2019

# Abstract

16273 scientists from 113 countries [1](https://egu2019.eu/#CountryStatistics) participated in the [EGU General Assembly 2019](https://www.egu2019.eu/) in Vienna, Austria. We estimate that these scientists travelled in total 94 million km to Vienna and back, which emitted 22302 tC02e, an average of ca 1.4 tCO2e per scientist. 86% of these carbon emissions result from long-haul flights (>1500km), 13% from short-haul and <1% from rail journeys. Scientists from China and the United States are responsible for 40% of emissions. Assuming that short-haul flights could be replaced by rail, reduces the carbon footprint by 11.5% to 19750 tCO2e, as contributions from countries like Germany, UK, France, Italy, Benelux and Scandinavia are reduced by a factor of 7.

# Data

 Data is based on https://egu2019.eu/#CountryStatistics.
 
 The processed data (Coordinates of departure location, distance to Vienna etc.) can be found in [data/data_processed.xlsx](https://github.com/milankl/CarbonFootprintEGU/blob/master/data/data_processed.xlsx)

# Methods

## 1. Departure location

The departure location per country is chosen as the capital / largest city (see [data](https://github.com/milankl/CarbonFootprintEGU/data/data_processed.xlsx)), with a few exceptions that are explained in the following

  a) Germany: Participants from Germany are split into 4 groups (Berlin 20%, Hamburg 20%, Munich 20%, Cologne 40%) to better represent the participant distribution and their distance to Vienna across Germany.
  
  b) United Kingdom: For same reasoning split into 2 groups (London 70%, Manchester 30%)
  
  c) United States: Washington DC 70%, Los Angeles 30%
  
  d) Austria: Vienna 50%, Graz 50%. Graz has a relatively high number to account for journey distances of participants from Innsbruck, Salzburg, etc.

  e) Canada: Toronto 80%, Vancouver 20%
  
## 2. Retour

Every participant is assumed to travel back to their departure location with the same mode of transport.
  
## 3. Mode of transport

Rail is assumed for all journeys with distances of less than 700km. Airplanes are assumed for longer distances. Short-haul is defined as distances of less than 1500km, longer distances are long-haul.

## 4. Carbon emissions

Rail journeys are assumed to emit 30gCO2e / km / person. 
[[ecopassenger.org](http://ecopassenger.hafas.de/hafas-res/download/Ecopassenger_Methodology_Data.pdf), 
[cer.be](http://www.cer.be/sites/default/files/publication/Facts%20and%20figures%202014.pdf), 
[eea.europa.eu](https://www.eea.europa.eu/data-and-maps/indicators/energy-efficiency-and-specific-co2-emissions/energy-efficiency-and-specific-co2-9)]

Short haul journeys are assumed to emit 200gCO2e / km / person, long haul journeys are assumed to emit 250gCO2e / km / person.
[[atmosfair.de](https://www.atmosfair.de/wp-content/uploads/atmosfair-flight-emissions-calculator-englisch-1.pdf),
[icao.int](https://www.icao.int/environmental-protection/CarbonOffset/Documents/Methodology%20ICAO%20Carbon%20Calculator_v10-2017.pdf)]

## 5. Scenarios

We want to compare the realistic assumptions above to a scenario where every participant with a distance of less than 1500km takes the train.
