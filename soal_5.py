teams = {
    "Indonesia": 0,
    "Malaysia": 0,
    "Jepang": 0,
    "Cina": 0,
}
team1 = [
    "Indonesia",
    "Malaysia",
    "Cina",
    "Cina",
    "Indonesia",
    "Jepang"
]
scoreTeam1 = [5, 1, 3, 0, 0, 1]
team2 = [
    "Malaysia",
    "Jepang",
    "Malaysia",
    "Indonesia",
    "Jepang",
    "Cina"
]
scoreTeam2 = [2, 3, 0, 2, 0, 3]

'''
PROGRAM ASSIGN POINT OF GROUP MATCH
    {
        Calculate the point between two matched 
        if a team won, it gets scored +3
        if tied, it gets scored +1
        if a team lost, it gets scored 0    
    }
DICTIONARY
    teams: dictionary
    team1, team2: string
    scoreTeam1, scoreTeam2: integer
FUNCTION
    assign_point(teams, team1, scoreTeam1, team2, scoreTeam2)
ALGORITHM
    assign_point(teams, team1, scoreTeam1, team2, scoreTeam2) {
        if scoreTeam1 > scoreTeam2:
            teams[team1] <- teams[team1] + 3
            teams[team2] <- teams[team2] + 0
        else if scoreTeam1 = scoreTeam2:
            teams[team1] <- teams[team1] + 1
            teams[team2] <- teams[team2] + 1
        else if scoreTeam1 < scoreTeam2:
            teams[team1] <- teams[team1] + 0
            teams[team2] <- teams[team2] + 3
    }
'''

def assign_point(teams, team1, scoreTeam1, team2, scoreTeam2):
    print("Match Result")
    print(team1, ":", scoreTeam1, team2, ":", scoreTeam2)
    if (scoreTeam1 > scoreTeam2):
        teams[team1] += 3
        teams[team2] += 0
    elif (scoreTeam1 == scoreTeam2):
        teams[team1] += 1
        teams[team2] += 1
    elif (scoreTeam1 < scoreTeam2):
        teams[team1] += 0
        teams[team2] += 3
    print("Point assigned")
    print(team1, ":", teams[team1], team2, ":", teams[team2])
    print()

for i in range (len(team1)):
    assign_point(teams, team1[i], scoreTeam1[i], team2[i], scoreTeam2[i])
print("Final point", teams)