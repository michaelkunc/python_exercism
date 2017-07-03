import collections as coll


class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):

    def __init__(self, length):
        self.elements = coll.deque(maxlen=length)

    def write(self, element):
        if len(self.elements) == self.elements.maxlen:
            raise BufferFullException
        else:
            self.elements.append(element)

    def read(self):
        if not self.elements:
            raise BufferEmptyException
        else:
            return self.elements.popleft()

    def clear(self):
        self.elements.clear()

    def overwrite(self, element):
        if len(self.elements) < self.elements.maxlen:
            self.write(element)
        else:
            self.elements.popleft()
            self.elements.append(element)
