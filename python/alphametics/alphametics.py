def solve(puzzle):
    """
    Returns the integer value of each character of the alphametics
    puzzle
    """
    puzzle = puzzle.split(' == ')
    return puzzle


if __name__ == '__main__':
    PUZZLE = "AND + A + STRONG + OFFENSE + AS + A + GOOD == DEFENSE"
    RESULT = solve(puzzle=PUZZLE)
    print(RESULT)
