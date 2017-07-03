import collections as coll


class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):

    def __init__(self, length):
        self.elements = coll.deque(maxlen=length)

    def write(self, element):
        self.elements.append(element)

    def read(self):
        if not self.elements:
            raise BufferEmptyException
        else:
            return self.elements.popleft()
