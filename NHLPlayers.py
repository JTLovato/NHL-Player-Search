 
from team import team_search

#First thing user sees.
#Asks user how they'd like to search
#Currently only option avaliable is: Team Search

def getNHLTeam():
    first_query = input("""
        Please Enter How You Would Like To Search: 
    
        -'T' to search by Team:
        -'P' to search by Player: COMING SOON 
        -'O' to search by Position:COMING SOON 
        -'N' to search by Number:COMING SOON 
        -'A' to search by Age:COMING SOON 
        -'C' to search by Country:COMING SOON 
        
        -'Q' to quit at anytime
        
    """).capitalize()

    #User can type 'q' at anty time to quit the program
    #User selects how to search for a player
    #Currently only option is to search by team

    while first_query != 'q':
        if first_query == 'T':
            team_search()
        elif first_query == 'P':
            pass
        elif first_query == 'O':
            pass
        elif first_query == 'N':
            pass
        elif first_query == 'A':
            pass
        elif first_query == 'C':
            pass
        else:
            print("Sorry, Try again using one of the above.")


print(getNHLTeam())

