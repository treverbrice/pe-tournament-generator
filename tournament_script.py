'''
run this script directly to generate tournament matchups based on season wins
'''

def get_num_teams() -> int:
    user_num_teams = int(input("Enter the number of teams in the tournament: "))
    if user_num_teams < 2:
        print("The minimum number of teams is 2, try again.")
        user_num_teams = get_num_teams()
    return user_num_teams

def get_team_name(team_num: int) -> str:
    user_team_name = input(f"Enter the name for team #{team_num}: ")
    if len(user_team_name) < 2:
        print("Team names must have at least 2 characters, try again")
        user_team_name = get_team_name(team_num)
    if len(user_team_name.split(" ")) > 2:
        print("Team names may have at most 2 words, try again.")
        user_team_name = get_team_name(team_num)
    return user_team_name

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
