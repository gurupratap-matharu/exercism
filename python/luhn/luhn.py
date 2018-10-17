class Luhn(object):
    """Luhn class to create objects which pertain to the Luhn algorithm"""

    def __init__(self, card_num):
        """Our constructor class which creates objects for the Luhn class"""
        self.card_num = card_num.replace(" ", "")
        print(self.card_num)

    def is_valid(self):
        """Method to check if the number is valid as per Luhn's algorithms. Returns a boolean value."""

        if len(self.card_num) <= 1:
            return False

        else:
            card_number = list(self.card_num)

            return [x * 2 if int((x * 2)) < 0 else 0 for x in card_number[-2::-2]]
            # for digit in card_number[-2::-2]:
            #     digit = int(digit)
            #     digit *= 2

            #     if digit > 9:
            #         digit -= 9
            # print(card_number)


card1 = Luhn('4539 1488 0343 6467')
print(card1.is_valid())
