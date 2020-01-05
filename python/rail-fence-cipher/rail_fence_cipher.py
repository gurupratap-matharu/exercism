def encode(message, rails):
    """
    Encodes a message as per the rails fence algorithm.
    Params:
    rails: int: defines the layers we use to encode the message.
    """
    encoded_message = []
    lane = 1
    for i in range(len(message)):
        if lane == 1:
            count = 1
        if lane == rails:
            count = -1
        encoded_message.append(lane)
        lane += count
    return encoded_message


def decode(encoded_message, rails):
    """
    Decodes a message as per the rails fence algorithm.
    Params:
    rails: int: defines the layers we used to encode the message.
    """
    return


if __name__ == '__main__':
    RESULT = encode(message="EXERCISESFORTHEBRAINTOBESHARP", rails=9)
    print(RESULT)
