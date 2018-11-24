class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None


def find_max_node(node):

    return max(node.data, node.left.data, node.right.data)


root = Tree()
root.data = 'root'
root.left = Tree()
root.left.data = 'left'
root.right = Tree()
root.right.data = 'right'

find_max_node(root)


