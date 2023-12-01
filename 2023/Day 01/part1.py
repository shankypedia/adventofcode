def extract_digits(line):
    part_1_numbers = [c for c in line if c.isdigit()]
    return int(part_1_numbers[0] + part_1_numbers[-1])

def main():
    input_file = "input.txt"
    try:
        with open(input_file, "r") as file:
            input_data = file.read().strip()
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
        return

    total_part_1 = 0

    for line in input_data.split('\n'):
        part_1_val = extract_digits(line)
        total_part_1 += part_1_val

    print("Total for Part 1:", total_part_1)

if __name__ == "__main__":
    main()
