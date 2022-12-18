import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def verification(input_str,input_type):
    """ 
    input_str: is the input of the user
    input_type: is the type of input: 1 = city, 2 = month, 3 = day
    """
    while True:
        input_read=input(input_str).lower()
        try:
            if input_read in ['chicago','new york city','washington',] and input_type == 1:
                break
            elif input_read in ['january', 'february', 'march', 'april', 'may', 'june', 'all',] and input_type == 2:
                break
            elif input_read in ['sunday', 'monday','tuesday','wednesday','thursday','friday','saturday','all',] and input_type == 3:
                break
            else:
                if input_type == 1:
                    print("Error, Choose from the list: chicago new york city or washington")
                if input_type == 2:
                    print("Error, Choose from the list: january, february, march, april, may, june or all")
                if input_type == 3:
                    print("Error,Choose from the list: sunday, ... saturday or all")
        except ValueError:
            print("your input is wrong")
    return input_read

def get_filters():
   
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = verification("Choose a city (chicago , new york city , washington)? ", 1)

    # TO DO: get user input for month (all, january, february, ... , june)

    month = verification("Choose month or all? ", 2)
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = verification("Choose day or all? ", 3)

    print('-'*60)
    return city, month, day


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
    #load data
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    df['hour'] = df['Start Time'].dt.hour
    
       # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]

    print('Most Common Month:', common_month)

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]

    print('Most Day Of Week:', common_day_of_week)

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]

    print('Most Common Start Hour:', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]

    print('Most Start Station:', common_start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]

    print('Most End Station:', end_station)

    # TO DO: display most frequent combination of start station and end station trip
    group_field=df.groupby(['Start Station','End Station'])
    combination_station = group_field.size().sort_values(ascending=False).head(1)
    print('Most frequent combination of Start Station and End Station trip:\n', combination_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('User Type Stats:')
    print(df['User Type'].value_counts())
    if city != 'washington':

    # TO DO: Display counts of gender
       gender = df['Gender'].value_counts()
       print('Gender Stats:', gender)

    # TO DO: Display earliest, most recent, and most common year of birth
       print('Birth Year Stats:')
       most_common_year = df['Birth Year'].mode()[0]
       print('Most Common Year:',most_common_year)
        
       most_recent_year = df['Birth Year'].max()
       print('Most Recent Year:',most_recent_year)
        
       earliest_year = df['Birth Year'].min()
       print('Earliest Year:',earliest_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
