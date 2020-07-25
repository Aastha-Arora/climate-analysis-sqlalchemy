## SQLAlchemy - Surfs Up!

Climate Analysis to plan a holiday vacation in Honolulu, Hawaii

A `SQLite database` containing the station measurements of temperature and precipitation from
Jan 2010 to Aug 2017 was provided for the analysis.

#### Step 1 - Climate Analysis and Exploration
The following analysis was done using SQLAlchemy ORM queries, Pandas, and Matplotlib.

**Precipitation Analysis**

* SQLAlchemy ORM query was designed to retrieve the last 12 months of precipitation data and load into a pandas dataframe 
* Results were plotted using matplotlib

![](https://github.com/Aastha-Arora/sqlalchemy-challenge/blob/master/Output/precipitation_distibution.png)

**Station Analysis**

* Queries was designed to calculate the total number of stations, to find the most active station
and to retrieve the last 12 months of temperature observation data (TOBS)

![](https://github.com/Aastha-Arora/sqlalchemy-challenge/blob/master/Output/temperature_distribution.png)

#### Step 2 - Climate App
A Flask App was designed based on the queries developed in Step 1 

**Flask Routes**

`/(Home page)`
  * Lists all routes that are available.
  
`/api/v1.0/precipitation`
  * Query results were converted to a dictionary using `date` as the key and `prcp` as the value 
  and the JSON representation of your dictionary was returned.

`/api/v1.0/stations`
  * Returns a JSON list of stations from the dataset.

`/api/v1.0/tobs`
  * Queries the dates and temperature observations of the most active station for the last year of data 
  and returns a JSON list of temperature observations (TOBS) for the previous year.

`/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`
  * Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
  * When given the start only, `TMIN`, `TAVG`, and `TMAX` is calculated for all dates greater than and equal to the start date.
  * When given the start and the end date, `TMIN`, `TAVG`, and `TMAX` is calcululated for dates between the start and end date inclusive.
  
 #### Additional Analysis
 
 **Temperature Analysis I**
Analyzed if there was a meaningful difference between the temperature in June and December. 
An independent t-test (unpaired test) was used to compare the means of two independent groups.
Assuming a 5% significance level, the Null Hypothesis was rejected as pvalue < 0.05
 
 **Temperature Analysis II**
 
 The minimum, average, and maximum temperatures for a range of dates was calculated and ploted. 
 Average temperaturewas plotted as the bar height. Peak-to-peak (TMAX-TMIN) value was used as the y error bar (YERR).
 
 ![](https://github.com/Aastha-Arora/sqlalchemy-challenge/blob/master/Output/Trip%20Avg%20Temp.png)
 
 **Daily Rainfall Average**
 
 The rainfall per weather station was calculated using the previous year's matching dates.
 Daily normals (the averages for the min, avg, and max temperatures) were also calculated and ploted using an area plot.
 
 ![](https://github.com/Aastha-Arora/sqlalchemy-challenge/blob/master/Output/Daily_Normal_Temperature.png)
