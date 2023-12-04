import sys
from collections import defaultdict

def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip().split('\n')

def process_gear_data_part2(gear_combinations):
    product_of_combinations = sum(v[0] * v[1] for v in gear_combinations.values() if len(v) == 2)
    print(f"Product of Gear Combinations (p2): {product_of_combinations}")

if __name__ == "__main__":
    input_file_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    input_data = read_input(input_file_path)
    gear_matrix = [[char for char in line] for line in input_data]

    gear_combinations = defaultdict(list)
    rows, cols = len(gear_matrix), len(gear_matrix[0])

    for r in range(rows):
        adjacent_gears, current_number = set(), 0

        for c in range(cols + 1):
            if c < cols and gear_matrix[r][c].isdigit():
                current_number = current_number * 10 + int(gear_matrix[r][c])
                for rr in [-1, 0, 1]:
                    for cc in [-1, 0, 1]:
                        if 0 <= r + rr < rows and 0 <= c + cc < cols:
                            if gear_matrix[r + rr][c + cc] == '*':
                                adjacent_gears.add((r + rr, c + cc))
            elif current_number > 0:
                for gear_position in adjacent_gears:
                    gear_combinations[gear_position].append(current_number)
                current_number, adjacent_gears = 0, set()

    process_gear_data_part2(gear_combinations)
