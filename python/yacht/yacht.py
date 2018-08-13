# Score categories
# Change the values as you see fit
YACHT = 'Yacht'
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 'FullHouse'
FOUR_OF_A_KIND = 'FourOfAKind'
LITTLE_STRAIGHT = 'LittleStraight'
BIG_STRAIGHT = 'BigStraight'
CHOICE = 'Choice'


def score(dice, category):
    if category == 1:
        return sum([x for x in dice if x == 1])

    elif category == 2:
        return sum([x for x in dice if x == 2])

    elif category == 3:
        return sum([x for x in dice if x == 3])

    elif category == 4:
        return sum([x for x in dice if x == 4])

    elif category == 5:
        return sum([x for x in dice if x == 5])

    elif category == 6:
        return sum([x for x in dice if x == 6])

    elif category == 'FullHouse':
        return sum(dice)

    elif category == 'FourOfAKind':
        for x in dice:
            if dice.count(x) >= 4:
                return 4 ** x
            else:
                return 0


    elif category == 'LittleStraight':
        if sorted(dice) == [1,2,3,4,5]:
            return 30
        else:
            return 0

    elif category == 'BigStraight':
        if sorted(dice) == [2,3,4,5,6]:
            return 30

        else:
            return 0
    elif category == 'Choice':
        return sum(dice)

    elif category == 'Yacht':
        if dice.count(dice[0]) == 5:
            return 50
        else:
            return 0
