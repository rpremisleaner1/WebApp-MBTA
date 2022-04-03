# WebApp-MBTA
 This is the base repo for MBTA project. Please read [instructions](instructions.md). 


# Project Wrapup 
## 1. Project Overview 
For the first part of the project, we used the ***MapQuest API*** to get the latitude and longitude value of a given place name or address and took this tuple of latitude and longitude to find the nearest station and whether it is wheelchair accessible or not using the ***MBTA V3 API***.
In order for the functions to work properly, we assumed that the user knows and enters his current location in the following format: ***60 Devonshire St Boston MA*** Without ',' as seperating values and with the city or state being 'Boston' or 'MA' we found very accurate results and neaby stations to any given address in Boston. If the user input looks different, it is still possible to get stations in Boston, but they are very likely to not be near the input location. In our Flask application we greet the user first and then direct him to our nearest station form. Once the current location is entered correctly, the user will be redirected to the result form, showing the nearest station and it's wheelchair availability. If the user entered an invalid address, the following message will pop up: ***We can't find the nearest Station based on your entry.***

## 2. Project Reflection

i. This is paragraph one 

ii. This is paragraph two 