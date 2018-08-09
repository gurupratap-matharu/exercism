
def saddle_points(matrix):
    """
    Returns a set of indices of saddle points in a given matrix.
    Saddle points are elements
        a. Highest in the row
        b. Lowest in the corresponding column
    """

    # We check if all rows of the given matrix are of uniform length

    if not all([len(row) == len(matrix[0]) for row in matrix]):
        raise ValueError('Matrix is not uniform in structure.')

    saddle = []  # We'll store the results here and return it.

    transpose = list(zip(*matrix))  # This is a transpose of the original. Rows and columns are basically inverted.

    for row_index, row in enumerate(matrix):

        highest_element = max(row)

        for column_index, element in enumerate(row):  # Iterate through each sub matrix

            if element == highest_element:  # There can be multiple largest elements!

                lowest_element = min(transpose[column_index])

                if highest_element == lowest_element:

                    saddle.append((row_index, column_index))

    return set(saddle)
