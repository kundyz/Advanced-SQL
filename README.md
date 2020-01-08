# Surfs Up!
![logo](/images/logo.jpeg)

Task
* Use the provided starter notebook and hawaii.sqlite files to complete your climate analysis and data exploration.
* Choose a start date and end date for your trip. Make sure that your vacation range is approximately 3-15 days total.
* Use SQLAlchemy create_engine to connect to your sqlite database.
* Use SQLAlchemy automap_base() to reflect your tables into classes and save a reference to those classes called Station and Measurement.
* Design a query to retrieve the last 12 months of precipitation data.
* Select only the date and prcp values.
* Load the query results into a Pandas DataFrame and set the index to the date column.
* Sort the DataFrame values by date.
* Plot the results using the DataFrame plot method.
* Use Pandas to print the summary statistics for the precipitation data.
* Design a query to calculate the total number of stations.
* Design a query to find the most active stations.
** List the stations and observation counts in descending order.


Which station has the highest number of observations?


Hint: You may need to use functions such as func.min, func.max, func.avg, and func.count in your queries.




Design a query to retrieve the last 12 months of temperature observation data (tobs).


Filter by the station with the highest number of observations.


Plot the results as a histogram with bins=12.
