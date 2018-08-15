def binary_search(list_of_numbers, number):
    """
    Finds the index of a number in the given list of numbers by using
    a binary search algorithm. This is a divide and conquer technique.

    Time Complexity

    Best Case O(1)
    Average Case O(log n)
    Worst Case O(log n)
    """
    # We find our start, end and a 'found' trigger to do the binary search.

    start = 0
    end = len(list_of_numbers) - 1
    found = False

    # We'll use a while loop and let it run until our start and end variables are
    # one and the same.

    while start <= end and not found:

        midpoint = (start + end) // 2  # This is the centre of our search list.

        if list_of_numbers[midpoint] == number:
            found = True  # We've found our number. Let's return the index.
            return midpoint
        else:
            if number < list_of_numbers[midpoint]:
                end = midpoint - 1  # Number lies on the lower half so we change the
                # end to lower than the midpoint.
            else:
                start = midpoint + 1  # Otherwise the number lies in the upper half and we change the start to ahead of our midpoint.

    # Incase we are unable to find the number our found trigger stays false and we
    # should raise an exception.
    if not found:
        raise ValueError('Number is not present in the list.')
