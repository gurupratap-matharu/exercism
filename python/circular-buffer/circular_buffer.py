class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer:
    def __init__(self, capacity):
        """
        The constructor class which instantiates an empty buffer with the desired capacity.
        """
        self.capacity = capacity
        self.buffer = []

    def read(self):
        """
        Returns the older chunk of data from the buffer.
        """
        if len(self.buffer) == 0:
            raise BufferEmptyException("Buffer is empty!")
        return self.buffer.pop(0)

    def write(self, data):
        """
        If buffer is not full writes data to it else raises an exception.
        """
        if len(self.buffer) >= self.capacity:
            raise BufferFullException("Buffer is full!")
        for chunk in data:
            self.buffer.append(chunk)
        return self.buffer

    def overwrite(self, data):
        """
        If buffer is not full writes more data else remove the oldest chunk and then writes new data.
        """
        for chunk in data:
            # first check if buffer is not full
            if len(self.buffer) >= self.capacity:
                self.buffer.pop(0)
            self.buffer.append(chunk)

        return self.buffer

    def clear(self):
        """Clears the buffer itself"""
        self.buffer.clear()
        return self.buffer
