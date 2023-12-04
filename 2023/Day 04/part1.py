import sys
from collections import defaultdict

def read_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip().split('\n')

def process_part1(data):
    p1_total_score = 0

    for line in data:
        first, rest = line.split('|')
        card_numbers = {int(x) for x in first.split(':')[1].split()}
        rest_numbers = {int(x) for x in rest.split()}

        common_count = len(card_numbers.intersection(rest_numbers))

        if common_count > 0:
            p1_total_score += 2 ** (common_count - 1)

    print(f"Part 1 Total Score: {p1_total_score}")

if __name__ == "__main__":
    input_file_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    input_data = read_file_content(input_file_path)
    process_part1(input_data)
