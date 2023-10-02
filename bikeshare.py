import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city = str(input("Enter the name of the city. Either chicago, new york city, or washington: ")).lower()
    while city not in ('chicago', 'new york city', 'washington'):
        print("You have not entered the correct data")
        city = str(input("Enter the name of the city. Either chicago, new york city, or washington: "))
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month = str(input("Enter the month name (Not Exceeding June) to filter by, or 'all' to apply no month filter: ")).lower()
        
    while month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
        print("You have not entered the correct data")
        month = str(input("Enter the name of the month (Not Exceeding June) to filter by,or 'all' to apply a no month filter: "))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = str(input("Enter the day of the week to filter by, or 'all' to apply no day filter: ")).lower()
        
    while day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
        print("You have not entered the correct data")
        day = str(input("Enter the day of the week to filter by, or 'all' to apply no day filter: "))

    print('-'*40)
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
    
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])       
    
    df['Month'] = df['Start Time'].dt.month
    if month != 'all': 
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
         
        df = df[df['Month'] == month]
        
    
    df['dow'] = df['Start Time'].dt.weekday_name
    df['dow'] = df['dow'].str.lower()
    if day != 'all': 
        df = df[df['dow'] == day]  
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    """
    To the reviewer;
    I am a little confused by the question in line 80 which asks for the most common month, yet the data has been filtered to only show data belonging to one month (if that is what the user has chosen). 
    What confuses me is that how can we show the most common of something if it is the only one there is.
    This is the same for the most common day of the week below.
    Because of this, I have chosen to first get the unique values from the columns month and dow and to give the mode if there are more that 1 unique values.
    Alternatively, just incase, I have not understood the question correctly, I have provided another answer to the question but i have commented them.
    I will really appreciate it if you pay attention to both the answers and give me your feedback on them and how to best understand the question.
    """
    
    # OPTION 1 ANSWER
    month_dict = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June'}
    try:
        if len(set(df['Month'].values)) > 1:
            most_commom_month = df['Month'].mode()[0]
            print('The most common month is: ',month_dict.get(most_commom_month), '\n')
        else:
            print('The data has been filetered to only contain one month hence there is no mode \n')              
    except:
        print('The data has been filetered to only contain one month hence there is no mode')        
    
    # OPTION 2 ANSWER
    """
    most_commom_month = df['Month'].mode()[0]
    print('The most common month is: ',month_dict.get(most_commom_month), '\n')
    """
    
    # TO DO: display the most common day of week
    # OPTION 1 ANSWER
    try:
        if len(set(df['dow'])) > 1:
            most_common_day = df['dow'].mode()[0]
            print('The most common day of the week is: ',most_commom_month, '\n')
        else:
            print('The data has been filetered to only contain one day of the week hence there is no mode', '\n')              
    except:
        print('The data has been filetered to only contain one day of the week hence there is no mode') 
      
    #OPTION 2 ANSWER
    """
    most_common_day = df['dow'].mode()[0]
    print('The most common day of the week is: ',most_commom_month, '\n')
    """
    
    # TO DO: display the most common start hour
    df['hour_data'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour_data'].mode()[0]
    
    print('The most common start hour is: ',most_common_start_hour, '\n')
    print("\nThis took %s seconds." % (time.time() - start_time))
    #print(df.head(10))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    
    #Printing the most common start station
    print('The most common start station is: ',most_common_start_station, '\n')

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    
    #Printing the most common end station
    print('The most common end station is: ',most_common_end_station, '\n')

    # TO DO: display most frequent combination of start station and end station trip
    df['Start and End Station Combination'] = df['Start Station'] + ',' + df['End Station']
    most_frequent_combination = df['Start and End Station Combination'].mode()[0]
    
    print('The most common frequent combination of start station and end station trip is: ',most_frequent_combination, '\n')
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])    
    travel_time = df['End Time'] - df['Start Time']

    user_input = str(input('Would you like to view 5 rows of individual total travel time data?(yes/no): \n')).lower()
    iteration = 0
    while user_input not in ('yes','no'):
        print('You have not entered the correct data')
        user_input = str(input('Would you like to view 5 rows of individual total travel time data?(yes/no): \n')).lower()
        
    if user_input == 'yes':
        while True:
            print("The total travel times for the 5 rows are: \n")
            print(travel_time.iloc[iteration:iteration+5])
            iteration += 5 
            next_5rows = str(input('Would you like to view the next 5 rows of data?(yes/no): ')).lower()
            if next_5rows == 'no':
                break
    elif user_input == 'no':
        print("The total travel time is: ", travel_time)
    
    # TO DO: display mean travel time
    mean_travel_time = travel_time.mean()
    
    print("The mean travel time is: ", mean_travel_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df["User Type"].value_counts()
    
    print("The counts of user types are: \n", user_types)

    # TO DO: Display counts of gender
    if city != 'washington':
        gender_types = df["Gender"].value_counts()
    
        print("The counts of gender types are: \n", gender_types)


        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_yob = min(df["Birth Year"])
        most_recent_yob = max(df["Birth Year"])
        most_common_yob = df["Birth Year"].mode()[0]

        print("The earliest year of birth is", int(earliest_yob))
        print("The most recent year of birth is", int(most_recent_yob))
        print("The most common year of birth is", int(most_common_yob))
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


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
