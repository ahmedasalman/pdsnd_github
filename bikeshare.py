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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputsd
    while True:
        city=input('please enter city (chicago, new york city, washington): ').lower()
        if city in CITY_DATA:
            break
        else:
            print('invalid input')
    # TO DO: get user input for month (all, january, february, ... , june)
    valid_months=['all','january','february','march','april','may','june']
    while True:
        month=input('please enter month(all, january, february, ... , june): ').lower()
        if month in valid_months:
            break
        else:
            print('invalid input')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    valid_days=['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    while True:
        day=input('please enter day of the week(all, monday, tuesday, ... sunday): ').lower()
        if day in valid_days:
            break
        else:
            print('invalid input')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):


    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':

        # use the index of the months list to get the corresponding int

        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    #Displays statistics on the most frequent times of travel.

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    allmonths=['january','february','march','april','may','june']
    popular_month = df['month'].mode()[0]
    print('Most common month: ', allmonths[int(popular_month-1)])

    # TO DO: display the most common day of week

    popular_day_ow = df['day_of_week'].mode()[0]
    print('Most common day of week: ', popular_day_ow)

    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def print_raw_data(df):
    n=0
    df.pop('Start Time')
    df.pop('day_of_week')
    df.pop('month')
    df.pop('hour')
    while True:
        raw_data=input('would you like to see some raw data?').lower()
        if raw_data=='yes':
            print("\n{}".format(df.iloc[n:n+5,:]))
            n=n+5
        elif raw_data=='no':
            break
        else:
            print('invalid input')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        print_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
