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

def get_num_games(num_teams: int) -> int:
    user_num_games = int(input("Enter the number of games played by each team: "))
    if user_num_games < num_teams - 1:
        print("Invalid number of games. Each team plays each other at least once in the regular season, try again")
        user_num_games = get_num_games(num_teams)
    return user_num_games

def get_num_wins(team_name: str) -> int:
    user_num_wins = int(input(f"Enter the number of wins Team {team_name} had: "))
    if user_num_wins < 0:
        print("The minimum number of wins is 0, try again.")
        user_num_wins = get_num_wins(team_name)
    return user_num_wins

def generate_first_round(teams: dict) -> None:
    local_teams = teams.copy()
    local_teams = dict(sorted(local_teams.items(), key=lambda item: item[1]))
    num_games = len(local_teams) // 2

    print("Generating the games to be played in the first round of the tournament...")
    for game in range(num_games):
        team1 = local_teams.popitem()
        local_teams = dict(sorted(local_teams.items(), key=lambda item: item[1], reverse = True))
        team2 = local_teams.popitem()
        local_teams = dict(sorted(local_teams.items(), key=lambda item: item[1]))
        print(f"Home: {team1[0]} VS Away: {team2[0]}")


# teams = {"name": wins, "name": wins}
if __name__ == "__main__":
    # get number of teams
    num_teams = get_num_teams()

    # loop through and get team names
    team_names = []
    for team in range(num_teams):
        team_names.append(get_team_name(team + 1))

    # get num of games
    num_games = get_num_games(num_teams)

    # loop through and get num of wins
    teams = {}
    for team in range(num_teams):
        teams[team_names[team]] = get_num_wins(team_names[team])

    # get the first round
    generate_first_round(teams)
