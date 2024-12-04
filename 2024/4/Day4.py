
with open("2024/prompts/4p.txt") as f:
    board = []
    for line in f:
        board.append(list(line.rstrip()))

total = 0
for y, row in enumerate(board):
    for x, item in enumerate(row):
        # check right
        if not (x > len(row) - 4):
            if ((row[x] + row[x+1] + row[x+2] + row[x+3]) == "XMAS"):
                total += 1
        # check left
        if (x > 2):
            if ((row[x] + row[x-1] + row[x-2] + row[x-3]) == "XMAS"):
                total += 1
        # check down
        if not (y > len(board) - 4):
            if ((board[y][x] + board[y+1][x] + board[y+2][x] + board[y+3][x]) == "XMAS"):
                total += 1
        # check up
        if y > 2:
            if ((board[y][x] + board[y-1][x] + board[y-2][x] + board[y-3][x]) == "XMAS"):
                total += 1
        # check up left
        if y > 2 and x > 2:
            if ((board[y][x] + board[y-1][x-1] + board[y-2][x-2] + board[y-3][x-3]) == "XMAS"):
                total += 1
        # check down left
        if not (y > len(board) - 4) and x > 2:
            if ((board[y][x] + board[y+1][x-1] + board[y+2][x-2] + board[y+3][x-3]) == "XMAS"):
                total += 1
        # check down right
        if not (y > len(board) - 4) and not (x > len(row) - 4):
            if ((board[y][x] + board[y+1][x+1] + board[y+2][x+2] + board[y+3][x+3]) == "XMAS"):
                total += 1
        # check up right
        if y > 2 and not (x > len(row) - 4):
            if ((board[y][x] + board[y-1][x+1] + board[y-2][x+2] + board[y-3][x+3]) == "XMAS"):
                total += 1

print("part1:", total)

total = 0
for y, row in enumerate(board):
    for x, item in enumerate(row):
        if x < 1 or x > len(row) - 2 or y < 1 or y > len(board) - 2:
            continue
        matches = 0
        if ((board[x-1][y-1] + board[x][y] + board[x+1][y+1]) == "MAS"):
            matches += 1
        if ((board[x-1][y-1] + board[x][y] + board[x+1][y+1]) == "SAM"):
            matches += 1
        if ((board[x-1][y+1] + board[x][y] + board[x+1][y-1]) == "SAM"):
            matches += 1
        if ((board[x-1][y+1] + board[x][y] + board[x+1][y-1]) == "MAS"):
            matches += 1
        if matches > 1:
            total += 1

print("part2:", total)
