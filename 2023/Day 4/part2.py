import sys
from collections import defaultdict

def read_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip().split('\n')

def process_part2(data):
    line_counts = defaultdict(int)

    for i, line in enumerate(data):
        line_counts[i] += 1

        first, rest = line.split('|')
        entry_id, card = first.split(':')
        card_numbers = {int(x) for x in card.split()}
        rest_numbers = {int(x) for x in rest.split()}

        common_numbers = card_numbers & rest_numbers
        common_count = len(common_numbers)

        for j in range(common_count):
            line_counts[i + 1 + j] += line_counts[i]

    print(f"Sum of Line Counts (Part 2): {sum(line_counts.values())}")

if __name__ == "__main__":
    input_file_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    input_data = read_file_content(input_file_path)
    process_part2(input_data)
