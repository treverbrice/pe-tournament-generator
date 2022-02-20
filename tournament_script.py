'''
run this script directly to generate tournament matchups based on season wins
'''

def get_num_teams() -> int:
    pass

def get_team_name(team_num: int) -> str:
    pass

def get_num_games() -> int:
    pass

def get_num_wins(team_name: str) -> int:
    pass

def generate_first_round(teams: dict) -> None:
    pass

# teams = {"name": wins, "name": wins}
if __name__ == "__main__":
    # get number of teams
    num_teams = get_num_teams()

    # loop through and get team names
    team_names = []
    for team in range(num_teams):
        team_names.append(get_team_name(team + 1))

    # get num of games
    num_games = get_num_games

    # loop through and get num of wins
    teams = {}
    for team in range(num_teams):
        teams[team_names[team]] = get_num_wins(team_names[team])

    # get the first round
    generate_first_round(teams)
