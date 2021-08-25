import requests


def team_search():
    team_number = input("""
    What Team Would You Like To Know More About?

    -Type 1 for New Jersey Devils
    -Type 2 for New York Islanders
    -Type 3 for New York Rangers
    -Type 4 for Philadelphia Flyers
    -Type 5 for Pittsburgh Penguins
    -Type 6 for Boston Bruins
    -Type 7 for Buffalo Sabres
    -Type 8 for Montreal Canadians
    :
    """)

    api = "https://statsapi.web.nhl.com/api/v1/teams/" + team_number
    json_data = requests.get(api).json()
    roster_api = "https://statsapi.web.nhl.com/api/v1/teams/" + team_number + "/roster"
    roster_json_data = requests.get(roster_api).json()

    team_list = json_data['teams']
    roster_list = roster_json_data['roster']


    for i in team_list:
        print(
            i['name'] + "\n",
            i['firstYearOfPlay'] + "\n",
            i['venue']['name'] + "\n"
        )

    for x in roster_list:
        y = (x['person']['fullName'])
        print(y)

    player_query = input("What player Would You Like To Know More About? ")

    for x in roster_list:
        full_name = (x['person']['fullName'])
        player_id = str(x['person']['id'])
        if player_query != full_name:
            pass
        else:
            roster_api_player = "https://statsapi.web.nhl.com/api/v1/people/" + player_id
            player_json_data = requests.get(roster_api_player).json()
            individual_player = player_json_data['people']

            season = input("""
            What Season would you Like to Specify?
            -20202021
            -20192020
            -20182019
            -20172018
            """)

            roster_api_stats = "https://statsapi.web.nhl.com/api/v1/people/" + player_id + "/stats?stats=statsSingleSeason&season=" + season
            player_stats_json_data = requests.get(roster_api_stats).json()
            individual_stats = player_stats_json_data['stats']
            for stat in individual_stats:
                all_stats = stat['splits']

            x = str(all_stats)


            for a in individual_player:
                 height = (a['height'])

            print(full_name + ": " + "\n" + "ID: " + player_id + "\n" + "Height: " + height + "\n" + "Goals: " + x)









    #print(roster_list[0]['person']['fullName'])
    #print(roster_list[1]['person']['fullName'])




