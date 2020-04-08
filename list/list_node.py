class ListNode:
    def __init__(self, in_value):
        self.value = in_value
        self.next = None

    def append(self, in_value):
        cur_node = self
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = ListNode(in_value)

    def elements(self):
        result = []
        cur_node = self
        while cur_node:
            result.append(cur_node.value)
            cur_node = cur_node.next
        return result

    def size(self):
        size = 0
        cur_node = self
        while cur_node:
            size += 1
            cur_node = cur_node.next
        return size

    def delete_at_idx(self, idx):
        size = self.size()

        if idx not in range(1, size) or size < 2:
            return

        if size == 2:
            self.next = None
            return

        prev_node = self
        cur_node = prev_node.next
        next_node = cur_node.next
        cur_idx = 1

        while cur_idx < idx and next_node:
            prev_node = prev_node.next
            cur_node = cur_node.next
            next_node = next_node.next
            cur_idx += 1

        prev_node.next = next_node

    def deduplicate(self):
        unique_nodes = set()
        cur_node = self
        prev_node = None

        while cur_node:
            if cur_node.value in unique_nodes:
                prev_node.next = cur_node.next
            else:
                unique_nodes.add(cur_node.value)
                prev_node = cur_node

            cur_node = cur_node.next



node = ListNode(0)
node.append(1)
node.append(2)
node.append(2)
node.append(3)

node.append(4)
node.append(5)
node.append(5)
node.append(2)
node.deduplicate()

print(node.elements())

#
# some_set = set()
# some_set.add(ListNode(0).value)
# some_set.add(ListNode(0).value)
# some_set.add(ListNode(1).value)


# print(some_set)
#
# if ListNode(0).value in some_set:
#     print("yes")