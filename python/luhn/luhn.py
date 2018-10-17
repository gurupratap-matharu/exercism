class Luhn(object):
<<<<<<< HEAD
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
=======
    """Our main Luhn class to create card objects."""

    def __init__(self, card_num):
        """The constructor method of the class."""
        
        # to remove all white spaces in the string
        card_num = card_num.replace(' ','')
        self.card_num = card_num


    def is_valid(self):
        """Method to check whether the passed number clears the Luhn's test. Returns a boolean."""
        
        # we check for min. length and non-decimal characters

        if len(self.card_num) < 2 or self.card_num.isdecimal() == False:
            return False
        
        else:
            card = list(self.card_num)
            n = len(card) - 2
            for digit in range(n,-1,-2):
                
                    i = int(card[digit])
                    i *= 2
                    if i > 9:
                        i -= 9
                    card[digit] = str(i)                   
           
           
            total = sum([int(x) for x in card]) 
            
            if total % 10 == 0:
                return True
            else:
                return False


>>>>>>> 36057ab7a6def22cbdb13ef737101f2ed768bca6
