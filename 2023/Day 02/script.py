import sys
from collections import defaultdict

def read_input(file_path):
    with open(file_path) as file:
        return file.read().strip()

def calculate_game_scores(data):
    player1_total_score = 0
    player2_total_score = 0

    for game_line in data.split('\n'):
        is_game_valid = True
        game_id, game_events = game_line.split(':')
        ball_counts = defaultdict(int)

        for event in game_events.split(';'):
            for ball in event.split(','):
                count, color = ball.split()
                count = int(count)
                ball_counts[color] = max(ball_counts[color], count)

                if count > {'red': 12, 'green': 13, 'blue': 14}.get(color, 0):
                    is_game_valid = False

        game_score = 1
        for count in ball_counts.values():
            game_score *= count

        player2_total_score += game_score
        if is_game_valid:
            player1_total_score += int(game_id.split()[-1])

    return player1_total_score, player2_total_score

if __name__ == "__main__":
    input_file_path = "input.txt"
    input_data = read_input(input_file_path)
    result_player1, result_player2 = calculate_game_scores(input_data)

    print(f"Player 1 Total Score: {result_player1}")
    print(f"Player 2 Total Score: {result_player2}")
