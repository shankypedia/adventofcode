import sys

def extract_digits(line):
    part_1_numbers = [c for c in line if c.isdigit()]
    
    part_2_numbers = []
    for i, c in enumerate(line):
        if c.isdigit():
            part_2_numbers.append(c)
        for digit, word in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if line[i:].startswith(word):
                part_2_numbers.append(str(digit + 1))

    return int(part_1_numbers[0] + part_1_numbers[-1]), int(part_2_numbers[0] + part_2_numbers[-1])

def main():
    input_file = "input.txt"
    try:
        with open(input_file, "r") as file:
            input_data = file.read().strip()
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
        sys.exit(1)

    total_part_1 = 0
    total_part_2 = 0

    for line in input_data.split('\n'):
        part_1_val, part_2_val = extract_digits(line)
        total_part_1 += part_1_val
        total_part_2 += part_2_val

    print("Total for Part 1:", total_part_1)
    print("Total for Part 2:", total_part_2)

if __name__ == "__main__":
    main()
