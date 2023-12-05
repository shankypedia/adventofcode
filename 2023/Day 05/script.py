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

    def apply_range(self, ranges: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        result = []
        for dest, src, sz in self.tuples:
            src_end = src + sz
            new_ranges = []
            while ranges:
                st, ed = ranges.pop()
                before = (st, min(ed, src))
                inter = (max(st, src), min(src_end, ed))
                after = (max(src_end, st), ed)
                if before[1] > before[0]:
                    new_ranges.append(before)
                if inter[1] > inter[0]:
                    result.append((inter[0] - src + dest, inter[1] - src + dest))
                if after[1] > after[0]:
                    new_ranges.append(after)
            ranges = new_ranges
        return result + ranges

def apply_functions_to_seed(seed: List[int], functions: List[Function]) -> List[int]:
    result = []
    for x in seed:
        for func in functions:
            x = func.apply_one(x)
        result.append(x)
    return result

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    input_data = read_file_content(input_file_path)
    seed, functions = parse_input_data(input_data)

    processed_seed = apply_functions_to_seed(seed, functions)
    print("Part 1:", min(processed_seed))

    processed_ranges = []
    pairs = list(zip(seed[::2], seed[1::2]))
    for st, sz in pairs:
        ranges = [(st, st + sz)]
        for func in functions:
            ranges = func.apply_range(ranges)
        processed_ranges.append(min(ranges)[0])
    print("Part 2:", min(processed_ranges))

if __name__ == "__main__":
    main()
