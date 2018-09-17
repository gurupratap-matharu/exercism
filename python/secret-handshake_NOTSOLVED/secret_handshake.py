codes = {
    'wink': 1,
    'double blink': 2,
    'close your eyes': 4,
    'jump': 8,
}


def handshake(code):
    reverse = True
    lst = []
    if code >= 16:
        reverse = False
        code -= 16

    while code:
        if code >= 8:
            lst.append('jump')
            code -= 8
        elif code >= 4:
            lst.append('close your eyes')
            code -= 4
        elif code >= 2:
            lst.append('double blink')
            code -= 2
        elif code == 1:
            lst.append('wink')
            code -= 1

    if reverse:
        lst.reverse()
    return lst


def secret_code(actions):
    total = 0
    for action in actions:
        if action in codes:
            total += codes[action]
    return total


print(secret_code(['double blink', 'jump']))
