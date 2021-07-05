# Algorithm & Data Structure
## Programming Language
Program language: Python

## How to run the program?
Run the program: `python soal_<number>.py`

### Problem 3 Solution
```
AREA OF TRIANGLE
    { Calculate the area of triangle}
DICTIONARY
    base, height: integer/float
FUNCTION
    triangle_area(base, height)
DESCRIPTION
    triangle_area(base, height) {
        return 1/2 * Base * Height
    }
```

### Problem 5 Solution
```
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
```

`Final point {'Indonesia': 7, 'Malaysia': 0, 'Jepang': 4, 'Cina': 6}`