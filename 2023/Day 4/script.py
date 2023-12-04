import sys
from collections import defaultdict

def read_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip().split('\n')

def process_data(data):
    p1_total_score = 0
    line_counts = defaultdict(int)

    for i, line in enumerate(data):
        line_counts[i] += 1

        first, rest = line.split('|')
        entry_id, card = first.split(':')
        card_numbers = [int(x) for x in card.split()]
        rest_numbers = [int(x) for x in rest.split()]
        
        common_numbers = set(card_numbers) & set(rest_numbers)
        common_count = len(common_numbers)

        if common_count > 0:
            p1_total_score += 2 ** (common_count - 1)

        for j in range(common_count):
            line_counts[i + 1 + j] += line_counts[i]

    print(f"Part 1 Total Score: {p1_total_score}")
    print(f"Sum of Line Counts (Part 2): {sum(line_counts.values())}")

if __name__ == "__main__":
    input_file_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    input_data = read_file_content(input_file_path)
    process_data(input_data)
