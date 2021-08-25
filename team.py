import requests


def team_search():

    division_query = input("""
    What Division Would You Like To Look At?
    -Type 1 for Atlantic 
    -Type 2 for Metropolitan
    -Type 3 for Central 
    -Type 4 for Pacific 
    """)

    if division_query == '1':
        team_number = input("""
            What Team Would You Like To Know More About?
        
            -Type 6 for Boston Bruins
            -Type 7 for Buffalo Sabres
            -Type 8 for Montreal Canadians
            -Type 9 for Ottawa Senators
            -Type 10 for Toronto Maple Leafs
            -Type 13 for Florida Panthers
            -Type 14 for Tampa Bay Lightning
            -Type 17 for Detroit Red Wings
        """)

    if division_query == '2':
        team_number = input("""
            What Team Would You Like To Know More About?
            
            -Type 1 for New Jersey Devils
            -Type 2 for New York Islanders
            -Type 3 for New York Rangers
            -Type 4 for Philadelphia Flyers
            -Type 5 for Pittsburgh Penguins
            -Type 12 for Carolina Hurricanes
            -Type 15 for Washington Capitals
            -Type 29 for Columbus Blue Jackets
        """)

    if division_query == '3':
        team_number = input("""
            What Team Would You Like To Know More About?
                
            -Type 16 for Chicago Blackhawks
            -Type 18 for Nashville Predators
            -Type 19 for St. Louis Blues
            -Type 21 for Colorado Avalanche
            -Type 25 for Dallas Stars
            -Type 30 for Minnesota Wild
            -Type 52 for Winnipeg Jets
            -Type 53 for Arizona Coyotes
        """)

    if division_query == '4':
        team_number = input("""
        What Team Would You Like To Know More About?
                
        -Type 20 for Calgary Flames
        -Type 22 for Edmonton Oilers
        -Type 23 for Vancouver Canucks
        -Type 24 for Anaheim Ducks
        -Type 26 for Los Angeles Kings
        -Type 28 for San Jose Sharks
        -Type 54 for Vegas Golden Knights
        -Type 55 for Seattle Kraken
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
        players = (x['person']['fullName'])
        print(players)

    player_query = input("\n What player Would You Like To Know More About? ")

    for x in roster_list:
        full_name = (x['person']['fullName'])
        player_id = str(x['person']['id'])
        if player_query != full_name:
            pass
        else:
            roster_api_player = "https://statsapi.web.nhl.com/api/v1/people/" + player_id
            player_json_data = requests.get(roster_api_player).json()
            individual_player = player_json_data['people']

            season = input(f"""
            You chose {player_query}
            
            What Season would you Like to Specify?
            -20202021
            -20192020
            -20182019
            -20172018
            -20162017
            -20152016
            -20142015
            -20132014
            -20122013
            -20112012
            -20102011
            """)

            roster_api_stats = "https://statsapi.web.nhl.com/api/v1/people/" + player_id + "/stats?stats=statsSingleSeason&season=" + season
            player_stats_json_data = requests.get(roster_api_stats).json()
            individual_stats = player_stats_json_data['stats']
            for stat in individual_stats:
                all_stats = stat['splits']

            stat_list = str(all_stats)

            for a in individual_player:
                height = (a['height'])
            if stat_list == '[]':
                print("Sorry, There's no info on that year for that player.")
            else:
                print(full_name + ": " + "\n" + "ID: " + player_id + "\n" + "Height: " + height + "\n" + "Stats: " + stat_list)














