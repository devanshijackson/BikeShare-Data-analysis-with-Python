import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
        (str) time_period - time period to filter by--month, day or none
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    have_city = False
        
    while (have_city != True) :
        city = input('\nWould you like to see data for Chicago, New York, or Washington?\n')
        city = city.lower()
        print('Processing data for {}.\n'.format(city))
        if (city == 'chicago' or city == 'new york' or city == 'washington'):
            have_city = True
            # get user input for time period (month, day or none)
            have_time = False
            while (have_time != True):
                time_period = input('\nWould you like to filter the data by month, day, or not at'
                                ' all? Type "none" for no time filter.\n')
                time_period.lower()

                #get user input for month (all, january, february, ... , june)
                if time_period == 'month':
                    corr_mo_name = False
                    have_time = True
                    day = 'all'
                    while (corr_mo_name != True):
                        month_name = ['january','february','march','april','may','june']
                        month = input('\nWhich month? January, February, March, April, May, or June?\n')
                        month = month.lower()
                        if month in month_name:
                            corr_mo_name = True
                        else:
                          print('Enter correct month name.\n')

                # get user input for day of week (all, monday, tuesday, ... sunday)
                elif time_period == 'day':
                    corr_d_name = False
                    have_time = True
                    month = 'all'
                    while (corr_d_name != True):
                      day = input('\nWhich day (Monday = 0, Sunday = 6) Please type your response as an integer.\n')
                      day = int(day)
                      if (0 <= int(day) <= 6):
                        corr_d_name = True
                      else:
                        print('Enter correct day (Monday = 0, Sunday = 6)  as an integer.\n')
                #if no filtering then set month and day to all
                elif time_period == 'none':
                  have_time = True
                  month = 'all'
                  day = 'all'
                else:
                  print('Type valid selection.\n')

        else:                   
          print('Invalid city.  To exit the bikeshare project press Ctr+D \n')

    print('-'*40)
    return city, month, day, time_period


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # filter by month if applicable
    if month != 'all':
      # use the index of the months list to get the corresponding int
      months = ['january', 'february', 'march', 'april', 'may', 'june']
      month = months.index(month) + 1
      df = df[df['Start Time'].dt.month == month]
    
    # filter by day of week if applicable
    if day != 'all':
      df = df[df['Start Time'].dt.weekday == day]

    return df


def time_stats(df,filter_by):
    """Displays statistics on the most frequent times of travel.
    Args:
    	df - Pandas DataFrame containing city data filtered by month and day
        (str) filter_by - time period to filter by--month, day or none         
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
	
    # display the most common month
    most_common = df['Start Time'].dt.strftime('%B').value_counts()
    print('Most Frequent Start Month:{}  Count:{}  Filter:{}'.format(most_common.index[0],most_common.iloc[0],filter_by))
    
    # display the most common day of week
    most_common = df['Start Time'].dt.weekday_name.value_counts()
    print('Most Frequent Start Day:{}  Count:{}  Filter:{}'.format(most_common.index[0],most_common.iloc[0],filter_by))
            
    # display the most common start hour(from 0 to 23)
    most_common = df['Start Time'].dt.hour.value_counts()
    print('Most Frequent Start Hour:{}  Count:{}  Filter:{}'.format(most_common.index[0],most_common.iloc[0],filter_by))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df,filter_by):
    """Displays statistics on the most popular stations and trip.
    Args:
    	df - Pandas DataFrame containing city data filtered by month and day
        (str) filter_by - time period to filter by--month, day or none         
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common = df['Start Station'].value_counts()
    print('Most Frequent Start Station:{}  Count:{}  Filter:{}'.format(most_common.index[0],most_common.iloc[0],filter_by))
   
    # display most commonly used end station
    most_common = df['End Station'].value_counts()
    print('Most Frequent End Station:{}  Count:{}  Filter:{}'.format(most_common.index[0],most_common.iloc[0],filter_by))
    
    # display most frequent combination of start and end station trip
    most_common = df['Start Station'] + ' to ' + df['End Station']
    most_common = most_common.value_counts()
    print('Most Frequent Start to End Station:{}  Count:{}  Filter:{}'.format(most_common.index[0],most_common.iloc[0],filter_by))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df,filter_by):
    """Displays statistics on the total and average trip duration.
     Args:
    	df - Pandas DataFrame containing city data filtered by month and day
        (str) filter_by - time period to filter by--month, day or none         
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time:{}  Count:{}  Filter:{}'.format(df['Trip Duration'].sum(),df['Trip Duration'].count(),filter_by))

    # display mean travel time
    print('Mean travel time:{}  Count:{}  Filter:{}'.format(df['Trip Duration'].mean(),df['Trip Duration'].count(),filter_by))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,filter_by):
    """Displays statistics on bikeshare users.
     Args:
    	df - Pandas DataFrame containing city data filtered by month and day
        (str) filter_by - time period to filter by--month, day or none         
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User Type: ')    
    user_df = df.groupby(['User Type'])['User Type'].count()
    print('Subscriber:{}  Customer:{}  Filter:{}'.format(user_df.loc['Subscriber'],user_df.loc['Customer'],filter_by))
    
      	# Display counts of gender
    if 'Gender' in df.columns:
      print('Gender data:')
      gender_df = df.groupby(['Gender'])['Gender'].count()
      print('Female:{}  Male:{}  Filter:{}'.format(gender_df.loc['Female'],gender_df.loc['Male'],filter_by))
	# Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
      print('\nEarliest birth year:', int(df['Birth Year'].min()))
      print('Most recent birth year:', int(df['Birth Year'].max()))
      print('Most common birth year:', int(df['Birth Year'].mode().loc[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_trip_data(df):
  """asks user if want to see trip data and displays individual trip data 3 rows at a time
   Args:
    	df - Pandas DataFrame containing city data filtered by month and day
    """
  
  show_data = input('\nDo you want to see individual trip data? Type yes or no\n')
  if show_data == 'yes':
    row = 0
    
    while (row < df['Start Time'].count() and show_data == 'yes'):
      for i in range(3):
        print('[')
        print(df.iloc[row,:8])
        print(']')
        row += 1
        
      show_data = input('\nDo you want to see more individual trip data? Type yes or no\n')
      

def main():
    while True:
        city, month, day, filter_by = get_filters()
        df = load_data(city, month, day)

        time_stats(df,filter_by)
        station_stats(df,filter_by)
        trip_duration_stats(df,filter_by)
        user_stats(df,filter_by)
        display_trip_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

