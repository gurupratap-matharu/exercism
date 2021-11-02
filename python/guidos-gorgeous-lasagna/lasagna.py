"""Baking script that exposes api methods to cook lasagnas"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return max(EXPECTED_BAKE_TIME - elapsed_bake_time, 0)

def preparation_time_in_minutes(layers=1) -> int:
    """
    Returns the total preparation time to make the lasagna
    which depends on the layers in the lasagna.
    """

    return layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers=1, elapsed_bake_time=1) -> int:
    """
    Tells us the total time in minutes that we have been cooking. Its a sum
    of preparation time and the time the lasagna has been in baking in the oven.
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
