from copy import deepcopy


def print_grid(grid):
    for row in grid:
        print(''.join(row))


def fork_lift(grid):
    neighbors = [(-1, -1), (-1, 0), (-1, 1),(0, -1),(0, 1), (1, -1), (1, 0), (1, 1)]
    rolls = 0
    new_table = deepcopy(grid)
    lx = len(grid[0])
    ly = len(grid)
    for x in range(lx):
        for y in range(ly):
            roll = grid[y][x]
            if roll != '@':
                continue
            around = 0
            for dx, dy in neighbors:
                nx, ny = x + dx, y + dy
                if 0 <= nx < lx and 0 <= ny < ly:
                    around += 1 if grid[ny][nx] == '@' else 0
            if around < 4:
                rolls += 1
                new_table[y][x] = '.'
    return rolls, new_table


def func1(filename='input.txt'):
    with open(filename) as f:
        input = [list(line.strip()) for line in f]
    rolls, new_table = fork_lift(input)  # warm up
    print(rolls)
    # print_grid(new_table)

def func2(filename='input.txt'):
    with open(filename) as f:
        input = [list(line.strip()) for line in f]
    rolls, new_table = fork_lift(input)
    total = rolls
    while rolls > 0:
        rolls, new_table = fork_lift(new_table)
        total += rolls
    print(total)


func2('test.txt')
func2('input.txt')

