# SQLAlchemy-Challenge

# Climate analysis

------- 
# Background

Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii! 

To help with your trip planning, you need to do some climate analysis on the area. The following outlines what you need to do.


--------
# Step 1 - Climate Analysis and Exploration

To begin, we used Python and SQLAlchemy to do basic climate analysis and data exploration of the climate database.

The following analysis was completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

    - Used the hawaii.sqlite files in the Resources Folder to complete the climate analysis 
        and data exploration.

    - Used SQLAlchemy create_engine to connect to the sqlite database.

    - Used SQLAlchemy automap_base() to reflect the tables into classes and save a reference 
         to those classes called Station and Measurement.

-------
# Precipitation Analysis

    Designed a query to retrieve the date and prcp values from the last 12 months of precipitation data 
        (from the most recent date in the database).There are more than one prcp value for each date. 
        Calculated the average of these values so we have a single prcp value per date.

    Loaded the query results into a Pandas DataFrame and set the index to the date column.

    Sorted the DataFrame values by date.

    Plotted the results using the DataFrame plot method.

    Used Pandas to print the summary statistics for the precipitation data.
    
    
-------- 
# Station Analysis

    Designed a query to calculate the total number of stations.

    Designed a query that lists all stations with their corresponding observation count in 
        descending order. 
        Which station is the most active (i.e., has the greatest number of observations)?

    Designed a query to retrieve the last 12 months of temperature observation data (TOBS) 
        for the most active station.

    Plotted the results as a histogram with bins=12.


--------------
# Step 2 - Climate App

In addition to the initial analysis, we can also design a Flask API based on the queries that we have just developed.

    Use Flask to create our routes.

Routes
    /

        Home page.

        List all routes that are available.

    /api/v1.0/precipitation
        Using the query from part 1 (most recent 12 months of precipitation data), convert 
            the query results to a dictionary using date as the key and prcp as the value.
        Return the JSON representation of your dictionary (note the specific format of our 
            dictionary as required from above).

    /api/v1.0/stations
        Return a JSON list of stations from the dataset.

    /api/v1.0/tobs

        Query the dates and temperature observations of the most active station for the 
            latest year of data.

        Return a JSON list of temperature observations (TOBS) for that year.

    /api/v1.0/<start> and /api/v1.0/<start>/<end>

        Create a query that returns the minimum temperature, the average temperature, and the
            max temperature for a given start or start-end range.
            Hint: We will need to use a function such as func.min, func.max, func.avg, and 
            func.count in your queries.

        When given the start date only, calculate min, max, and avg for all dates greater than 
            and equal to the start date.

        When given the start and the end date, calculate the min, avg, and max for dates 
            between the start and end date inclusive.

        Return a JSONified dictionary of min, max, and avg temperatures.

    
    
    
    
