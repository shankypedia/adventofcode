import sys
from typing import List, Tuple

def read_file_content(file_path: str) -> str:
    try:
        with open(file_path) as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

def parse_input_data(data: str) -> Tuple[List[int], List['Function']]:
    lines = data.split('\n')
    seed, *others = data.split('\n\n')
    seed = [int(x) for x in seed.split(':')[1].split()]
    functions = [Function(parse_function(s)) for s in others]
    return seed, functions

def parse_function(data: str) -> List[Tuple[int, int, int]]:
    lines = data.split('\n')[1:]
    return [[int(x) for x in line.split()] for line in lines]

class Function:
    def __init__(self, tuples: List[Tuple[int, int, int]]):
        self.tuples = tuples

    def apply_one(self, x: int) -> int:
        for dst, src, sz in self.tuples:
            if src <= x < src + sz:
                return x + dst - src
        return x

def apply_functions_to_seed(seed: List[int], functions: List[Function]) -> List[int]:
    result = []
    for x in seed:
        for func in functions:
            x = func.apply_one(x)
        result.append(x)
    return result

def main():
    if len(sys.argv) != 2:
        print("Usage: python part1.py <input_file>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    input_data = read_file_content(input_file_path)
    seed, functions = parse_input_data(input_data)

    processed_seed = apply_functions_to_seed(seed, functions)
    print("Part 1:", min(processed_seed))

if __name__ == "__main__":
    main()
