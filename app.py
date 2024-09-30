from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

import itertools
import math
import random

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_schedule', methods=['POST'])
def generate_schedule():
    data = request.get_json()
    num_teams = int(data.get('numTeams'))
    games_per_team = int(data.get('gamesPerTeam'))
    
    if not num_teams or not games_per_team:
        return jsonify({'error': 'Missing required parameters'}), 400
    
    schedule = generate_round_robin_schedule2(num_teams, games_per_team)
    return jsonify({'schedule': schedule})

def generate_round_robin_schedule1(num_teams, games_per_team):
    schedule = []
    formatted_schedule = [[] for _ in range(num_teams + 1)]

    # Max number of times a team might play another team
    # For example if there are 8 teams and each team plays 14 games than this means
    # Every team plays every other team 2 times. 2 is what we are calculating here for this example
    team_multiplier = (math.ceil(games_per_team/(num_teams-1)))
    print(f"Team Multiplier: {team_multiplier}")

    # List of teams
    teams = list(range(1, num_teams+1))

    # Create all combinations of of unique pairings of games
    all_matchups = list(itertools.combinations(teams, 2))
    # randomize it
    # random.shuffle(all_matchups)

    # Duplicate all the match ups based on how many games are getting played
    all_matchups = all_matchups * team_multiplier

    # Loop through rounds and allocate games to the schedule
    game_number = 0

    # Create rounds until each team has played the required number of match ups
    while all_matchups:
        print(f"All Matchups: {all_matchups}")
        # Track of all the games for this round
        round_games = []

        # Track all the teams that are already playing this round
        teams_in_this_round = set()

        for match in all_matchups:
            team1, team2 = match

            # Make sure that neither team has already been scheduled to play this round
            if team1 not in teams_in_this_round and team2 not in teams_in_this_round:
                round_games.append((team1, team2))
                teams_in_this_round.add(team1)
                teams_in_this_round.add(team2)
                print(f"Added Match: ({team1}, {team2})")
                formatted_schedule[team1].append(team2)
                formatted_schedule[team2].append(team1)

        # Round match ups are now done add them to the schedule
        schedule.append(round_games)

        # remove all the matches that were just added from all_matchups
        for match in round_games:
            all_matchups.remove(match)
        
        print(f"Added Round: {round_games}")

        game_number += 1

        # Break if all teams have played the required number of games
        if game_number >= games_per_team:
            break

    print(f"Game Number: {game_number}")
    print(f"Games Per Team: {games_per_team}")
    return schedule

def generate_round_robin_schedule2(num_teams, games_per_team):
    schedule = []
    formatted_schedule = [[] for _ in range(num_teams + 1)]

    # Max number of times a team might play another team
    # For example if there are 8 teams and each team plays 14 games than this means
    # Every team plays every other team 2 times. 2 is what we are calculating here for this example
    team_multiplier = (math.ceil(games_per_team/(num_teams-1)))
    print(f"Team Multiplier: {team_multiplier}")

    # List of teams
    teams = list(range(1, num_teams+1))

    # Create all combinations of of unique pairings of games
    all_matchups = list(itertools.combinations(teams, 2))
    # randomize it
    # random.shuffle(all_matchups)

    # Duplicate all the match ups based on how many games are getting played
    all_matchups = all_matchups * team_multiplier

    # Loop through rounds and allocate games to the schedule
    game_number = 0

    # Create rounds until each team has played the required number of match ups
    while all_matchups:
        print(f"All Matchups: {all_matchups}")
        # Track of all the games for this round
        round_games = []

        # Track all the teams that are already playing this round
        teams_in_this_round = set()

        for match in all_matchups:
            team1, team2 = match

            # Make sure that neither team has already been scheduled to play this round
            if team1 not in teams_in_this_round and team2 not in teams_in_this_round:
                round_games.append((team1, team2))
                teams_in_this_round.add(team1)
                teams_in_this_round.add(team2)
                print(f"Added Match: ({team1}, {team2})")
                formatted_schedule[team1].append(team2)
                formatted_schedule[team2].append(team1)

        # Round match ups are now done add them to the schedule
        schedule.append(round_games)

        # remove all the matches that were just added from all_matchups
        for match in round_games:
            all_matchups.remove(match)
        
        print(f"Added Round: {round_games}")

        game_number += 1

        # Break if all teams have played the required number of games
        if game_number >= games_per_team:
            break

    print(f"Game Number: {game_number}")
    print(f"Games Per Team: {games_per_team}")

    for team in range(1, num_teams + 1):  # Start from 1 to num_teams
        opponents = formatted_schedule[team]
        print(f"Team {team} has matches with: {opponents}")
    
    return formatted_schedule

if __name__ == '__main__':

    # Example usage
    # num_teams = 8
    # games_per_team = 14
    # schedule = generate_round_robin_schedule1(num_teams, games_per_team)
    # formatted_schedule = generate_round_robin_schedule2(num_teams, games_per_team)

    formatted = True
    # Display the schedule
    if not True:
        for round_num, round_games in enumerate(schedule):
            print(f"Round {round_num + 1}: \t {round_games}")
    elif False:
        for team in range(1, num_teams + 1):  # Start from 1 to num_teams
            opponents = formatted_schedule[team]
            print(f"Team {team} has matches with: {opponents}")


    app.run(port=5000, debug=True)