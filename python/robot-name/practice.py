import random

import datetime

seed = datetime.datetime.now().microsecond
random.seed(seed)
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters = [x for x in letters]
for i in range(10):
    alphabet1 = random.choice(letters)
    alphabet2 = random.choice(letters)
    number1 = random.randint(0, 9)
    number2 = random.randint(0, 9)
    number3 = random.randint(0, 9)

    name = alphabet1 + alphabet2 + str(number1) + str(number2) + str(number3)
    print(name, end=' ')
