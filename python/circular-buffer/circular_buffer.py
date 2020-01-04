class BufferFullException(Exception):
    def __init__(self, message):
        self.message = message
        raise Exception(self.message)


class BufferEmptyException(Exception):
    def __init__(self, message):
        self.message = message
        raise Exception(message)


class CircularBuffer:
    def __init__(self, capacity):
        """
        The constructor class which instantiates a buffer and defines its capacity.
        """
        self.capacity = capacity
        from collections import deque
        self.buffer = deque([])

    def read(self):
        """
        Returns the older chunk of data from the buffer.
        """
        if len(self.buffer) == 0:
            BufferEmptyException("Buffer is empty!")
        return self.buffer.popleft()

    def write(self, data):
        """
        If buffer is not full write data to it else raises an exception.
        """
        if len(self.buffer) >= self.capacity:
            BufferFullException("Buffer is full!")
        for chunk in data:
            self.buffer.append(chunk)
        return self.buffer

    def overwrite(self, data):
        """
        If buffer is not full writes more data else remove the oldest chunk 
        and then writes new data.
        """
        for _, chunk in enumerate(data):
            # first check if buffer is not full
            if len(self.buffer) >= self.capacity:
                self.buffer.popleft()
            self.buffer.append(chunk)
        return self.buffer

    def clear(self):
        """Clears the buffer itself"""
        self.buffer.clear()


if __name__ == '__main__':
    c = CircularBuffer(3)
    c.write('5')
    c.write('4')
    c.write('3')
    c.write('2')
    c.write('1')
    print(c.read())
    print(c.read())
    print(c.read())
    print(c.read())
