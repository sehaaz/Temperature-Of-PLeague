import pandas as pd
from Team import Team
from Temperature import Temperature
from Referee import Referee
import matplotlib.pyplot as plt
import requests
import os


# Searching the list then returns to a bool.
def search_list_bool(list, param):
    for cont in list:
        if cont.title == param:
            return True
    return False


# Search
def search_list(list, param):
    for cont in list:
        if cont.title == param:
            return cont


# Converts League Data Date to Temperature Data Date
def convert_date(date_string):
    day, month, year = date_string.split('/')
    if not int(year) > 2000:  # an exception in source .csv files
        year = '20' + year
    formatted_date = f'{year}-{month}-{day}'
    return formatted_date


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if int(arr[j].title) > int(arr[j + 1].title):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Gets the Title
def title_getter(list, title):
    for titles in list:
        if titles.title == title:
            return titles


# Gets the Temperature Data via API.
def dec_team_temp_data(team_name):
    locations_path = "Data/Locations.csv"
    locations_df = pd.read_csv(locations_path)

    for index, row in locations_df.iterrows():
        if team_name == row['Team']:
            url = "https://archive-api.open-meteo.com/v1/archive"
            latitude = row['Latitude']
            longitude = row['Longitude']
            start_date = "2000-01-01"
            end_date = "2019-12-31"
            daily_data = "temperature_2m_mean"
            timezone = "Europe/London"

            params = {
                "latitude": latitude,
                "longitude": longitude,
                "start_date": start_date,
                "end_date": end_date,
                "daily": daily_data,
                "timezone": timezone
            }

            response = requests.get(url, params=params)
            data = response.json()

            return data['daily']


# Gets the specific day Temperature Data.
def get_temp_from_data(date, team_title, teams_):
    for team in teams_:
        if team.title == team_title:
            while True:
                if date == team.home_temp_data['time'][team.home_temp_data_index]:
                    return team.home_temp_data["temperature_2m_mean"][team.home_temp_data_index]
                else:
                    team.home_temp_data_index += 1


# Main process of the program.
def process(process_list, process_temp, row):
    if not search_list_bool(process_list, process_temp):
        process_list.append(Temperature(process_temp))

    temperature = search_list(process_list, process_temp)
    temperature.add_card("Home", "Yellow", int(row["HY"]))
    temperature.add_card("Away", "Yellow", int(row["AY"]))
    temperature.add_card("Home", "Red", int(row["HR"]))
    temperature.add_card("Away", "Red", int(row["AR"]))
    temperature.add_goal("Home", int(row["FTHG"]))
    temperature.add_goal("Away", int(row["FTAG"]))
    temperature.match_adder()


# CSV to file converter.
def csv_to_file(path, df):
    if not os.path.exists(path):
        # Save the DataFrame to a new CSV file
        df.to_csv(path, index=False)
        print(f"DataFrame saved as {path}")
    else:
        print(f"File {path} already exists. Please choose a different file name.")


# Sets the frame for save.
def show(show_temps):
    total_match = 0

    final_frame = pd.DataFrame(columns=['Temperature',
                                        'Match',
                                        'Total Goal',
                                        'Home Goal',
                                        'Away Goal',
                                        'Total Card',
                                        'Home Yellow Card',
                                        'Home Red Card',
                                        'Away Yellow Card',
                                        'Away Red Card'])

    bubble_sort(show_temps)

    for temp in show_temps:
        match = temp.match_counter
        total_match += temp.match_counter

        new_row = {'Temperature': temp.title,
                   'Match': temp.match_counter,
                   'Total Goal': temp.total_goal / match,
                   'Home Goal': temp.home_goal / match,
                   'Away Goal': temp.away_goal / match,
                   'Total Card': temp.total_card / match,
                   'Total Yellow Card': temp.total_yellow_card / match,
                   'Total Red Card': temp.total_red_card / match,
                   'Home Yellow Card': temp.home_yellow_card / match,
                   'Home Red Card': temp.home_red_card / match,
                   'Away Yellow Card': temp.away_yellow_card / match,
                   'Away Red Card': temp.away_red_card / match
                   }
        new_row = pd.DataFrame(new_row, index=[0])

        final_frame = pd.concat([final_frame, new_row], ignore_index=True)

    print(total_match)

    return final_frame


