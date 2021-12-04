import numpy as np
import copy

with open('day4.txt', 'r+') as f:
    lines = [line.strip() for line in f.readlines()]
dra = [int(ele) for ele in lines[0].split(",")]
newboard = lines[2:]
ord = 0
boards = np.empty((100, 5, 5), int)
for i, line in enumerate(newboard):
    k = i % 6
    if k < 5:
        boards[ord][k:] = [int(ele) for ele in line.split()]
    if k == 5:
        ord += 1


def unmarked(board):
    tot = 0
    for row in board:
        if np.count_nonzero(row == -1) == 5:
            for x in board:
                for y in x:
                    if y > -1:
                        tot += y
            return tot
    for col in board.T:
        if np.count_nonzero(col == -1) == 5:
            for x in board:
                for y in x:
                    if y > -1:
                        tot += y
            return tot


def check(boards):
    list99 = set([i for i in range(0, 100)])

    for num in dra:
        newboard = []
        for board in boards:
            board = np.where(board == num, -1, board)
            newboard.append(board)
        boards = copy.deepcopy(newboard)
        for i, board in enumerate(boards):
            if len(list99) == 1:
                aim = list(list99)[0]
                um = unmarked(boards[aim])
                if um:
                    return boards[aim], um*num
            else:
                for row in board:
                    if np.count_nonzero(row == -1) == 5:
                        list99.discard(i)
                        break
                for col in board.T:
                    if np.count_nonzero(col == -1) == 5:
                        list99.discard(i)
                        break


finalboard, tot = check(boards)
print(finalboard)
print(tot)
