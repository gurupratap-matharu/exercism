import random

import datetime


class Robot(object):
    def __init__(self):
        seed = datetime.datetime.now().microsecond
        random.seed(seed)
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        letters = [x for x in letters]

        alphabet1 = random.choice(letters)
        alphabet2 = random.choice(letters)
        number1 = random.randint(0, 9)
        number2 = random.randint(0, 9)
        number3 = random.randint(0, 9)

        name = alphabet1 + alphabet2 + str(number1) + str(number2) + str(number3)
        self.name = name

    def reset(self):
        self.name = Robot().name


random.seed('Hola')
for i in range(5):
    robot1 = Robot()
    print(robot1.name)
    robot1.reset()
