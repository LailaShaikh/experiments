import Queue

"""
Interview question was asked in Invaria Tech.
Printing the all nodes of given tree from root to child from left to right traversal way
"""

class Node(object):
    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right
    def __str__(self):
        if self.left and self.right:
            return "{}-->L{}-->R{}".format(self.name, self.left.name, self.right.name)
        else:
            return "{}".format(self.name)


def print_traversed_tree(tree):
    root = tree
    q = Queue.Queue()
    first = True
    
    print root.name,
    def print_items(n):
        if n.left :
            q.put(n.left)         
            print n.left.name,
        if n.right:
            q.put(n.right)
            print n.right.name,

    while first or not q.empty():
        print_items(root)
        root = q.get()
        first = False

if __name__ == '__main__':
    L = Node('L')
    K = Node('K')
    J = Node('J')
    I = Node('I')
    H = Node('H')
    G = Node('G')
    F = Node('F', left=L)
    E = Node('E', left=J, right=K)
    D = Node('D', left=H, right=I)
    C = Node('C', left=F, right=G)
    B = Node('B', left=D, right=E)
    tree = Node('A', left=B, right=C)

    print print_traversed_tree(tree)
