class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def get_bounds(node, in_value, floor=None, ceil=None):
    if not node:
        return floor, ceil

    if in_value == node.value:
        return in_value, in_value

    elif in_value < node.value:
        floor, ceil = get_bounds(node.left, in_value, floor, node.value)

    elif in_value > node.value:
        floor, ceil = get_bounds(node.right, in_value, node.value, ceil)

    return floor, ceil


node_7 = Node(7)
node_5 = Node(5)
node_10 = Node(10)
node_7.left = node_5
node_7.right = node_10
node_3 = Node(3)
node_5.left = node_3
node_3.left = Node(1)
node_5.right = Node(6)
node_10.left = Node(9)
node_10.right = Node(20)

print(get_bounds(node_7, 7))

