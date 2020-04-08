class Heap:
    def __init__(self):
        self.container = []

    def peek(self):
        if len(self.container) == 0:
            return None
        return self.container[0]

    def pop(self):
        if len(self.container) == 0:
            return None

        if len(self.container) == 1:
            return self.container.pop(0)

        result = self.container[0]
        last = self.container.pop()
        self.container[0] = last
        self._sift_down(0)
        return result

    def push(self, element):
        self.container.append(element)
        self._sift_up(len(self.container) - 1)

    def __len__(self):
        return len(self.container)

    def _sift_up(self, idx):
        if idx == 0:
            return
        parent_idx = self.parent_idx(idx)
        if self.container[idx] > self.container[parent_idx]:
            self._swap(idx, parent_idx)
            self._sift_up(parent_idx)

    def _sift_down(self, idx):
        if idx >= len(self.container) // 2:
            return

        right_child_idx = self.right_child_idx(idx)
        left_child_idx = self.left_child_idx(idx)
        greater_child_idx = left_child_idx

        if right_child_idx < len(self.container) and self.container[right_child_idx] > self.container[left_child_idx]:
            greater_child_idx = right_child_idx

        if self.container[greater_child_idx] > self.container[idx]:
            self._swap(idx, greater_child_idx)
            self._sift_down(greater_child_idx)

    def _swap(self, i, j):
        self.container[i], self.container[j] = self.container[j], self.container[i]

    @staticmethod
    def parent_idx(idx):
        return (idx - 1) // 2

    @staticmethod
    def left_child_idx(idx):
        return idx * 2 + 1

    @staticmethod
    def right_child_idx(idx):
        return idx * 2 + 2


some_list = [10, 5, 3, 30, 25, 2, 0, -1, 200]
heap = Heap()

for e in some_list:
    heap.push(e)

actual = []
while len(heap) > 0:
    actual.append(heap.pop())

print(actual)
