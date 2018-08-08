
def saddle_points(matrix):

    transpose = list(zip(*matrix))
    for row, column in zip(matrix, transpose):
        i = row.index(max(row))
        column = transpose[i]
        j = column.index(min(column))
        if max(row) == min(column):
            print(j, i)


# matrix = [[9, 8, 7], [5, 3, 2], [6, 6, 7]]
matrix = [[4, 5, 4], [3, 5, 5], [1, 5, 4]]
# matrix = [[6, 7, 8], [5, 5, 5], [7, 5, 6]]
saddle_points(matrix)
