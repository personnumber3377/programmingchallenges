import pathlib
import sys
 
 
def parse(puzzle_input: str) -> list[str]:
    """Parse input"""
    return puzzle_input.splitlines()
 
 
def part1(data: list[str]) -> int:
    """Solve part 1"""
    samples: tuple[int, ...] = tuple(n for n in range(20, 221, 40))
    signal_strengths: dict[int, int] = {sample: 0 for sample in samples}
    num_cycles: int = 0
    x: int = 1
    for instr in data:
        num_cycles += 1
        if num_cycles in samples:
            signal_strengths[num_cycles] = x * num_cycles
        if instr.startswith("addx "):
            num_cycles += 1
            if num_cycles in samples:
                signal_strengths[num_cycles] = x * num_cycles
            x += int(instr[5:])
    return sum(v for v in signal_strengths.values())
 
 
def part2(data: list[str]) -> str:
    """Solve part 2"""
    sprite_pos: int = 1
    drawn_pixel: int = 0
    lit_pixels: list[list[int]] = []
    line_pixels: list[int] = [drawn_pixel]
    for instr in data:
        if drawn_pixel in range(sprite_pos - 1, sprite_pos + 2):
            line_pixels.append(drawn_pixel)
        drawn_pixel += 1
        if drawn_pixel == 40:
            lit_pixels.append(line_pixels)
            line_pixels = []
            drawn_pixel = 0
        if instr.startswith("addx "):
            if drawn_pixel in range(sprite_pos - 1, sprite_pos + 2):
                line_pixels.append(drawn_pixel)
            drawn_pixel += 1
            if drawn_pixel == 40:
                lit_pixels.append(line_pixels)
                line_pixels = []
                drawn_pixel = 0
            sprite_pos += int(instr[5:])
 
    screen: list[list[str]] = [
        ["#" if pixel in line else "." for pixel in range(40)] for line in lit_pixels
    ]
 
    readout: str = ""
    for screen_line in screen:
        readout += "".join(screen_line) + "\n"
    return readout.rstrip("\n")

RUN_COUNT = 10000


def solve(puzzle_input: str) -> tuple[int, str]:
    """Solve the puzzle for the given input"""
    data: list[str] = parse(puzzle_input)
    #solution1: int = part1(data)  # Correct answer was 12980 (with my data)
    for _ in range(RUN_COUNT):

        solution2: str = part2(data)  # Correct answer was "BRJLFULP" (with my data)
 
    return solution2
 
 
if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))

