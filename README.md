# Bikeshare-Data-analysis-using-Python
Used Python and bikeshare data from NYC, Chicago and Washington DC to compute and display descriptive statistics.  The program accepts
raw inputs from the user to create interactive experience from the terminal and to show data as well as statistics.

# Software needed
Need Python3, numpy and pandas to run the program, which could be installed using Anaconda.

# Datasets
The original datasets provided by https://www.motivateco.com/ was initially processed by Udacity and provided for project work in CSV
format.  The zipped up CSV files (washington.csv, new_york_city.csv and chicago.csv) will have to be downloaded in the same folder as the 
bikeshare.py file, prior to running the script.  The CSV files include randomly selected data from first six months of 2017.  
All three datafiles contain six core columns:
* Start Time (e.g., 2017-01-01 00:07:57)
* End Time (e.g., 2017-01-01 00:20:53)
* Trip Duration (in seconds - e.g., 776)
* Start Station (e.g., Broadway & Barry Ave)
* End Station (e.g., Sedgwick St & North Ave)
* User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:
* Gender
* Birth Year

# Program Steps
1.  Acquire user input about city and time filters.
2.  Display popular times of travel (i.e., occurs most often in the start time):  most common month, day of week, hour of day
3. Display popular stations and trip:  most common start station, end station,trip from start to end 
4. Display trip duration:  total travel time, average travel time
5. Display user info:  counts of each user type, counts of each gender,earliest, most recent, most common year of birth 
6.  Ask to display raw data, restart or quit

# Help sought from to accomplish project objectives
* https://pandas.pydata.org
* https://stackoverflow.com
* https://docs.python.org/3/library/functions.html
