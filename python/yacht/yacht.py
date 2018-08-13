# Score categories
# Change the values as you see fit
YACHT = 'YACHT'
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 'FULL_HOUSE'
FOUR_OF_A_KIND = 'FOUR_OF_A_KIND'
LITTLE_STRAIGHT = 'LITTLE_STRAIGHT'
BIG_STRAIGHT = 'BIG_STRAIGHT'
CHOICE = 'CHOICE'


def score(dice, category):

    """
    The dice game [Yacht](https://en.wikipedia.org/wiki/Yacht_(dice_game)) is from
    the same family as Poker Dice, Generala and particularly Yahtzee, of which it
    is a precursor. In the game, five dice are rolled and the result can be entered
    in any of twelve categories. The score of a throw of the dice depends on
    category chosen.
    """

    # First we check if the category asked is within the 'ONES - SIXES' range and
    # return the corresponding sum of the digits present.

    if category in [1, 2, 3, 4, 5, 6]:
        return sum([x for x in dice if x == category])

    # Full House is the most tricky. We sort the dices and check of occurences of the
    # first and the last term. If they are 2,3 or 3,2 then just return the sum, else 0
    elif category == 'FULL_HOUSE':

        lst = sorted(dice)
        i = lst.count(dice[0])
        j = lst.count(dice[-1])

        if (i == 2 and j == 3) or (i == 3 and j == 2):
            return sum(dice)

        else:
            return 0


    elif category == 'FOUR_OF_A_KIND':
        return [x*4 if dice.count(x) >= 4 else 0 for x in dice][0]

    elif category == 'LITTLE_STRAIGHT':

        if sorted(dice) == [1, 2, 3, 4, 5]:
            return 30
        else:
            return 0

    elif category == 'BIG_STRAIGHT':

        if sorted(dice) == [2, 3, 4, 5, 6]:
            return 30

        else:
            return 0

    elif category == 'CHOICE':
        return sum(dice)

    elif category == 'YACHT':
        return [50 if dice.count(x) == 5 else 0 for x in dice][0]



