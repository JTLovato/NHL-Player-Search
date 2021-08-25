import requests
from team import team_search


def getNHLTeam():
    team_name = input("""
        Please Enter How You Would Like To Search: 
    
        -'T' to search by Team:
        -'P' to search by Player:
        -'O' to search by Position:
        -'N' to search by Number:
        -'A' to search by Age:
        -'C' to search by Country:
    """).capitalize()

    api = "https://statsapi.web.nhl.com/api/v1/teams/" + team_name
    json_data = requests.get(api).json()

    if team_name == 'T':
        team_search()


print(getNHLTeam())
