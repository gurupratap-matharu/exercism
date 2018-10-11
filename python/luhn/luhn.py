class Luhn(object):
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


