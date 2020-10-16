UNARY = ('n')
BINARY = ('+', '-', '*', '//', 'e')


def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def evaluate_rpn(data=None):
    """Evaluates the expression using Reverse Polish Notation"""
    stack = []

    for char in data.split():

        if represents_int(char):
            stack.append(int(char))

        elif char in UNARY:
            num = -1 * stack.pop()
            stack.append(num)

        elif char in BINARY:
            num_2, num_1 = stack.pop(), stack.pop()

            if char == '+':
                stack.append(num_1 + num_2)

            elif char == '-':
                stack.append(num_1 - num_2)

            elif char == '*':
                stack.append(num_1 * num_2)

            elif char == '//':
                stack.append(num_1 // num_2)

            elif char == 'e':
                stack.append(num_1 ** num_2)

        else:
            print(char)
            continue
    print(stack)
    return stack[0]


if __name__ == '__main__':
    evaluate_rpn('7 4 +')
