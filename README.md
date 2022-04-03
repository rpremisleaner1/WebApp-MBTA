# Project Wrapup 
## 1. Project Overview 
For the first part of the project, we used the ***MapQuest API*** to get the latitude and longitude value of a given place name or address and took this tuple of latitude and longitude to find the nearest station and whether it is wheelchair accessible or not using the ***MBTA V3 API***.
In order for the functions to work properly, we assumed that the user knows and enters his current location in the following format: ***60 Devonshire St Boston MA*** Without ',' as separating values and with the city or state being 'Boston' or 'MA' we found very accurate results and neaby stations to any given address in Boston. If the user input looks different, it is still possible to get stations in Boston, but they are very likely to not be near the input location. In our Flask application we greet the user first and then direct him to our nearest station form. Once the current location is entered correctly, the user will be redirected to the result form, showing the nearest station and it's wheelchair availability. If the user entered an invalid address, the following message will pop up: ***We can't find the nearest Station based on your entry.***

## 2. Project Reflection

i. In general we can say, that this assignment was quite fun. Working with the different API's, reading their documentations as well as documentations about the *json* or *pprint* module, *the understanding URL* documentation, or the Flask *documentation* offered a not only a great learning opportunity but was also a fun way to gain knowlwedge and experience in working with api's and build a small application based on the results. In general, we can say that our project went well from a process point of view, we did not get stuck for too long on one part and our predefined scope was appropriate, as we got to deliver a final result we are confident in submitting. We are definitely looking forward to our final project and hope to get to use our gained knowledge in order to come up with a even better final result, a visually more appealing html web page and an application which is more resitant towards different user inputs or use cases. 

ii. As we both had different time slots because of work, different courses etc. our plan from the beginning was to work on the project independently and in our own sub-branches and then coordinate our merge with the main branch once we got to a solid solution. This worked pretty well and we were able to come up and improve our functions together in an equal way. Although we worked assynchronous most of the time, we also had several calls, discussing our progress, pointing out next steps and dividing our workload. An example for this would be that one of us started working on the flask part of the project while the other improved our functions for the first part. Overall, we are happy with the way we split the work and are looking forward working together on the final project. 