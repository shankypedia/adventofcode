def extract_digits(line):
    part_2_numbers = []
    for i, c in enumerate(line):
        if c.isdigit():
            part_2_numbers.append(c)
        for digit, word in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if line[i:].startswith(word):
                part_2_numbers.append(str(digit + 1))

    return int(part_2_numbers[0] + part_2_numbers[-1])

def main():
    input_file = "input.txt"
    try:
        with open(input_file, "r") as file:
            input_data = file.read().strip()
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
        return

    total_part_2 = 0

    for line in input_data.split('\n'):
        part_2_val = extract_digits(line)
        total_part_2 += part_2_val

    print("Total for Part 2:", total_part_2)

if __name__ == "__main__":
    main()
