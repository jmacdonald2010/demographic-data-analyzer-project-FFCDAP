import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round((df.loc[df['sex'] == 'Male', 'age'].mean()), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((len(df.loc[df['education'] == 'Bachelors'].index) / len(df.index) * 100), 1) # not sure if they want it 0-100 or 0-1 for percentages

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = len(df.loc[((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'))])
    lower_education = len(df.loc[((df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate'))])

    # percentage with salary >50K
    higher_education_rich = round((len(df.loc[((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')) & (df['salary'] == '>50K')]) / higher_education * 100), 1)
    lower_education_rich = round((len(df.loc[((df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')) & (df['salary'] == '>50K')]) / lower_education * 100), 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df.sort_values('hours-per-week').iloc[0, 12]

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = round((len(df.loc[df['hours-per-week'] == min_work_hours])), 1)

    rich_percentage = round((len(df.loc[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')]) / num_min_workers * 100), 1)

    # What country has the highest percentage of people that earn >50K?
    gt50ks = df.loc[(df['salary'] == '>50K'), 'native-country'].value_counts()
    country_series = df[['native-country']].value_counts()
    # greater than 50k salary percentages (by country)
    gt50ks_percents = pd.Series()
    for i, v in gt50ks.iteritems():
        gt50ks_percents[i] = (gt50ks[i] / country_series[i]) * 100
    gt50ks_percents = gt50ks_percents.max(level=0)  # used to clean up the series so .idxmax() works
    highest_earning_country = gt50ks_percents.idxmax()
    highest_earning_country_percentage = round((len(df.loc[((df['native-country'] == highest_earning_country) & (df['salary'] == '>50K'))]) / len(df.loc[(df['native-country'] == highest_earning_country)]) * 100), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
