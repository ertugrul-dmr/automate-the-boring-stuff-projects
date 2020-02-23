grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for i in range(0, len(grid[0])):
    for r in range(0, len(grid)):
        print(grid[r][i], end='')
    print('\t')
for i in range(len(grid[0]) - 1, 0, -1):
    for r in range(0, len(grid)):
        print(grid[r][i], end='')
    print('\t')
