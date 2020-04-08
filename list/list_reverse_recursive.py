class Node:
    def __init__(self, data, node_next=None):
        self.data = data
        self.next = node_next


def print_list(head):
    while head:
        arrow = "->" if head.next else ""
        print(head.data + arrow, end='')
        head = head.next


def reverse(node):
    prev, current = None, node
    while current:
        tmp = current.next
        current.next = prev
        prev = current
        current = tmp
    return prev


def reverse_recursive(node):
    head, _ = _reverse_recursive(node)
    return head


def _reverse_recursive(node):
    if node.next is None:
        return node, node

    head, tail = _reverse_recursive(node.next)
    node.next = None
    tail.next = node
    return head, node


node_1 = Node("A")
node_2 = Node("B")
node_3 = Node("C")
node_4 = Node("D")

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4

print_list(node_1)

new_head = reverse_recursive(node_1)

print("\n\nreversed recursive:")
print_list(new_head)

new_head = reverse(new_head)
print("\n\nreversed:")
print_list(new_head)
