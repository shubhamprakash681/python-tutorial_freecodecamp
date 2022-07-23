number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 0]
]
for ls in number_grid:
    print(ls)

for row in number_grid:
    for col in row:
        print(col)

print()

for row_number in range(len(number_grid)):
    for col_number in range(len(number_grid[row_number])):
        print(number_grid[row_number][col_number])
