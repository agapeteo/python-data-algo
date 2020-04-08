class RingBuffer:
    def __init__(self, input_capacity):
        self.max_size = input_capacity
        self.container = [None] * input_capacity
        self.count = 0
        self.read_idx = 0
        self.write_idx = 0

    def enqueue(self, in_element):
        self.container[self.write_idx] = in_element
        self.write_idx = self._next_idx(self.write_idx)
        if self.count == self.max_size:
            self.read_idx = self.write_idx
        else:
            self.count = self.count + 1

    def dequeue(self):
        result = self.container[self.read_idx]

        self.read_idx = self._next_idx(self.read_idx)
        self.count = self.count - 1

        return result

    def elements(self):
        result = []
        cur_idx = self.read_idx
        for i in range(0, self.count):
            result.append(self.container[cur_idx])
            cur_idx = self._next_idx(cur_idx)
        return result

    def _next_idx(self, cur_idx):
        return (cur_idx + 1) % self.max_size


buf = RingBuffer(3)
buf.enqueue(1)
buf.enqueue(2)
buf.enqueue(3)
buf.enqueue(4)
buf.enqueue(5)

data = buf.dequeue()

print(data)
print(buf.elements())