class Data_Getter:

    def __init__(self, start_season, how_long):
        self.start_season = start_season
        self.how_long = how_long

    def main_function(self):
        home_teams = []
        away_teams = []
        referees = []
        temps = []

        current_season = self.start_season
        next_season = 0

        locations_path = "Data/Locations.csv"
        locations_df = pd.read_csv(locations_path)

        for index, row in locations_df.iterrows():
            home_teams.append(Team(row["Team"]))
            away_teams.append(Team(row["Team"]))

        print("Away teams")
        for team in away_teams:
            team.home_temp_data = dec_team_temp_data(team.title)
            print(team.title + " dict declared")

        print("Home teams")
        for team in home_teams:
            team.home_temp_data = dec_team_temp_data(team.title)
            print(team.title + " dict declared")

        for i in range(0, self.how_long+1):
            if current_season < 9:
                next_season = str(0) + str(current_season + 1)
                current_season = str(0) + str(current_season)
            elif current_season == 9:
                current_season = "09"
                next_season = "10"
            else:
                next_season = current_season + 1

            print("20" + str(current_season) + "-" + str(next_season))

            league_csv_url = r"Data/League/20" + str(current_season) + "-" + str(next_season) + ".csv"
            current_season = int(current_season) + 1

            data_frame = pd.read_csv(league_csv_url)

            countinist = 0
            for index, row in data_frame.iterrows():
                home_team_title = row['HomeTeam']
                away_team_title = row["AwayTeam"]
                referee_title = row["Referee"]
                date = row['Date']
                new_date = convert_date(date)

                countinist += 1

                temp_int = int(get_temp_from_data(new_date, home_team_title, home_teams))

                print(str(countinist) + " " + home_team_title + " vs " + away_team_title + "  temp= " + str(temp_int))

                if not search_list_bool(referees, referee_title):
                    referees.append(Referee(referee_title))

                referee = search_list(referees, referee_title)
                process(referee.temps, temp_int,row)

                home_team = search_list(home_teams, home_team_title)
                process(home_team.temps, temp_int,row)

                away_team = search_list(away_teams, away_team_title)
                process(away_team.temps, temp_int,row)

                if not search_list_bool(temps, temp_int):
                    temps.append(Temperature(temp_int))

                temperature = search_list(temps, temp_int)
                temperature.add_card("Home", "Yellow", int(row["HY"]))
                temperature.add_card("Away", "Yellow", int(row["AY"]))
                temperature.add_card("Home", "Red", int(row["HR"]))
                temperature.add_card("Away", "Red", int(row["AR"]))
                temperature.add_goal("Home", int(row["FTHG"]))
                temperature.add_goal("Away", int(row["FTAG"]))
                temperature.match_adder()

        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)

        temp_csv_path = "Results/Temperatures/Temperatures.csv"

        print("Temps")

        temps_frame = show(temps)
        print(temps_frame)
        csv_to_file(temp_csv_path, temps_frame)

        print("Away")

        for team in away_teams:
            print(team.title)
            team_frame = show(team.temps)
            print(team_frame)

            team_csv_path = "Results/Teams/Away/" + str(team.title) + ".csv"
            csv_to_file(team_csv_path, team_frame)

        print("Home teams")

        for team in home_teams:
            print(team.title)
            team_frame = show(team.temps)
            print(team_frame)

            team_csv_path = "Results/Teams/Home/" + str(team.title) + ".csv"
            csv_to_file(team_csv_path, team_frame)

        print("Referees")

        for referee in referees:
            print(referee.title)
            referee_frame = show(referee.temps)
            print(referee_frame)

            team_csv_path = "Results/Referees/" + str(referee.title) + ".csv"
            csv_to_file(team_csv_path, referee_frame)