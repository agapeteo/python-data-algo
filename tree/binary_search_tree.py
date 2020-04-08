class Node:
    def __init__(self, input_value):
        self.value = input_value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None
        pass

    def add(self, input_value):
        if not self.root:
            self.root = Node(input_value)
            return
        self.add_to_node(self.root, input_value)

    def add_to_node(self, root_node, input_value):
        if input_value <= root_node.value:
            if not root_node.left:
                root_node.left = Node(input_value)
            else:
                self.add_to_node(root_node.left, input_value)
        else:
            if not root_node.right:
                root_node.right = Node(input_value)
            else:
                self.add_to_node(root_node.right, input_value)

    def __contains__(self, input_value):
        return self.contains_from_node(self.root, input_value)

    def contains_from_node(self, root_node, input_value):
        if not root_node:
            return False
        if root_node.value == input_value:
            return True
        if input_value < root_node.value:
            return self.contains_from_node(root_node.left, input_value)
        else:
            return self.contains_from_node(root_node.right, input_value)

    def elements_sorted(self):
        result_list = []
        self.elements_sorted_from_node(self.root, result_list)
        return result_list

    def elements_sorted_from_node(self, root_node, input_list):
        if not root_node:
            return
        self.elements_sorted_from_node(root_node.left, input_list)
        input_list.append(root_node.value)
        self.elements_sorted_from_node(root_node.right, input_list)

    def depth(self):
        return self.depth_from_node(self.root, 0)

    def depth_from_node(self, cur_node, cur_depth):
        if not cur_node or (not cur_node.left and not cur_node.right):
            return cur_depth

        return max(self.depth_from_node(cur_node.left, cur_depth + 1),
                   self.depth_from_node(cur_node.right, cur_depth + 1))


def test():
    tree = Tree()
    tree.add(6)
    tree.add(5)
    tree.add(3)
    tree.add(10)
    tree.add(12)
    print(tree.elements_sorted())
    print(10 in tree)
    print(11 in tree)
    print(tree.depth())
    tree.add(30)
    print(tree.depth())
    tree.add(300)
    print(tree.depth())


if __name__ == "__main__":
    test()
