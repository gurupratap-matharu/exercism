import time


def binary_search_recursive(list_of_numbers, number, start=0, end=None):

    # The end of our search is initialized to None. First we set the end to the length of the sequence.
    if end is None:
        end = len(list_of_numbers) - 1

    if start > end:
        raise ValueError('Number not in list')

    mid = (start + end) // 2  # This is the mid value of our binary search.

    if number == list_of_numbers[mid]:
        # We have found the number in our list. Let's return the index.
        return mid

    if number < list_of_numbers[mid]:
        # Number lies in the lower half. So we call the function again changing the end value to 'mid - 1' Here we are entering the recursive mode.

        return binary_search_recursive(list_of_numbers, number, start, mid - 1)
    # number > list_of_numbers[mid]
    # Number lies in the upper half. So we call the function again changing the start value to 'mid + 1' Here we are entering the recursive mode.

    return binary_search_recursive(list_of_numbers, number, mid + 1, end)


if __name__ == "__main__":
    start_time = time.time()
    lst = [1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 634]
    number = 144
    print(binary_search_recursive(lst, number))
    print("--- {:.5f} seconds ---".format(time.time() - start_time))
