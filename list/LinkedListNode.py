class Node:
    def __init__(self, data, node_next=None):
        self.data = data
        self.next = node_next


def print_list(head):
    while head:
        arrow = "->" if head.next else ""
        print(head.data + arrow, end='')
        head = head.next